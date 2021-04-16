from selenium import webdriver


class find_by_ID():
    def test(self):
        base_url = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get(base_url)
        elementByID = driver.find_element_by_id('name')
        if elementByID is not None:
            print("We Found an Element")
        elementByName = driver.find_element_by_name('show-hide')

        if elementByName is not None:
            print('We found an element by Name')


test_object = find_by_ID()
test_object.test()
