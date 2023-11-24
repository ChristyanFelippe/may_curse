*** Settings ***
Variables           devices.py
Variables           variables.py  ${HOSTNAME}
Resource            ubuntu/Utils.robot


*** Keywords ***
Telnet Login
    Run Keyword If  '${NEW_IF}' == 'true'
    ...  Configure IP  ${TA_IP}  ${TA_IF}
    Telnet.Open Connection  ${IP}  port=${PORT}  timeout=3
    Telnet.Login  ${USERNAME}  ${PASSWORD}  ${USERNAME_PROMPT}  ${PASSWORD_PROMPT}  5 sec
    Telnet.Set Prompt  ${USR_PROMPT}

Telnet Logout
    Telnet.Close All Connections
    Run Keyword If  '${NEW_IF}' == 'true'
    ...  Remove IP  ${TA_IP}  ${TA_IF}

Enter exec mode
    Telnet.Write  enable
    Telnet.Set Prompt  ${EXC_PROMPT}

Enter config mode
    Enter exec mode
    Telnet.Write  configure terminal
    Telnet.Set Prompt  ${CFG_PROMPT}


Clear startup config and reboot
    Telnet.Write  clear startup config
    Telnet.Write  yes
    Telnet.Read Until Prompt
    Telnet.Write  reboot
    Telnet.Write  yes

Load configuration and reboot
    [Arguments]  ${IP}  ${FILE_NAME}
    Telnet.Write  load configuration tftp inet ${IP} ${FILE_NAME}
    Telnet.Write  y
    Sleep  5
    ${return} =  Telnet.Read
    Should Contain  ${return}  Download config file via TFTP successfully.
    Telnet.Write  reboot
    Telnet.Write  y
    Telnet.Close All Connections
    Sleep  10

Upload configuration
    [Arguments]  ${IP}  ${FILE_NAME}
    Telnet.Write  upload configuration tftp inet ${IP} ${FILE_NAME}
    Telnet.Write  y
    Sleep  5
    ${return} =  Telnet.Read
    Should Contain  ${return}  Upload config file via TFTP successfully.


Login And Load Standard Config
    Telnet Login
    Enter exec mode
    Load configuration and reboot  ${TA_IP}  ${STANDARD_CFG}
    Wait Until Keyword Succeeds  3 min  5 sec  Telnet Login
    Telnet Logout

Run show running config
    Telnet.Write  show running-config
    Telnet.Write Until Expected Output  ${SPACE}  ${HOSTNAME}  3 min  1 s
    Sleep  2
    ${return} =  Telnet.Read