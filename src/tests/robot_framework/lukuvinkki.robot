*** Settings ***
Resource  resource.robot
Library  DateTime
Suite Setup  Open and Configure Browser
Suite Teardown  Close Browser
Test Setup  Run Keywords  Login
Test Teardown  Go To Logout Page

*** Test Cases ***
# Sprint 1 Acceptance criterias:

# As a user I can add a book to my list
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

# As a user I can add a link to my lukuvinkki, As a user I can add a link to my lukuvinkki, As a user I can add a comment to my lukuvinkki
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

#As a user I can add a podcast to my list, As a user I can define type for my lukuvinkki, As a user I can add different info to the lukuvinkki depending on it's type
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

Add Blog Post
    Go to Choose Type Page
    Select Blog Post As Type
    Submit
    Set Title  esimerkki blogi postaus
    Save
    Add Should Succeed

# As a user, I can see a list of all my lukuvinkkis
View Lukuvinkki Button Takes to Lukuvinkkiview Page
    Go to Choose Type Page
    Select Book As Type
    Submit
    Click View Lukuvinkkis
    Lukuvinkkiview Page Should Be Open

# Sprint 3 Acceptance criterias:
#As a user, I can mark my lukuvinkki with a timestamp
Changing Status To Read Shows Timestamp
    Click Logout
    Go To Register Page
    Register With  tyhjalukuvinkkikayttaja  veryStrongPassword  veryStrongPassword
    Goto Login Page
    Login With  tyhjalukuvinkkikayttaja  veryStrongPassword
    Go to Choose Type Page
    Select Book As Type
    Submit
    Set Title  Dyyni
    Save
    Click View Lukuvinkkis
    Change Status
    Change Status Should Succeed

# As a user I can add lukuvinkki by youtube-url
Add Youtube Video From URL
    Go To Choose Type Page
    Select Youtube As Type
    Set Youtube URL  https://www.youtube.com/watch?v=Lmw4lzjEqD8
    Submit
    Youtube Add Should Contain  seal.mp4  Storklathe
    Save
    Add Should Succeed

Add Youtube Video With Bad URL
    Go To Choose Type Page
    Select Youtube As Type
    Set Youtube URL  nolink
    Submit
    Add Should Fail With Message  Could not find any youtube videos with provided url

# As a user, I can add a lukuvinkki tied to my account
Can See Private Lukuvinkki Added By Another account
    Go to Choose Type Page
    Select Book As Type
    Submit
    Set Title  Harry Potter ja Azkabanin vanki
    Set Author  J.K. Rowling
    Set ISBN  9789513187040
    Set Description   J. K. Rowlingin teossarjan kolmas osa
    Set Link  https://www.adlibris.com/fi/kirja/harry-potter-ja-azkabanin-vanki-9789513187040
    Set Comment  Nidottu
    Set Public
    Save
    Go to Lukuvinkkiview Page
    Click Logout
    Goto Login Page
    Login With  tyhjalukuvinkkikayttaja  veryStrongPassword
    Page Should Contain All Info  Harry Potter ja Azkabanin vanki  J.K. Rowling  J. K. Rowlingin teossarjan kolmas osa  https://www.adlibris.com/fi/kirja/harry-potter-ja-azkabanin-vanki-9789513187040  Nidottu

Cannot See Private Lukuvinkki Added By Another account
    Go to Choose Type Page
    Select Book As Type
    Submit
    Set Title  Taru Sormusten Herrasta: Sormuksen ritarit
    Set Author  J. R. R. Tolkien
    Set ISBN  9789510468265
    Set Description  Kaikenikäisten klassikko, tulvillaan seikkailua, jännitystä ja huumoria!
    Set Link  https://www.adlibris.com/fi/e-kirja/taru-sormusten-herrasta-sormuksen-ritarit-9789510468265
    Set Comment  E-kirja
    Save
    Go to Lukuvinkkiview Page
    Click Logout
    Goto Login Page
    Login With  tyhjalukuvinkkikayttaja  veryStrongPassword
    Page Should Contain Not All Info  Taru Sormusten Herrasta: Sormuksen ritarit  J. R. R. Tolkien  Kaikenikäisten klassikko, tulvillaan seikkailua, jännitystä ja huumoria!  https://www.adlibris.com/fi/e-kirja/taru-sormusten-herrasta-sormuksen-ritarit-9789510468265  E-kirja

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

Page Should Contain Not All Info
    [Arguments]  ${title}  ${author}  ${description}  ${link}  ${comment}
    Page Should Not Contain  ${title}
    Page Should Not Contain  ${author}
    Page Should Not Contain  ${description}
    Page Should Not Contain  ${link}
    Page Should Not Contain  ${comment}

Youtube Add Should Contain 
    [Arguments]  ${title}  ${author}
    Textfield Should Contain  title  ${title}
    Textfield Should Contain  author  ${author}

Change Status Should Succeed
    ${date} =  Get Current Date  result_format=%d.%m.%y
    Page Should Contain  ${date}
 
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

Set Public
    Select Checkbox  visibility
    
Change Status
    Click Button  change_status_button

Save
    Click Button  save_button

Submit
    Click Button  submit

Click Logout
    Click Link  Logout
    Logout Page Should Be Open

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