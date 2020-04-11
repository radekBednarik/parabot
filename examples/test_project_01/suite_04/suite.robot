**Settings***
Library           SeleniumLibrary
Suite Setup       Set the Things Up        
Suite Teardown    Close All Browsers


***Variables***
${BROWSER}                chrome
${HOMEPAGE}               https://www.tesena.com/
${HOMEPAGE_TITLE_TEXT}    Tesena


***Test Cases***
Homepage Title is Correct
    Check Page Title  ${HOMEPAGE_TITLE_TEXT}


***Keywords***
Set the Things Up
    Set Selenium Timeout    30 seconds
    Set Selenium Speed      1 seconds
    Open Browser            ${HOMEPAGE}    ${BROWSER}

Check Page Title
    [Arguments]        ${pagetitle_text}
    Title Should Be    ${pagetitle_text}
