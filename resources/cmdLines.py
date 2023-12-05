"""
This file has methods to iterate over the gcom CLI
"""
# !/usr/bin/python3
import telnetlib
import re, itertools, sys

from robot.api.deco import keyword
from robot.api import logger

from devices import *
from variables import get_variables

not_commands = ['?', '....press', 'commands:', '^']
val_types = ['INTEGER', 'STRING', 'A.B.C.D', 'X:X::X:X', 'H:H:H:H:H:H', 'HH:MM:SS', 'YYYY/MM/DD', 'NUMBER']
cmd_end = '<enter>'
FAIL = '\033[91m'
ENDC = '\033[0m'
all_chars = (chr(i) for i in range(sys.maxunicode))
categories = {'Cc'}
control_chars = ''.join(map(chr, itertools.chain(range(0x00, 0x20), range(0x7f, 0xa0))))
control_char_re = re.compile('[%s]' % re.escape(control_chars))
loop_cmds = ['logging', 'ping', 'debug', 'alarm', 'running-config', 'dot1x', 'startup-config', 'ping6', 'snmp-server',
             'access-list', "onu-type", "pppoeplus", "rate-limit", "traffic-priority", "onu-classification",
             "onu-opm-threshold", "tracert", "tracert6", "onu", "ip", "ont", "pcap"]
DEBUG = False


def remove_control_chars(s):
    s = s.replace('[76C', '')
    s = s.replace('[76D', '')
    s = s.replace('[1B', '')
    s = s.replace('[1A', '')
    s = s.replace('[74D', '')
    s = s.replace('[73D', '')
    s = s.replace('[K', '')
    s = s.replace('\x1b', '')
    s = s.replace("....press ENTER to next line, CTRL_C to break, other key to next page.... ",'')
    return s


def open_telnet(ip, username_prompt, password_prompt):
    tn = telnetlib.Telnet(ip)
    tn.read_until(username_prompt.encode("ascii"))
    tn.write(USERNAME.encode('ascii') + b"\n")
    tn.read_until(password_prompt.encode("ascii"))
    tn.write(PASSWORD.encode('ascii') + b"\n")
    return tn


def read_until_prompt(tn, prompt):
    b = tn.read_until(prompt.encode('ascii'), timeout=3)
    t = b.decode('utf-8', 'ignore')
    while prompt not in t:
        if 'CR->exit' in t:
            tn.write('\r'.encode('ascii'))
        else:
            tn.write(' '.encode('ascii'))
        new_lines = tn.read_until(prompt.encode('ascii'), timeout=1).decode('utf-8', 'ignore')
        t += new_lines
    return t


def look_tree(tn, prompt, command=''):
    tn.write((command + ' ?').encode('ascii'))
    tn.read_until('?'.encode('ascii')).decode('utf-8', 'ignore')
    return read_until_prompt(tn, prompt)


# get make value for commands
def get_make(arg):
    if 'A.B.C.D' in arg.name:
        arg.name = '1.1.1.1'
    elif 'X:X::X:X/M' in arg.name:
        arg.name = 'A:A::A:A/1'
    elif 'X:X::X:X' in arg.name:
        arg.name = 'A:A::A:A'
    elif 'H:H:H:H:H:H' in arg.name:
        arg.name = 'A:A:A:A:A:A'
    elif 'STRING' in arg.name:
        if 'ethernet' in arg.upper.name:
            arg.name = '1/1'
        elif 'gpon' in arg.upper.name or 'pon' in arg.upper.name:
            arg.name = '0/1'
        elif 'interface' in arg.upper.name:
            arg.name = 'e1/1'
        elif 'ONT' in arg.desc:
            arg.name = '0/1/1'
        elif 'profile' in arg.desc and 'index' in arg.desc:
            arg.name = '1'
        elif 'HEX' in arg.desc:
            arg.name = '0000000000000000'
        elif 'SN:' in arg.desc:
            arg.name = 'AAAA-AAAAAAAA'
        elif 'UTC' in arg.desc:
            arg.name = '1'
        elif 'object identifier' in arg.desc:
            arg.name = '1.3.6.1.2.1.16.1.1.1.5.1'
        elif 'dBm' in arg.desc:
            arg.name = '-10'
        else:
            arg.name = get_str(arg.name)
    elif 'HH:MM:SS' in arg.name:
        arg.name = '11:11:11'
    elif 'YYYY/MM/DD' in arg.name:
        arg.name = '2000/11/11'
    elif 'NUMBER' in arg.name:
        arg.name = '1'
    elif 'INTEGER' in arg.name:
        val = arg.name[arg.name.find('<') + 1:arg.name.find('-')]
        arg.name = val


def get_str(name):
    ret = ''
    val = name[name.find('<') + 1:name.find('-')]
    for i in range(int(val)):
        ret += 'c'
    return ret


class Command:
    def __init__(self, name, desc='', upper=None, type='cmd'):
        self.name = name
        self.args = []
        self.desc = desc
        self.upper = upper
        self.type = type

    def __str__(self):
        return self.name


# build command line from comamnd list
def build_command(cmd, line=None):
    if cmd.upper is not None:
        build_command(cmd.upper, line)
    line.append(cmd.name)


# get whole command line, print in console and  wirte to the report file
def enter_and_check(cmd, report_file):
    cmds = []
    build_command(cmd, cmds)
    cmds.pop()
    cmds = ' '.join(cmds) + ' '
    with open(report_file, "a") as myfile:
        myfile.write(cmds + "\n")
    if DEBUG:
        print(cmds)


def loop(tn, cmd, prompt, report_file):
    text = look_tree(tn, prompt, cmd.name)
    lines = text.split('\n')
    for line in lines:
        if line.startswith(chr(13)):
            continue
        if not len(line):
            continue
        if line.startswith(chr(32)):
            continue
        if line.rstrip(chr(13)).endswith('^'):
            break
        not_command_in_line = False
        for not_command in not_commands:
            if not_command in line:
                not_command_in_line = True
        if not_command_in_line:
            continue
        line_split = line.split()
        arg = Command(line_split[0], ' '.join(line_split[1:]))
        arg.upper = cmd
        if arg.name == cmd_end:
            enter_and_check(arg, report_file)
        if arg.name != cmd_end:
            for type in val_types:
                if type in arg.name:
                    arg.type = 'val'
                    get_make(arg)
                    break
            if arg.type == 'val' or not check_repeat(arg):
                cmd.args.append(arg)
                loop(tn, arg, prompt, report_file)
                clean_cmd(tn, arg)


def clean_cmd(tn, cmd):
    tn.write('\b'.encode('ascii'))
    for i in range(len(cmd.name)):
        tn.write('\b'.encode('ascii'))


def check_repeat_loop(command, arg):
    for a in command.args:
        ret = check_repeat_loop(a, arg)
        if ret:
            return True
        if arg.name == a.name and arg.desc == a.desc:
            return True
    return False


def check_repeat(arg):
    cmd = arg
    while cmd.upper is not None and cmd.upper.name != '' and cmd.upper.name != 'show' and cmd.upper.name != 'no':
        cmd = cmd.upper
    if cmd.name in loop_cmds:
        return check_repeat_loop(cmd, arg)
    return False


@keyword
def build_unique_commands(ip, hostname, prompt, command, report_file):
    variables = get_variables(hostname)
    for v in variables.values():
        logger.info(f"Variable: {v}")
        not_commands.append(v)

    tn = open_telnet(ip, variables['USERNAME_PROMPT'], variables['PASSWORD_PROMPT'])
    enter_mode(tn, hostname, prompt)

    cmd = get_last_command(tn, command)
    
    loop(tn, cmd, prompt, report_file)
    tn.close()

    return report_file


def get_last_command(tn, command):
    commands = command.split()
    if len(commands) > 1:
        command = Command(commands[0])
        tn.write((command.name + ' ').encode('ascii'))
        for i in range(1, len(commands)):
            command = Command(commands[i], upper=command)
            if i < (len(commands) - 1):
                tn.write((command.name + ' ').encode('ascii'))

    else:
        command = Command(command)
    return command


def get_mode_commands(description, lines):
    ret = lines.copy()
    for line in lines:
        if not description in line:
            ret.remove(line)
        else:
            ret.remove(line)
            for i in range(0, len(ret)):
                if ret[i].startswith(chr(13)):
                    ret = ret[:i]
                    return ret
    return ret

def clean_line(tn, prompt):
    tn.write("?".encode("ascii"))
    line = tn.read_until("\r\n".encode("ascii"))
    for c in range(len(line)):
        tn.write('\b'.encode('ascii'))
    tn.write('\n'.encode('ascii'))
    read_until_prompt(tn, prompt)
    read_until_prompt(tn, prompt)


#
@keyword
def build_mode_commands(ip, hostname, prompt, description, command=None):
    variables = get_variables(hostname)
    for v in variables.values():
        not_commands.append(v)

    tn = open_telnet(ip, variables['USERNAME_PROMPT'], variables['PASSWORD_PROMPT'])
    enter_mode(tn, hostname, prompt)
    commands = get_commands(tn, prompt, description)
    report_file = (re.sub(r'\W+', '', description)).replace(" ", "") + ".txt"
    for cmd in commands:
        print(f"commands : {cmd}")
        if cmd.name == "show":
            continue
        if command is not None:
            c = Command(command)
            tn.write((c.name + ' ').encode('ascii'))
            cmd = Command(cmd.name, upper=c)
            loop(tn, cmd, prompt, report_file)
            clean_line(tn, prompt)
        else:
            loop(tn, cmd, prompt, report_file)
            clean_line(tn, prompt)

    tn.close()
    return report_file

def enter_mode(tn, hostname, prompt):
    prompt = prompt.replace(hostname, "")
    cmds = modes_and_cmds.get(prompt)
    for cmd in cmds:
        print(f"cmds : {cmd}")
        tn.write((cmd + "\n").encode("ascii"))
    output = tn.read_until(prompt.encode('ascii'))
    print(f"output is {output}")

def get_commands(tn, prompt, description):
    text = look_tree(tn, prompt, "")
    text = remove_control_chars(text)
    lines = text.split('\n')
    lines = get_mode_commands(description, lines)
    cmds = []
    for line in lines:
        print(f"line is {line}")
        if line.startswith(chr(13)):
            continue
        if not len(line):
            continue
        if line.startswith(chr(32)):
            continue
        if line.rstrip(chr(13)).endswith('^'):
            continue
        not_command_in_line = False
        line_split = line.split()
        for not_command in not_commands:
            if not_command in line:
                not_command_in_line = True
        if not_command_in_line:
            continue
        arg = Command(line_split[0], ' '.join(line_split[1:]))
        cmds.append(arg)
    return cmds

def get_aim(prompt):
    indexes = []
    i = 0
    for c in prompt:
        if c.isdigit():
            indexes.append(i)
        i = i + 1
    return indexes

if __name__ == '__main__':
    build_mode_commands("10.100.25.43", "G16", "G16(deploy-profile-dba-1)#", "C_entry_dba (c_entry_dba) mode commands")
