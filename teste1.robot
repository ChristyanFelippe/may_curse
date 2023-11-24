*** Settings ***
Library  SeleniumLibrary

Test Teardown  SeleniumLibrary.Close Browser

*** Test Cases ***
Cenário: Previsão do tempo em Florianópolis
    SeleniumLibrary.Set Selenium Speed 	 value=0.1
    SeleniumLibrary.Open Browser   url=http://www.google.com.br/  browser=chrome
    SeleniumLibrary.Maximize Browser Window
    SeleniumLibrary.Click Element 	 name=q
    Input Text 	 name=q 	 Previsão do tempo em Biguaçu/SC
    SeleniumLibrary.Click Element 	 name=btnK 	 modifier=False
    sleep  1s
    SeleniumLibrary.Wait Until Page Contains 	 Previsão do tempo em Biguaçu/SC 	 timeout=5s 	 error=None
# robot -d ./reports .\google_search_test.robot