import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="B:\CSE Job Preparation\SQA\Automation Testing\Drivers\chromedriver.exe ")


class NavigationCommands:
    def navigation_commands(self):
        driver.get("http://demo.guru99.com/test/newtours/")
        first_title = driver.title
        print(first_title)
        driver.get("https://www.pavantestingtools.com/")
        second_title = driver.title
        time.sleep(5)
        print(second_title)
        driver.back()
        time.sleep(5)
        print("After Backing the Title is : ", first_title)
        driver.forward()
        time.sleep(5)
        print("After forwarding the Title is: ", second_title)
        driver.close()


obj = NavigationCommands()
obj.navigation_commands()
