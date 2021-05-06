from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='B:\CSE Job Preparation\SQA\Automation Testing\Drivers\chromedriver.exe')


class MouseAction:
    def mouse_actions(self):
        driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials')
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="txtUsername"]').send_keys('Admin')
        driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys('admin123')
        driver.find_element_by_id('btnLogin').click()

        admin = driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
        usermgt = driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
        users = driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')

        action = ActionChains(driver)
        action.move_to_element(admin).move_to_element(usermgt).move_to_element(users).click().perform()

    def double_click(self):
        driver.get('http://testautomationpractice.blogspot.com/')
        driver.maximize_window()
        element = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')
        double_click = ActionChains(driver)
        double_click.double_click(element).perform()

    def right_click(self):
        driver.get('https://swisnl.github.io/jQuery-contextMenu/demo/input.html')
        right_click_btn = driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')
        rightBtn = ActionChains(driver)
        rightBtn.context_click(right_click_btn).perform()

    def drag_drop(self):
        driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
        driver.maximize_window()
        source_element = driver.find_element_by_xpath('//*[@id="box6"]')
        target_element = driver.find_element_by_xpath('//*[@id="box106"]')
        drag_action = ActionChains(driver)
        drag_action.drag_and_drop(source_element, target_element).perform()


obj = MouseAction()
# obj.mouse_actions()
# obj.double_click()
# obj.right_click()
obj.drag_drop()
