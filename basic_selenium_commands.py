import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="B:\CSE Job Preparation\SQA\Automation Testing\Drivers\chromedriver.exe")


class BasicCommands:
    def basics(self):
        base_url = "http://demo.automationtesting.in/Windows.html"
        driver.get(base_url)
        check_title = driver.title
        check_url = driver.current_url
        print("Title of the Page is: ", check_title)
        print("URL of the Page is: ", check_url)
        driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
        time.sleep(5)

        driver.close()  # Close a single Tab
        driver.quit()  # Closes all the Windows / Tabs


obj = BasicCommands()
obj.basics()
