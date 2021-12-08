*** Settings ***
Resource  resource.robot
Suite Setup  Run Keywords  Open and Configure Browser  Login
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

Add Lukuvinkki Without Title
    Set Author  William Golding
    Save
    Add Should Fail With Message  Check that you have entered atleast a title and an author.

Add Lukuvinkki Without Author
    Set Title  Kärpästen herra
    Save
    Add Should Fail With Message  Check that you have entered atleast a title and an author.

Add Non Empty Lukuvinkki Without Author
    Set Description  Romaani vuodelta 1954
    Save
    Add Should Fail With Message  Check that you have entered atleast a title and an author.

Added Lukuvinkki Visible On View Page
    Set Title  Hohto
    Set Author  Stephen King
    Set Description  Kauhuromaani vuodelta 1977
    Set Link  https://fi.wikipedia.org/wiki/Hohto
    Set Comment  447 sivua pitkä
    Save
    Go to Lukuvinkkiview Page
    Page Should Contain All Info  Hohto  Stephen King  Kauhuromaani vuodelta 1977  https://fi.wikipedia.org/wiki/Hohto  447 sivua pitkä

View Lukuvinkki Button Takes to Lukuvinkkiview Page
    Click View Lukuvinkkis
    Lukuvinkkiview Page Should Be Open

Save Button Wont Change The Page
    Save
    Add Lukuvinkki Page Should Be Open

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

Page Should Contain All Info
    [Arguments]  ${title}  ${author}  ${description}  ${link}  ${comment}
    Page Should Contain  ${title}
    Page Should Contain  ${author}
    Page Should Contain  ${description}
    Page Should Contain  ${link}
    Page Should Contain  ${comment}
Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Link
    [Arguments]  ${link}
    Input Text  link  ${link}

Set Description
    [Arguments]  ${description}
    Input Text  description  ${description}

Set Comment
    [Arguments]  ${comment}
    Input Text  comment  ${comment}

Save
    Click Button  save_button

Click View Lukuvinkkis
    Click button  view_button