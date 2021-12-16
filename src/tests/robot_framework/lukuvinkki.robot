*** Settings ***
Resource  resource.robot
Suite Setup  Open and Configure Browser
Suite Teardown  Close Browser
Test Setup  Run Keywords  Login
Test Teardown  Go To Logout Page

*** Test Cases ***
Add Empty Book Lukuvinkki
    Go to Choose Type Page
    Select Book As Type
    Submit
    Save
    Add Should Fail With Message  Check that you have entered atleast a title.

Add Book Without Title
    Go to Choose Type Page
    Select Book As Type
    Submit
    Set Author  William Golding
    Save
    Add Should Fail With Message  Check that you have entered atleast a title.

Add A Book With Just A Title
    Go to Choose Type Page
    Select Book As Type
    Submit
    Set Title  Kärpästen herra
    Save
    Add Should Succeed

All Added Book Info Visible On View Page
    Go to Choose Type Page
    Select Book As Type
    Submit
    Set Title  Hohto
    Set Author  Stephen King
    Set ISBN  20091039043904
    Set Description  Kauhuromaani vuodelta 1977
    Set Link  https://fi.wikipedia.org/wiki/Hohto
    Set Comment  447 sivua pitkä
    Save
    Go to Lukuvinkkiview Page
    Page Should Contain All Info  Hohto  Stephen King  Kauhuromaani vuodelta 1977  https://fi.wikipedia.org/wiki/Hohto  447 sivua pitkä

Add Podcast
    Go to Choose Type Page
    Select Podcast As Type
    Submit
    Set Title  The Joe Rogan Experience
    Save
    Add Should Succeed

Add Youtube Video
    Go To Choose Type Page
    Select Youtube As Type
    Submit
    Set Title  Introduction to Programming and Computer Science - Full Course
    Save
    Add Should Succeed

Add Youtube Video From URL
    Go To Choose Type Page
    Select Youtube As Type
    Set Youtube URL  https://www.youtube.com/watch?v=Lmw4lzjEqD8
    Submit
    Youtube Add Should Contain  seal.mp4
    Save
    Add Should Succeed

Add Blog Post
    Go to Choose Type Page
    Select Blog Post As Type
    Submit
    Set Title  esimerkki blogi postaus
    Save
    Add Should Succeed

View Lukuvinkki Button Takes to Lukuvinkkiview Page
    Go to Choose Type Page
    Select Book As Type
    Submit
    Click View Lukuvinkkis
    Lukuvinkkiview Page Should Be Open

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

Youtube Add Should Contain 
    [Arguments]  ${title}
    Textfield Should Contain  title  ${title}
    
Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Link
    [Arguments]  ${link}
    Input Text  link  ${link}

Set Youtube URL
    [Arguments]  ${link}
    Input Text  youtube-url  ${link}

Set Description
    [Arguments]  ${description}
    Input Text  description  ${description}

Set Comment
    [Arguments]  ${comment}
    Input Text  comment  ${comment}

Set ISBN
    [Arguments]  ${ISBN}
    Input Text  ISBN  ${ISBN}

Save
    Click Button  save_button

Submit
    Click Button  submit

Click View Lukuvinkkis
    Click Button  view_button

Select Podcast As Type
    Select Radio Button  type  Podcast

Select Book As Type
    Select Radio Button  type  Book

Select Blog Post As Type
    Select Radio Button  type  blog_post

Select Youtube As Type
    Select Radio Button  type  Youtube