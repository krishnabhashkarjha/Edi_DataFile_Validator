import time
from Utilites import AppConstants
from Scripts_For_TransactionTracker.TransactionTrackerOperations2 import TransactionTrackerOperations
from Utilites.SeleniumOperations import SeleniumOperations
from AppResources import ElementLocator_For_TransactionTracker as ElementLocator

class Po_from_TT:

    def __init__(self,lo,v_driver):
        self.lo = lo
        self.v_driver = v_driver

    def login(self,v_tool):
        if v_tool == "DC4 Prod":
            Link = AppConstants.DC4_PROD_LINK
        elif v_tool == "DC4 PreProd":
            Link = AppConstants.DC4_PREPROD_LINK
        elif v_tool == "Launchpad":
            Link = AppConstants.LAUNCHPAD_LINK
        elif v_tool == "FTP Pre-prod":
            Link = AppConstants.FTP_PREPROD_LINK
        else:
            self.lo.log_to_file("ERROR", "Error in Login.login(). Invalid Link")
            return False
        self.v_driver.get(Link)
        SeleniumOperation = SeleniumOperations(self.v_driver, self.lo)
        if v_tool == "Launchpad":
            print("IN login method for Launchpad")
            time.sleep(7)
            self.v_driver.switch_to.frame(0)
            SeleniumOperation.send_text_by_xpath(ElementLocator.Login_Email_Xpath,ElementLocator.Launchpad_username)
            SeleniumOperation.send_text_by_xpath(ElementLocator.Login_Password_Xpath,ElementLocator.Launchpad_password)
            SeleniumOperation.click_element_by_xpath(ElementLocator.Login_Button)
        elif v_tool == "FTP Pre-prod":
            print("IN login method for FTP")
            self.v_driver.get(ElementLocator.FTP_PREPROD_LINK)
            SeleniumOperation.send_text_by_xpath(ElementLocator.FTP_USERNAME_Xpath, ElementLocator.FTP_pre_prod_username)
            SeleniumOperation.send_text_by_xpath(ElementLocator.FTP_PASSWORD_Xpath, ElementLocator.FTP_pre_prod_password)
            SeleniumOperation.click_element_by_xpath(ElementLocator.FTP_LOGIN_BUTTON_Xpath)

    def TT_Operations(self,v_supplier,v_retailer,v_doc_type,v_date):
        print("IN TT Operations")
        time.sleep(10)
        self.v_driver.get("https://commerce.spscommerce.com/transaction-tracker/prod/transactions/")
        time.sleep(5)
        tt_operations = TransactionTrackerOperations(self.v_driver, self.lo)
        tt_operations.search_process_for_process_test_file(v_supplier, v_retailer, v_doc_type, v_date,"prod")
        tt_operations.Download_processFile()

    def call_check_accepted(self,v_supplier,v_retailer,v_doc_type,v_date):
        print("In Call check accepted")
        self.v_driver.execute_script("window.open('about:blank', 'tab3');")
        self.v_driver.switch_to.window("tab3")
        time.sleep(3)
        self.v_driver.get("https://commerce.spscommerce.com/transaction-tracker/prod/transactions/")
        time.sleep(8)
        tt_operations = TransactionTrackerOperations(self.v_driver, self.lo)
        tt_operations.search_process_for_process_test_file(v_supplier, v_retailer, v_doc_type, v_date, "preprod")
        time.sleep(5)
        SeleniumOperation = SeleniumOperations(self.v_driver, self.lo)
        # self.v_driver.switch_to.frame(1)
        time.sleep(2)
        a = SeleniumOperation.get_text_by_xpath(ElementLocator.accepted1)
        if a == "Accepted":
            print("First Parcel is Accepted")
            pass
        b = SeleniumOperation.get_text_by_xpath(ElementLocator.accepted2)
        if b == "Accepted":
            print("Second Parcel is Accepted")
            pass
        c = SeleniumOperation.get_text_by_xpath(ElementLocator.accepted3)
        if a == "Accepted":
            print("Third Parcel is Accepted")
            pass