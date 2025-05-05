from __future__ import annotations
# from typing import TYPE_CHECKING, Any, Optional
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.ios import XCUITestOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Desired Capabilities
desired_caps = {
    'platformName': 'iOS',
    'platformVersion': '15.5',
    'deviceName': 'iPhone 11 Pro Max',
    'automationName': 'XCUITest',
    # 'udid': '9F1DDE89-2F0C-4053-BC3A-6A3C171D126B',
    'app': '/Users/lakshmimaduri/Library/Developer/Xcode/DerivedData/CalculatorTutorial-ghsrysfzwfrbaccpvfkbxaubilaw/Build/Products/Debug-iphonesimulator/CalculatorTutorial.app'
#     'sendKeyStrategy': "setValue",
#    'showXcodeLog': True,
#    'useNewWDA': True
}

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=XCUITestOptions().load_capabilities(desired_caps))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        # Waiting until the next process comes up
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'Number1')))
        number1 = self.driver.find_element(AppiumBy.NAME, 'Number1')
        plus_sign  = self.driver.find_element(AppiumBy.NAME, "plusSign")
        number2 = self.driver.find_element(AppiumBy.NAME, 'Number2')
        number1.send_keys("45")
        number2.send_keys("55")
        plus_sign.click()
        result_field = self.driver.find_element(AppiumBy.NAME, 'resultBox')
        self.assertEqual(str(result_field.text), "100", "Results do not match!")

if __name__ == '__main__':
    unittest.main()



# python3 -m venv . 
# source bin/activate
# python3

