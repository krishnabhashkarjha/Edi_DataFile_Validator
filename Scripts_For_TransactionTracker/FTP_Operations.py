from Utilites.SeleniumOperations import SeleniumOperations
# from Scripts_For_TransactionTracker.TransactionTrackerOperations2 import TransactionTrackerOperations
from AppResources import ElementLocator_For_TransactionTracker as ElementLocator
from Utilites.ExcelOperations import ExcelOperations
import time

class FTP_Operation:

    def __init__(self, lo, v_driver):
        self.lo = lo
        self.v_driver = v_driver


    def File_Uploading(self):
        SeleniumOperation = SeleniumOperations(self.v_driver, self.lo)
        SeleniumOperation.click_element_by_xpath(ElementLocator.FTP_Refresh)
        self.v_driver.get(ElementLocator.FTP_File_link)
        SeleniumOperation.click_element_by_xpath(ElementLocator.FTP_Refresh)
        self.v_driver.get(ElementLocator.FTP_inbound_edi)
        time.sleep(5)
        first_parcel = ExcelOperations.get_value(ElementLocator.Edi_Parcel_file, 1, 1)
        second_parcel = ExcelOperations.get_value(ElementLocator.Edi_Parcel_file, 2, 1)
        third_parcel = ExcelOperations.get_value(ElementLocator.Edi_Parcel_file, 3, 1)
        SeleniumOperation.send_text_by_xpath(ElementLocator.FTP_add_file,
                                             f"C:\\Users\\Krishnabhashkar.Jha\\Downloads\\{first_parcel}.dat")
        time.sleep(10)
        SeleniumOperation.send_text_by_xpath(ElementLocator.FTP_add_file,
                                             f"C:\\Users\\Krishnabhashkar.Jha\\Downloads\\{second_parcel}.dat")
        time.sleep(10)
        SeleniumOperation.send_text_by_xpath(ElementLocator.FTP_add_file,
                                             f"C:\\Users\\Krishnabhashkar.Jha\\Downloads\\{third_parcel}.dat")
        time.sleep(10)
        # SeleniumOperation.click_element_by_xpath(ElementLocator.FTP_upload)
        for i in range(3):
            time.sleep(2)
            SeleniumOperation.click_element_by_xpath(ElementLocator.FTP_Refresh)
            break

        time.sleep(3)
        SeleniumOperation.click_element_by_xpath(ElementLocator.FTP_Logout)