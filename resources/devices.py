TA_TFTP_DIR = "/var/lib/tftpboot/"
TA_JENKINS_QAP_DIR = "/root/jenkinsQAP/"

CFG_FILE = "backup_GCOM_GPON.cfg"
STANDARD_CFG = "standart_cfg.cfg"
CFG_CMDs_FILE = "cfg_cmds.txt"
PORT = "23"
USERNAME = "admin"
PASSWORD = "admin"

CFG_CMDs_FILE_PATH = TA_JENKINS_QAP_DIR + CFG_CMDs_FILE
NEW_CFG_CMDs_FILE_PATH = TA_JENKINS_QAP_DIR + "new_" + CFG_CMDs_FILE
NEW_CFG_FILE = "new_" + CFG_FILE
CFG_FILE_PATH = TA_TFTP_DIR + CFG_FILE
NEW_CFG_FILE_PATH = TA_TFTP_DIR + "new_" + CFG_FILE

HARDWARE_VERSION = "'${HARDWARE_VERSION}'"
BOOTROM_VERSION = "'${BOOTROM_VERSION}'"
EPLD_VERSION = "'${EPLD_VERSION}'"
SOFTWARE_VERSION = "'${SOFTWARE_VERSION}'"

DEVICE_TYPES = [
    "i10-100  2301,1ETH (SFU)",
    "i10-420  1420G,4ETH+2POTS (SFU+HGU)",
    "i30-100  110Gi,1ETH (SFU)",
    "i40-100  R1,1ETH (SFU+HGU)",
    "i40-100-v2  R1v2,1ETH (SFU+HGU)",
    "i40-201  120AC,2ETH+WIFI(SFU+HGU)",
    "i40-211  121W,2ETH(LAN-1-FE+LAN-2-GE)+1POTS+WIFI (SFU+HGU)",
    "i40-400-1  140PoE,4ETH+PoE (SFU+HGU)",
    "i40-401  AX1800,4ETH+WIFI (SFU+HGU)",
    "i40-411  AX1800V,4ETH+1POTS+WIFI (SFU+HGU)",
    "i40-421  142NW,4ETH+2POTS+WIFI (SFU+HGU)",
    "i41-100  110Gb,1ETH (SFU)",
    "i41-201  1200R,2ETH+WIFI(SFU+HGU)",
    "i41-211  121AC,2ETH+1POTS+WIFI (SFU+HGU)",
    "i41-421  142NG,4ETH+2POTS+WIFI (SFU+HGU)"]

USR_CMDs = ["version", "system", "running-config", "cpu-statistics", "cpu-utilization", "cpu-classification", "memory",
            "utilization", "statistics"]

CPEs = [{
    "index": "0/1/1",
    "sn": "ZNTS-11111111",
    "line": "6",
    "model": "110Gb"

}, {
    "index": "0/1/2",
    "sn": "ITBS-2c9a91cf",
    "line": "1",
    "model": "110Gb"

}, {
    "index": "0/1/3",
    "sn": "ITBS-6eeae6e5",
    "line": "3",
    "model": "R1"
}, {
    "index": "0/1/4",
    "sn": "ITBS-0dfcb343",
    "line": "1",
    "model": "R1"
}, {
    "index": "0/3/1",
    "sn": "ITBS-0da64181",
    "line": "5",
    "model": "110Gb"
}, {
    "index": "0/3/2",
    "sn": "YL20-02000106",
    "line": "4",
    "model": "R1"
}]

modes_and_cmds = {
    ">": [],
    "#": ["enable"],
    "(config)#": ["enable", "configure terminal"],
    "(deploy-profile-rule)#": ["enable", "configure terminal", "deploy profile rule"],
    "(deploy-profile-line)#": ["enable", "configure terminal", "deploy profile line"],
    "(deploy-profile-dba)#": ["enable", "configure terminal", "deploy profile dba"],
    "(deploy-profile-vlan)#": ["enable", "configure terminal", "deploy profile vlan"],
    "(deploy-profile-unique)#": ["enable", "configure terminal", "deploy profile unique"],
    "(deploy-profile-alarm)#": ["enable", "configure terminal", "deploy profile alarm"],
    "(deploy-profile-rule-0/1/1)#": ["enable", "configure terminal", "deploy profile rule", "aim 0/1/1"],
    "(deploy-profile-line-1)#": ["enable", "configure terminal", "deploy profile line", "aim 1"],
    "(deploy-profile-dba-1)#": ["enable", "configure terminal", "deploy profile dba", "aim 1"],
    "(deploy-profile-vlan-1)#": ["enable", "configure terminal", "deploy profile vlan", "aim 1"],
    "(deploy-profile-unique-0/1/1)#": ["enable", "configure terminal", "deploy profile unique", "aim 0/1/1"],
    "(deploy-profile-alarm-1)#": ["enable", "configure terminal", "deploy profile alarm", "aim 1"],
    "(config-if-gpon-0/1)#": ["enable", "configure terminal", "interface gpon 0/1"],
    "(config-if-ethernet-1/1)#": ["enable", "configure terminal", "interface ethernet 1/1"],
    "(config-if-pon-0/1)#": ["enable", "configure terminal", "interface pon 0/1"],
    "(config-if-vlanInterface-1)#": ["enable", "configure terminal", "interface vlan-interface 1"],
    "(deploy-profile-wifi-1)#": ["enable", "configure terminal", "deploy profile wifi", "aim 1"],
    "(onu-0/1/1)#": ["enable", "configure terminal", "onu 0/1/1"]
}
