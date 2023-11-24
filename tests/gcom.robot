*** Settings ***
Library    String
Library    Telnet

# Resource    ../resources/ubuntu/Utils.robot
# Resource    ../resources/OLTUtils.robot
# Library     ../resources/cmdLines.py

# Test Setup       Telnet Login
# Test Teardown    Logout with Sleep

*** Variables ***
${VARIAVEL1}    Valor da Variável 1
${VARIAVEL2}    Valor da Variável 2


*** Test Cases ***

Exemplo de Teste
    Log    ${VARIAVEL1}
    Log    ${VARIAVEL2}
    # ${file_name} =    build_mode_commands    ${IP}    ${HOSTNAME}    ${EXC_PROMPT}    System (system) mode commands:
    # Compare Files     ${file_name}



*** Keywords ***
# Compare Files
#     [Arguments]                   ${file_name}
#     ${file1} =                    Get File        ${file_name}
#     ${file_name2} =               Catenate        SEPARATOR=       resources/cmds/gpon/    ${file_name}
#     ${file2} =                    Get File        ${file_name2}
#     Should Be Equal As Strings    ${file1}        ${file2}


# Logout with Sleep
#     Telnet Logout
#     BuiltIn.Sleep    3