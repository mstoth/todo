from selenium import webdriver
import os
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):
        if os.name=='nt':
            # You might need to put the path to chromedriver.exe in
            # the following line as an argument to Chrome()
            # like webdriver.Chrome("C:\Program Files\Chrome") for instance

            self.browser = webdriver.Chrome()
        else:
            self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)  
        self.fail('Finish the test!')  

        # She is invited to enter a to-do item straight away

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  

