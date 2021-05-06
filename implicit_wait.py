from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='B:\CSE Job Preparation\SQA\Automation Testing\Drivers\chromedriver.exe')


class ImplicitWait:
    def implicit_wait(self):
        base_url = 'http://demo.guru99.com/test/newtours/'
        driver.get(base_url)
        # Wait for Some Time Here
        driver.implicitly_wait(10)

        assert "Welcome: Mercury Tours" in driver.title
        driver.find_element_by_name('userName').send_keys('mercury')
        driver.find_element_by_name('password').send_keys('mercury')
        driver.find_element_by_name('submit').click()


obj = ImplicitWait()
obj.implicit_wait()
