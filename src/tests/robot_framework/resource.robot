*** Settings ***
Library  SeleniumLibrary
Library  ../../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.1 seconds
${HOME URL}  http://${SERVER}
${ADDLUKUVINKKI URL}  http://${SERVER}/addlukuvinkki
${LUKUVINKKIVIEW URL}  http://${SERVER}/lukuvinkkiview

*** Keywords ***
Open and Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Main Page Should Be Open
    Title Should Be  Lukuvinkki

Add Lukuvinkki Page Should Be Open
    Title Should Be  Lukuvinkki-Add

Lukuvinkkiview Page Should Be Open
    Title Should Be  Lukuvinkki-View

Go To Main Page
    Go To  ${HOME URL}

Go To Add Lukuvinkki Page
    Go To  ${ADDLUKUVINKKI URL}

Go To Lukuvinkkiview Page
    Go To  ${LUKUVINKKIVIEW URL}
