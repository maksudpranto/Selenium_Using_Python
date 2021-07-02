from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def full_page_screenshot():
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("https://demo.opencart.com/index.php?route=product/category&path=20")
    driver.implicitly_wait(10)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
    driver.set_window_size(S('Width'), S('Height'))
    driver.find_element_by_tag_name('body').screenshot(
        "B:\\SQA Preparation\\SQA - BITM\\Automation Test\\Screenshot\\full_page.png")


def visible_part_screenshot():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://demo.opencart.com")
    driver.implicitly_wait(10)
    driver.save_screenshot("B:\\SQA Preparation\\SQA - BITM\\Automation Test\\Screenshot\\visible_part.png")


if __name__ == "__main__":
    full_page_screenshot()
    visible_part_screenshot()

print("""
Successfully Taken All Screenshots !! 
""")
