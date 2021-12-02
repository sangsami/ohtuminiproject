*** Settings ***
Resource  resource.robot
Suite Setup  Open and Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Add Lukuvinkki Page

*** Test Cases ***
Add Lukuvinkki With Title And Author
    Set Title  Kärpästen herra
    Set Author  William Golding
    Save
    Add Should Succeed

Add Existing Lukuvinkki
    Set Title  Kärpästen herra
    Set Author  William Golding
    Save
    Add Should Fail With Message  The lukuvinkki already exists

Add Empty Lukuvinkki
    Save
    Add Should Fail With Message  Check that you have entered atleast a title and an author.


*** Keywords ***
Add Should Succeed
    Add Lukuvinkki Page Should Be Open
    Page Should Contain  The lukuvinkki was saved.

Add Should Fail With Message
    [Arguments]  ${message}
    Add Lukuvinkki Page Should Be Open
    Page Should Contain  ${message}

View Should Succeed With Message
    [Arguments]  ${lukuvinkki}
    Add Lukuvinkki Page Should Be Open
    Page Should Contain  ${lukuvinkki}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Save
    Click Button  save_button

Click View Lukuvinkkis
    Click button  view_button