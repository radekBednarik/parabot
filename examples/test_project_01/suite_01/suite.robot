**Settings***
Library           SeleniumLibrary
Library           OperatingSystem
Suite Setup       Set the Things Up        
Suite Teardown    Close All Browsers


***Variables***
${BROWSER}                chrome
${HOMEPAGE}               https://www.tesena.com/
${HOMEPAGE_TITLE_TEXT}    Tesena
${TEST_DATA_FILE_PATH}    examples/test_data.csv
${PAGE_TITLE_FILE}        examples/page_title.txt


***Test Cases***
Homepage Title is Correct
    [Tags]    reg
    Get Test Data     ${TEST_DATA_FILE_PATH}
    Check Page Title  ${HOMEPAGE_TITLE_TEXT}
    Save Page Title  ${PAGE_TITLE_FILE}


***Keywords***
Set the Things Up
    Set Selenium Timeout    30 seconds
    Set Selenium Speed      1 seconds
    Open Browser            ${HOMEPAGE}    ${BROWSER}

Check Page Title
    [Arguments]        ${pagetitle_text}
    Title Should Be    ${pagetitle_text}


Get Test Data
    [Arguments]         ${filepath}
    ${file_content}=    Get File    ${filepath}


Save Page Title
    [Arguments]    ${filepath}
    Append To File    ${filepath}    ${HOMEPAGE_TITLE_TEXT}
