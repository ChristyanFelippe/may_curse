*** Settings ***
Library    String
Library    Telnet

Resource    ../resources/Utils.robot
Resource    ../resources/OLTUtils.robot
Library     ../resources/cmdLines.py

Test Setup       Telnet Login
# Test Teardown    Logout with Sleep

*** Variables ***
${IP}    10.100.25.43
${NEW_IF}    False
${PROMPT_OLT}   G16
${OLT_IP}     10.100.25.43

*** Test Cases ***

Exemplo de Teste
    Log    ${IP}
    Log    ${NEW_IF}
