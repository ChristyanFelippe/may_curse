*** Settings ***
Library    String
Library    Telnet

# Resource    ../resources/ubuntu/Utils.robot
Resource    ../resources/OLTUtils.robot
# Library     ../resources/cmdLines.py

Test Setup       Telnet Login
Test Teardown    Logout with Sleep

*** Variables ***
${IP}    10.100.34.66
${HOSTNAME}    G8
${NEW_IF}    False

*** Test Cases ***

Exemplo de Teste
    Log    ${IP}
    Log    ${HOSTNAME}
    Log    ${NEW_IF}
