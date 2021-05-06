from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path='B:\CSE Job Preparation\SQA\Automation Testing\Drivers\chromedriver.exe')
# driver = webdriver.Firefox(executable_path='B:\CSE Job Preparation\SQA\Automation Testing\Drivers\geckodriver-v0.29.1-win64\geckodriver.exe')
driver = webdriver.Edge("B:\CSE Job Preparation\SQA\Automation Testing\Drivers\edgedriver_win64\msedgedriver.exe")


class CheckTitle:
    def title(self):
        base_url = "http://demo.guru99.com/test/newtours/"
        driver.get(base_url)
        title_is = driver.title
        url_is = driver.current_url
        # html_code_is = driver.page_source
        print("The Title Is: ", title_is)
        print("The Current URL Is: ", url_is)
        # print("The HTML Code Is", html_code_is)
        driver.maximize_window()
        driver.close()


obj = CheckTitle()
obj.title()
