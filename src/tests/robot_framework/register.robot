*** Settings ***
Resource  resource.robot
Suite Setup  Open and Configure Browser
Test Setup  Go to Logout Page
Test Teardown  Go to Logout Page
Suite Teardown  Close Browser

*** Test Cases ***
# Sprint 2 acceptance criterias:
# As a user, I can register to the service
Invalid Username Raises Error Message
    Go To Register Page
    Register With  1234567  veryStrongPassword  veryStrongPassword
    Page Should Contain  Username must contain only letters from a to z

Given Passwords Dont Match Error Message
    Go to Register Page
    Register With  toimivakayttajanimi  veryStrongPassword  veryStrongPassword2
    Page Should Contain  Passwords must match

Username Too Short Wont Create User
    Go to Register Page
    Register With  ab  veryStrongPassword  veryStrongPassword
    Register Page Should Be Open

Password Too Short Wont Create User
    Go To Register Page
    Register With  toimivakayttajanimi  12  12
    Register Page Should Be Open


*** Keywords ***
Register With
    [Arguments]  ${username}  ${password}  ${password_again}
    Input Text  username  ${username}
    Input Text  password  ${password}
    Input Text  password_confirmation  ${password_again}
    Click Button  Register
