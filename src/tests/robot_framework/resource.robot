*** Settings ***
Library  SeleniumLibrary
Library  ../../AppLibrary.py

*** Variables ***
${SERVER}  127.0.0.1:5000
${BROWSER}  chrome
${DELAY}  0.0 seconds
${HOME URL}  http://${SERVER}
${CHOOSETYPE_URL}  http://${SERVER}/choosetype
${ADDLUKUVINKKI URL}  http://${SERVER}/addlukuvinkki
${LUKUVINKKIVIEW URL}  http://${SERVER}/lukuvinkkiview
${CHANGELUKUVINKKI URL}  http://${SERVER}/changelukuvinkki
${CHANGETYPE URL}  http://${SERVER}/changetype
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register
${LOGOUT URL}  http://${SERVER}/logout
${SEARCH URL}  http://${SERVER}/search

*** Keywords ***
Open and Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Main Page Should Be Open
    Title Should Be  Lukuvinkki

Choosetype Page Should Be Open
    Title Should Be  Choose type for new lukuvinkki

Add Lukuvinkki Page Should Be Open
    Title Should Be  Lukuvinkki-Add

Lukuvinkkiview Page Should Be Open
    Title Should Be  Lukuvinkki-View

Changelukuvinkki Page Should Be Open
    Title Should Be  Change current lukuvinkki

Changetype Page Should Be Open
    Title Should Be  Change lukuvinkkitype if needed

Logout Page Should Be Open
    Title Should Be  Logout

Register Page Should Be Open
    Title Should Be  Register

Login Page Should Be Open 
    Title Should Be  Login

Go To Main Page
    Go To  ${HOME URL}

Go to Choose Type Page
    Go to  ${CHOOSETYPE_URL}

Go To Add Lukuvinkki Page
    Go To  ${ADDLUKUVINKKI URL}

Go To Lukuvinkkiview Page
    Go To  ${LUKUVINKKIVIEW URL}

Go To Changelukuvinkki Page
    Go To  ${CHANGELUKUVINKKI URL}

Go To Changetype Page
    Go To  ${CHANGETYPE URL}

Go To Login Page
    Go To  ${LOGIN URL}

Go To Logout Page
    Go To  ${LOGOUT URL}

Go To Register Page
    Go To  ${REGISTER URL}

Go To Search Page
    Go To  ${SEARCH URL}

Login
    Go To Login Page
    Input Text  username  guest
    Input Text  password  veryStrongPassword
    Click Button  Login