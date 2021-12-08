*** Settings ***
Resource  resource.robot
Suite Setup  Open and Configure Browser
Suite Teardown  Close Browser
Test Setup  Run Keywords  Login  Go To Main Page
Test Teardown  Go to Logout Page

*** Test Cases ***
Main Page Open
    Main Page Should Be Open

Click Add Lukuvinkki Link 
    Click Link  Add lukuvinkki
    Add Lukuvinkki Page Should Be Open

Click View All Lukuvinkkis Link
    Click Link  View all lukuvinkkis
    Lukuvinkkiview Page Should Be Open
