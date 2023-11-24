*** Settings ***
Library    String
Library    Telnet

Resource    ../resources/Utils.robot
Resource    ../resources/OLTUtils.robot
Library     ../resources/cmdLines.py

Test Setup       Telnet Login
# Test Teardown    Logout with Sleep

*** Variables ***
# ${IP}               10.100.25.43
# ${NEW_IF}           False
# ${PROMPT_OLT}       G16
# ${OLT_IP}           10.100.25.43
# ${HOSTNAME}         G16
 

*** Test Cases ***

Show User Commands
    FOR               ${command}               IN       @{USR_CMDs}
    Log      command
    ${show_usr} =     Catenate                 show     ${command}
    ${file_name} =    build_unique_commands    ${IP}    ${HOSTNAME}    ${EXC_PROMPT}    ${show_usr}    show_usr_cmds.txt
    END
#     BuiltIn.Sleep     3
#     END
#     Compare Files     ${file_name}

# Show User Commands
#     FOR               ${command}               IN       @{USR_CMDs}
#     Log   ${command}