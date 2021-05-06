from selenium import webdriver

driver = webdriver.Chrome(executable_path='B:\CSE Job Preparation\SQA\Automation Testing\Drivers\chromedriver.exe')


class RadioAndCheckBox:
    def radio_checkbox(self):
        driver.get('https://letskodeit.teachable.com/pages/practice')
        driver.maximize_window()

        # Working with Radio Buttons
        driver.find_element_by_id('benzradio').click()

        # Working with Check Box
        driver.find_element_by_id('bmwcheck').click()


obj = RadioAndCheckBox()
obj.radio_checkbox()
