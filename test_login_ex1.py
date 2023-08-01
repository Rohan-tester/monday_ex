from selenium import webdriver
import allure
from selenium.webdriver.common.by import By


class Test_CredKart_Login():

    def test_pageTitle_001(self, setup):
        self.driver = setup
        if self.driver.title == "CredKart":
            self.driver.save_screenshot(".\\Screenshot\\test_pageTitle_001_pass.PNG")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshot\\test_pageTitle_001_fail.PNG")
            self.driver.close()
            assert False
            
            
    def test_login_new(self, setup):
        self.driver = setup
        self.driver.get("https://automation.credence.in/login")
        self.driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Credencetest@test.com")
        self.driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Credence@123")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        try:
            self.driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
            self.driver.save_screenshot(".\\Screenshot\\ss_login.png")
            print("Test Case is Pass")
            self.driver.close()
            assert True

        except:
            self.driver.save_screenshot(".\\Screenshot\\ss_login.png")
            print("Test Case is Fail")
            self.driver.close()
            assert False
