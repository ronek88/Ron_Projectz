### The purpose of this script is to play automatically banggood game

*** Settings ***
Documentation    Banggood game
Library          SeleniumLibrary
Library          DebugLibrary
Library          String

*** Test Cases ***
Banggood Game Automator
    [Tags]    banggood

    Open Browser    https://www.banggood.com/Casual-Game-Money-Box.html?utmid=15618&bid=37698    chrome

    #Log in to game
    Wait Until Element Is Visible      xpath=/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div
    Scroll Element Into View           xpath=/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div
    Click Element                      xpath=/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div
    Wait Until Element Is Visible      xpath=//*[@id="login-email"]
    Input Text                         xpath=//*[@id="login-email"]    rtischler11@gmail.com
    Input Password                     xpath=//*[@id="login-pwd"]    Kokotko88
    Click Element                      xpath=//*[@id="login-submit"]
#    Wait Until Element Is Visible      xpath=/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/div/span     timeout=60s
#    Scroll Element Into View           xpath=/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/div/span

    #Check the capacity and click the button
    FOR  ${i}  IN RANGE  1   9999999
        Wait Until Element Is Visible      xpath=/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/div/span     timeout=60s
        Scroll Element Into View           xpath=/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/div/span
        ${cap}   GET TEXT   xpath=/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/p[3]
        ${cap_int}  Fetch From Right    ${cap}  :
        ${cap_int_convert}   Convert To Integer    ${cap_int}
        Click Element       xpath=/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/div/span
        Log To Console    ${\n}Waiting ${cap_int_convert}s for new button click..
        Sleep      ${cap_int_convert+300}s
        Reload Page
    END



    [Teardown]    Close Browser

