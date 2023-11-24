*** Settings ***
Library             OperatingSystem

*** Keywords ***
Configure IP
    [Arguments]  ${IP}  ${IF}
    ${output} =  Run  ip a a ${IP}/24 dev ${IF}
    Log  ${output}
    ${output} =  Run  ip a | grep ${IF}
    Log  ${output}
    Should Contain  ${output}  ${IF}: <BROADCAST,MULTICAST,UP,LOWER_UP>
    Should Contain  ${output}  inet ${IP}/24 scope global ${IF}

Remove IP
    [Arguments]  ${IP}  ${IF}
    ${output} =  Run  ip a d ${IP}/24 dev ${IF}
    Log  ${output}
    ${output} =  Run  ip a | grep ${IF}
    Log  ${output}
    Should Not Contain  ${output}  inet ${IP}/24 scope global ${IF}