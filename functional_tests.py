from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
# from django import test
import time
import sqlite3
from pprint import pprint

sqlite_file = 'db.sqlite3'    # name of the sqlite database file
table_name = 'accounts_tuser'   # name of the table to be queried
column_name = 'username'

class AccountSetupTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Firefox()
        conn = sqlite3.connect(sqlite_file)
        conn.row_factory = sqlite3.Row
        self.c = conn.cursor()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
#
#     def test_can_load_activation_page_after_registration(self):
#         self.browser.get('http://localhost:8000/register')
#
#         username = self.browser.find_element_by_id('id_username')
#         username.send_keys('test3')
#
#         phone = self.browser.find_element_by_id('id_phone_number')
#         phone.send_keys('12345678903')
#
#         pass1 = self.browser.find_element_by_id('id_password1')
#         pass1.send_keys('test3')
#
#         pass2 = self.browser.find_element_by_id('id_password2')
#         pass2.send_keys('test3')
#         pass2.send_keys(Keys.ENTER)
#
#         time.sleep(10)
#
#         self.assertIn('Activation', self.browser.title)
#         # self.fail('Finish the test!')

    # def test_user_can_register(self):
    #     self.browser.get('http://localhost:8000/register')
    #
    #     username = self.browser.find_element_by_id('id_username')
    #     username.send_keys('testuser')
    #
    #     phone = self.browser.find_element_by_id('id_phone_number')
    #     phone.send_keys('0779222337')
    #     # phone.send_keys('0706471650')
    #
    #     pass1 = self.browser.find_element_by_id('id_password1')
    #     pass1.send_keys('testuser')
    #
    #     pass2 = self.browser.find_element_by_id('id_password2')
    #     pass2.send_keys('testuser')
    #     pass2.send_keys(Keys.ENTER)
    #
    #     time.sleep(10)
    #     self.assertIn('Activation', self.browser.title)
    #     verification = self.browser.find_element_by_id('id_verification_code')
    #     self.c.execute('SELECT * FROM {tn} WHERE {cn}="{usr}"'.\
    #             format(tn=table_name, cn=column_name,usr="testuser"))
    #     v_code = self.c.fetchone()['verification_code']
    #     verification.send_keys(v_code)
    #     verification.send_keys(Keys.ENTER)
    #
    #     time.sleep(10)
    #     self.assertIn('TestUser',self.browser.find_element_by_tag_name('h1'))
    #     # self.fail('Finish the test!')

#
    # def test_inactive_user_login_is_redirected_to_activation_page(self):
    #     self.browser.get('http://localhost:8000/register')
    #
    #     username = self.browser.find_element_by_id('id_username')
    #     username.send_keys('testuser')
    #
    #     phone = self.browser.find_element_by_id('id_phone_number')
    #     phone.send_keys('0779222337')
    #     # phone.send_keys('0706471650')
    #
    #     pass1 = self.browser.find_element_by_id('id_password1')
    #     pass1.send_keys('testuser')
    #
    #     pass2 = self.browser.find_element_by_id('id_password2')
    #     pass2.send_keys('testuser')
    #     pass2.send_keys(Keys.ENTER)
    #
    #     time.sleep(5)
    #     self.browser.get('http://localhost:8000/login')
    #     username = self.browser.find_element_by_id('id_username')
    #     username.send_keys('testuser')
    #
    #     password = self.browser.find_element_by_id('id_password')
    #     password.send_keys('testuser')
    #     password.send_keys(Keys.ENTER)
    #
    #     time.sleep(5)
    #     self.assertIn('Activation', self.browser.title)

    # def test_inactive_user_can_activate_and_login(self):
    #     self.browser.get('http://localhost:8000/register')
    #
    #     username = self.browser.find_element_by_id('id_username')
    #     username.send_keys('testuser')
    #
    #     phone = self.browser.find_element_by_id('id_phone_number')
    #     phone.send_keys('0779222337')
    #     # phone.send_keys('0706471650')
    #
    #     pass1 = self.browser.find_element_by_id('id_password1')
    #     pass1.send_keys('testuser')
    #
    #     pass2 = self.browser.find_element_by_id('id_password2')
    #     pass2.send_keys('testuser')
    #     pass2.send_keys(Keys.ENTER)
    #
    #     time.sleep(5)
    #     self.browser.get('http://localhost:8000/login')
    #     username = self.browser.find_element_by_id('id_username')
    #     username.send_keys('testuser')
    #
    #     password = self.browser.find_element_by_id('id_password')
    #     password.send_keys('testuser')
    #     password.send_keys(Keys.ENTER)
    #
    #     time.sleep(5)
    #     self.assertIn('Activation', self.browser.title)
    #     verification = self.browser.find_element_by_id('id_verification_code')
    #     self.c.execute('SELECT * FROM {tn} WHERE {cn}="{usr}"'.\
    #             format(tn=table_name, cn=column_name,usr="testuser"))
    #     v_code = self.c.fetchone()['verification_code']
    #     verification.send_keys(v_code)
    #     verification.send_keys(Keys.ENTER)
    #
    #     time.sleep(5)
    #     self.assertIn('Testuser',self.browser.find_element_by_tag_name('h1').text)

    # def test_inactive_user_can_change_number(self):
    #     self.browser.get('http://localhost:8000/register')
    #
    #     username = self.browser.find_element_by_id('id_username')
    #     username.send_keys('testuser')
    #
    #     phone = self.browser.find_element_by_id('id_phone_number')
    #     phone.send_keys('0779222337')
    #     # phone.send_keys('0706471650')
    #
    #     pass1 = self.browser.find_element_by_id('id_password1')
    #     pass1.send_keys('testuser')
    #
    #     pass2 = self.browser.find_element_by_id('id_password2')
    #     pass2.send_keys('testuser')
    #     pass2.send_keys(Keys.ENTER)
    #
    #     time.sleep(5)
    #     self.assertIn('Activation', self.browser.title)
    #     change_number_link = self.browser.find_element_by_tag_name('a')
    #     change_number_link.click()
    #
    #     time.sleep(5)
    #     self.assertIn('Change number', self.browser.title)
    #     phone = self.browser.find_element_by_id('id_phone_number')
    #     phone.send_keys('0706471650')
    #     phone.send_keys(Keys.ENTER)
    #
    #     time.sleep(5)
    #     self.assertIn('Activation', self.browser.title)
    #     verification = self.browser.find_element_by_id('id_verification_code')
    #     self.c.execute('SELECT * FROM {tn} WHERE {cn}="{usr}"'.\
    #             format(tn=table_name, cn=column_name,usr="testuser"))
    #     v_code = self.c.fetchone()['verification_code']
    #     verification.send_keys(v_code)
    #     verification.send_keys(Keys.ENTER)
    #
    #     time.sleep(5)
    #     self.assertIn('Testuser',self.browser.find_element_by_tag_name('h1').text)

if __name__ == '__main__':
    unittest.main()
