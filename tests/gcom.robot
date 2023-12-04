*** Settings ***
Library    String
Library    Telnet
Library    OperatingSystem

Resource    ../resources/Utils.robot
Resource    ../resources/OLTUtils.robot
Library     ../resources/cmdLines.py

Test Setup       Telnet Login
Test Teardown    Logout with Sleep

*** Variables ***
# ${IP}               10.100.25.43
# ${NEW_IF}           False
# ${PROMPT_OLT}       G16
# ${OLT_IP}           10.100.25.43
# ${HOSTNAME}         G16
 

*** Test Cases ***

# Show User Commands
#     OperatingSystem.Remove File     show_usr_cmds.txt
#     FOR               ${command}               IN       @{USR_CMDs}
#     ${show_usr} =     Catenate                 show     ${command}
#     ${file_name} =    build_unique_commands    ${IP}    ${HOSTNAME}    ${EXC_PROMPT}    ${show_usr}    show_usr_cmds.txt
#     BuiltIn.Sleep     1
#     END
#     Compare Files     ${file_name}

# Config Commands
#     ${file_name} =    build_mode_commands    ${IP}    ${HOSTNAME}    ${CFG_PROMPT}    Global configure (config) mode commands:
#     ${file_name} =    build_mode_commands    ${IP}    ${HOSTNAME}    ${CFG_PROMPT}    Global configure (config) mode commands:    show
#     Compare Files     ${file_name}

Profile DBA Commands
    ${file_name} =    build_mode_commands    ${IP}    ${HOSTNAME}    ${PROFILE_DBA1_PROMPT}    C_entry_dba (c_entry_dba) mode commands:
    Compare Files     ${file_name}


*** Keywords ***
Compare Files
    [Arguments]                   ${file_name}
    ${file1} =                    Get File        ${file_name}
    ${file_name2} =               Catenate        SEPARATOR=       cmds/gpon/    ${file_name}
    ${file2} =                    Get File        ${file_name2}
    Should Be Equal As Strings    ${file1}        ${file2}

Logout with Sleep
    Telnet Logout
    BuiltIn.Sleep    1