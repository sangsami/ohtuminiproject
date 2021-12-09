*** Settings ***
Resource  resource.robot
Suite Setup  Open and Configure Browser
Suite Teardown  Close Browser
Test Setup  Run Keywords  Login
Test Teardown  Go to Logout Page

*** Test Cases ***
Lukuvinkkiview Page Is Open
    Lukuvinkkiview Page Should Be Open

Click Go to main Page
    Click Link  Go to main page
    Main Page Should Be Open

Click Add A New Lukuvinkki Link 
    Click Link  Add a new lukuvinkki
    Choosetype Page Should Be Open

Click Logout
    Click Link  Logout
    Logout Page Should Be Open

