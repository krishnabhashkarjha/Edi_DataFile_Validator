
from Utilites.SeleniumOperations import SeleniumOperations
import time
from AppResources import ElementLocator_For_TransactionTracker as ElementLocator
from Utilites.ExcelOperations import ExcelOperations

class TransactionTrackerOperations:
    def __init__(self,driver, lo):
        self.driver = driver
        self.log = lo

    def select_customer(self, v_customer_type, v_customer_name):

        self.log.log_to_file(self,"INFO", "Executing TransactionTrackerOperations.select_customer()")
        selenium_operations_object = SeleniumOperations(self.driver, self.log)
        time.sleep(2)
        if v_customer_type == "Company":
            selenium_operations_object.send_text_by_xpath(ElementLocator.COMPANY_SEARCH_INPUTBOX, v_customer_name)
        if v_customer_type == "Trading Partner":
            selenium_operations_object.send_text_by_xpath(ElementLocator.TRADING_SEARCH_INPUTBOX, v_customer_name)
        time.sleep(2)
        count = self.driver.find_elements_by_xpath(ElementLocator.DROP_DOWN_LIST)
        for i in range(len(count)):
            if v_customer_type == "Company":
                v_customer_from_TT = selenium_operations_object.get_text_by_xpath(
                    ElementLocator.CUSTOMER_FROM_TT_FOR_COMPANY_1 + str(
                        i) + ElementLocator.CUSTOMER_FROM_TT_FOR_COMPANY_2)
            if v_customer_type == "Trading Partner":
                v_customer_from_TT = selenium_operations_object.get_text_by_xpath(
                    ElementLocator.CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_1 + str(
                        i) + ElementLocator.CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_2)
            if v_customer_name.lower() == v_customer_from_TT.lower():
                if v_customer_type == "Company":
                    selenium_operations_object.click_element_by_xpath(
                        ElementLocator.CUSTOMER_FROM_TT_FOR_COMPANY_1 + str(
                            i) + ElementLocator.CUSTOMER_FROM_TT_FOR_COMPANY_2)
                if v_customer_type == "Trading Partner":
                    selenium_operations_object.click_element_by_xpath(
                        ElementLocator.CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_1 + str(
                            i) + ElementLocator.CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_2)
                break
        time.sleep(2)

    def search_process_for_process_test_file(self,supplier,retailer,doc_type,date,mode):
        self.log.log_to_file(self,"INFO", "Executing method 'search_process' from TransactionTrackerOperations")
        self.driver.switch_to.frame(0)
        selenium_operations_object = SeleniumOperations(self.driver, self.log)
        if mode == "preprod":
            selenium_operations_object.click_element_by_xpath(ElementLocator.preprod_click)
            selenium_operations_object.click_element_by_xpath(ElementLocator.preprod)
            pass
        elif mode == "prod":
            pass
        time.sleep(2)
        self.select_customer("Company",supplier)
        time.sleep(2)
        self.select_customer("Trading Partner",retailer)
        selenium_operations_object.send_text_by_xpath(ElementLocator.START_DATE,date)
        selenium_operations_object.send_text_by_xpath(ElementLocator.DOCUMENT_TYPE,doc_type)
        selenium_operations_object.click_element_by_xpath(ElementLocator.Status_button)
        selenium_operations_object.click_element_by_xpath(ElementLocator.Accepted_click)
        selenium_operations_object.click_element_by_xpath(ElementLocator.SEARCH_BTN)
        time.sleep(5)

    def get_parcel(self,rows):
        row = int(rows)
        selenium_operations_object = SeleniumOperations(self.driver, self.log)
        file_broker = selenium_operations_object.get_text_by_xpath(ElementLocator.file_broker_xpath);print(file_broker)
        ExcelOperations.set_value_to_cell(ElementLocator.Edi_Parcel_file,row,1,file_broker)
        selenium_operations_object.click_element_by_xpath(f'//*[@id="parcel-{str(file_broker)}"]/div/div/div[2]/div/a/div/div')
        time.sleep(3)
        selenium_operations_object.click_element_by_xpath(ElementLocator.Download_xpath)
        selenium_operations_object.click_element_by_xpath(ElementLocator.BackToTransaction)
        selenium_operations_object.click_element_by_xpath(ElementLocator.BackToSearch)

    def Download_processFile(self):
        selenium_operations_object = SeleniumOperations(self.driver, self.log)
        # tt_first_parcel = selenium_operations_object.get_text_by_xpath(ElementLocator.parcel_1_click)
        # tt_second_parcel = selenium_operations_object.get_text_by_xpath(ElementLocator.parcel_2_click)
        # tt_third_parcel = selenium_operations_object.get_text_by_xpath(ElementLocator.parcel_3_click)
        selenium_operations_object.click_element_by_xpath(ElementLocator.parcel_1_click)
        self.get_parcel("1")
        # selenium_operations_object.send_text_by_xpath(ElementLocator.search_parcel,tt_second_parcel)
        selenium_operations_object.click_element_by_xpath(ElementLocator.parcel_2_click)
        self.get_parcel("2")
        selenium_operations_object.click_element_by_xpath(ElementLocator.parcel_3_click)
        self.get_parcel("3")


