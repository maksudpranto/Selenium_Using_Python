from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Edge(
    executable_path='B:\CSE Job Preparation\SQA\Automation Testing\Drivers\edgedriver_win64\msedgedriver.exe')


class DropDown:
    def drop_down(self):
        driver.get('https://letskodeit.teachable.com/p/practice')
        driver.maximize_window()
        element = driver.find_element_by_id('carselect')
        drop = Select(element)

        # Select BY VISIBLE TEXT
        # drop.select_by_visible_text('BMW')

        # Select BY INDEX NUMBER
        # drop.select_by_index(1)

        # Select BY VALUE
        # drop.select_by_value('honda')

        # Count How Many Values in DROPDOWN
        # no_of_values = len(drop.options)
        # print("Total Options are: ", no_of_values)

        # Print all the Values of DROPDOWN
        all_options = drop.options
        for option in all_options:
            print(option.text)


obj = DropDown()
obj.drop_down()
