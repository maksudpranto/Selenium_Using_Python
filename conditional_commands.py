from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='B:\CSE Job Preparation\SQA\Automation Testing\Drivers\chromedriver.exe')


class ConditionalCommands:
    def conditional_commands(self):
        base_url = "http://demo.guru99.com/test/newtours/"
        driver.get(base_url)
        user_name = driver.find_element_by_name('userName')
        password = driver.find_element_by_name('password')

        print(user_name.is_displayed())  # Return TRUE or FALSE Based on Element Status
        print(user_name.is_enabled())  # Return TRUE or FALSE

        print(password.is_enabled())
        print(password.is_displayed())

        user_name.send_keys('mercury')
        password.send_keys('mercury')

        driver.find_element_by_name('submit').click()


obj = ConditionalCommands()
obj.conditional_commands()
