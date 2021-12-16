*** Settings ***
Resource  resource.robot
Suite Setup  Open and Configure Browser
Suite Teardown  Close Browser
Test Setup  Run Keywords  Login
Test Teardown  Go To Logout Page

*** Test cases ***
# Sprint 3 acceptance criterias:
# As a user I can search by title

Search For Something That Doesnt Exist
    Go To Search Page
    Set Searchterm  ThisClearlyDoesntExist
    Submit Search
    Page Should Contain  Your search returned nothing

Search For Something That Exists
    Enter Book For Test
    Go To Search Page
    Set Searchterm  TestingSearchFunction
    Submit Search
    Page Should Contain  555550000

*** Keywords ***
Set Searchterm
    [Arguments]  ${searchterm}
    Input Text  searchterm  ${searchterm}  

Submit Search
    Click Button  submit

Enter Book For Test
    Go to Choose Type Page
    Select Radio Button  type  Book
    Click Button  submit
    Input Text  title  TestingSearchFunction
    Input Text  author  Stephen King
    Input Text  ISBN  555550000
    Click Button  save_button
