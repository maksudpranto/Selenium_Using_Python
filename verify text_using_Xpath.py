from selenium import webdriver

text_to_verify = 'Selenium is a suite of tools for automating web browsers.'
drive = webdriver.Chrome('chromedriver.exe')
drive.get('https://www.selenium.dev/')
drive.find_element_by_xpath('//*[@id="navbar"]/div[1]/span').click()
drive.find_element_by_xpath('//*[@id="aboutSubnav"]/div[1]/a').click()
scrapped_text = drive.find_element_by_xpath('/html/body/section/div/p').text

if text_to_verify == scrapped_text:
    print('Text Matches')
else:
    print('Not Matches')
drive.find_element_by_xpath('//*[@id="header"]/a[1]').click()
