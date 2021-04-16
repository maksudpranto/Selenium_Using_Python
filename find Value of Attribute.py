from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')


class find_value:
    def value(self):
        base_url = 'https://letskodeit.teachable.com/p/practice'
        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.get(base_url)

        element = driver.find_element_by_id('bmwradio')
        result = element.get_attribute('type')

        print('Value of the Attribute is : ' + result)
        time.sleep(1)
        driver.quit()


obj = find_value()
obj.value()
