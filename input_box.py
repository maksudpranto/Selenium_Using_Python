from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='B:\CSE Job Preparation\SQA\Automation Testing\Drivers\chromedriver.exe')


class InputBox:
    def input_box(self):
        driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
        driver.maximize_window()
        # How to find How Many Input Fields are Present in Web Page.
        input_boxes = driver.find_elements(By.CLASS_NAME, 'text_field')
        print("Total Number of Input Boxes Is: ", len(input_boxes))

        # How to Provide Value in Text Box
        driver.find_element_by_id('RESULT_TextField-1').send_keys('Maksud Hossain')
        driver.find_element_by_id('RESULT_TextField-2').send_keys('Pranto')
        driver.find_element_by_id('RESULT_TextField-3').send_keys('01682197720')
        # How to Get the Status
        status = driver.find_element_by_id('RESULT_TextField-1').is_displayed()
        print("The Status is: ", status)


obj = InputBox()
obj.input_box()
