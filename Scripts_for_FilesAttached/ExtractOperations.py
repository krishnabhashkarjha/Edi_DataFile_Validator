import time
from selenium import webdriver
from Utilites import AppConstants
from AppResources import ElementLocators_For_FilesAttached as Element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException 
import pandas as pd

#from Utilites.LogFileUtility import LogFileUtility as lo

class ExtractIDs():
    def __init__(self,supplier_name):
        self.driver = webdriver.Chrome(AppConstants.BROWSER_DRIVER)
        self.driver.maximize_window()
        self.driver.get('https://commerce.spscommerce.com/auth/login/')
        self.wait = WebDriverWait(self.driver, 10)
        self.supplier_name = supplier_name

    def Login(self):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(0))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Element.Login_Email))).send_keys(Element.username)
        self.driver.find_element_by_xpath(Element.Login_Password_Xpath).send_keys(Element.password)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Element.Sign_in_button))).click()

    def Nexus(self):     
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(0))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Element.Nexus_tile))).click()
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(0))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Element.Dropdown_selector))).click()
        #self.driver.find_element_by_xpath(Element.Dropdown_selector).click()
        self.driver.find_element_by_xpath(Element.Pre_Production_selctor).click()

    def search_company(self):
        self.driver.find_element_by_xpath(Element.Network).click()
        self.driver.find_element_by_xpath(Element.relationships_tab).click()
        self.driver.find_element_by_xpath(Element.search_selcetor).click()
        self.driver.find_element_by_xpath(Element.exact_match).click()
        self.driver.find_element_by_xpath(Element.search_company).send_keys(self.supplier_name)
        self.driver.find_element_by_xpath(Element.search_button).click()
        self.driver.find_element_by_xpath(Element.toggle_compact_view).click()

    def ExtractIDs(self):
        time.sleep(4)
        self.supplier_ISA_IDs = self.driver.find_elements_by_xpath(Element.supplier_ISA_IDs_path)
        #self.supplier_ISA_IDs_list = []
        for self.supplier_ISA_ID in self.supplier_ISA_IDs:
            self.supplier_ISA_IDs_list.append(self.supplier_ISA_ID.text)
        #print(self.supplier_ISA_IDs_list)
        
        self.supplier_Group_IDs = self.driver.find_elements_by_xpath(Element.supplier_Group_IDs_path)
        #self.supplier_Group_IDs_list = []
        for self.supplier_Group_ID in self.supplier_Group_IDs:
            self.supplier_Group_IDs_list.append(self.supplier_Group_ID.text)
        #print(self.supplier_Group_IDs_list)
        
        self.retailer_ISA_IDs = self.driver.find_elements_by_xpath(Element.retailer_ISA_IDs_path)
        #self.retailer_ISA_IDs_list = []
        for self.retailer_ISA_ID in self.retailer_ISA_IDs:
            self.retailer_ISA_IDs_list.append(self.retailer_ISA_ID.text)
        #print(self.retailer_ISA_IDs_list)

        self.retailer_Group_IDs = self.driver.find_elements_by_xpath(Element.retailer_Group_IDs_path)
        #self.retailer_Group_IDs_list = []
        for self.retailer_Group_ID in self.retailer_Group_IDs:
            self.retailer_Group_IDs_list.append(self.retailer_Group_ID.text)
        #print(self.retailer_Group_IDs_list)
        
        self.retailer_names = self.driver.find_elements_by_xpath(Element.retailer_names_path)
        #self.retailer_Group_IDs_list = []
        for self.retailer_name in self.retailer_names:
            self.retailer_names_list.append(self.retailer_name.text)
        #print(self.retailer_Group_IDs_list)

    def ScrapePages(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Element.relationionship_navigation_buttons)))
        self.supplier_ISA_IDs_list = []
        self.supplier_Group_IDs_list = []
        self.retailer_ISA_IDs_list = []
        self.retailer_Group_IDs_list = []
        self.retailer_names_list = []
        try:
            self.driver.find_element_by_xpath(Element.relationship_next_button_disabled)                #single page condition
            print("-- Single Page found -- ")
            self.ExtractIDs()
        except NoSuchElementException:                                                                  #Multiple Pages condition
            print("-- Multiple Pages found --")
            while self.driver.find_element_by_xpath(Element.relationship_next_button):                  #Loop till next page button exist
                self.ExtractIDs()
                self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath(Element.relationship_next_button)) #click next page
                self.wait.until(EC.element_to_be_clickable((By.XPATH, Element.relationionship_navigation_buttons)))                      #wait till presence Pagination buttons   
                try:
                    if self.driver.find_element_by_xpath(Element.relationship_next_button_disabled):  #Check for disabled button(last page break the loop)
                        self.ExtractIDs()
                        break
                except NoSuchElementException:                                                        #not last page, continue the loop
                    continue

    def SaveIDs(self):
        self.df_IDs = pd.DataFrame(columns = ['Supplier Qual','Supplier ISA ID','Supplier Group ID','Retailer Qual','Retailer ISA ID','Retailer Group ID','Retailer Name'])
        self.df_IDs['Supplier ISA ID'] = self.supplier_ISA_IDs_list
        self.df_IDs['Supplier Group ID'] = self.supplier_Group_IDs_list
        self.df_IDs['Retailer ISA ID'] = self.retailer_ISA_IDs_list
        self.df_IDs['Retailer Group ID'] = self.retailer_Group_IDs_list
        self.df_IDs['Retailer Name'] = self.retailer_names_list
        
        self.df_IDs['Supplier Qual'] = self.df_IDs['Supplier ISA ID'].str[:2]    #Supplier - get Qualifiers(1st two characters) save to 'Sender Qual' column
        self.df_IDs['Supplier ISA ID'] = self.df_IDs['Supplier ISA ID'].str[3:]  #remove Qualifiers from ISA ID column
        self.df_IDs['Retailer Qual'] = self.df_IDs['Retailer ISA ID'].str[:2]    #Retailer - get Qualifiers(1st two characters) save to 'Sender Qual' column
        self.df_IDs['Retailer ISA ID'] = self.df_IDs['Retailer ISA ID'].str[3:]  #remove Qualifiers from ISA ID column
        print(self.df_IDs)
        self.driver.quit()
        return self.df_IDs
        
            
                                                  




'''obj = ExtractIDs()
obj.Login()
obj.Nexus()
obj.search_company()
obj.ScrapePages()
obj.SaveIDs()'''