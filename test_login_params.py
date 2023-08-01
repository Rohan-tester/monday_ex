from selenium.webdriver.common.by import By
import allure

class Test_login_page:
    def test_new_page(self, setup, getdata):
        self.driver = setup
        self.driver.find_element("https://automation.credence.in/login")
        self.driver.find_element(By.XPATH,"//input[@id='email']").send_keys(getdata[0])
        self.driver.find_element(By.XPATH,"//input[@id='password']").send_keys(getdata[1])
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()

        try:
            self.driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
            print("Test Case is Pass")
            self.driver.save_screenshot(".\\Screenshot\\"+getdata[0]+"_"+getdata[1]+"_"+"login.png")
            self.driver.close()
            assert True

        except:
            self.driver.save_screenshot(".\\Screenshot\\"+getdata[0]+"_"+getdata[1]+"_"+"login.png")
            self.driver.close()
            assert False
