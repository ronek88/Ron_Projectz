### The purpose of this script is to download file without popup error

*** Settings ***
Documentation    SaveFileExample
Library          ExtSeleniumLibrary.py

*** Test Cases ***
SAVE FILE EXAMPLE
    [Tags]    FILE SAVE

    ExtSeleniumLibrary.OPEN CHROME WITH DOWNLOAD
    ...  https://www.thinkbroadband.com/download

    SLEEP  2s
    Execute JavaScript      window.scrollBy(1500, 900);

    CLICK ELEMENT           xpath=//*[@id="main-col"]/div/div/div[6]/p[2]/a[1]

    SLEEP  30s
    CLOSE BROWSER
