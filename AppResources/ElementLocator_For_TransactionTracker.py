

# Common Constants
INPUT_FILE_PATH = "../AppResources/InputFile_For_TransactionTracker.xlsx"
Edi_Parcel_file = "../AppResources/Edi_parcel_file.xlsx"
Login_Email_Xpath = "//input[@type='email' and @name = 'username']"
Login_Password_Xpath = "//input[@type='password' and @name = 'password']"
Login_Button = "//button[@test='login-button']"

# Login Credentials

# FTP
FTP_USERNAME_Xpath = ".//input[@id='username']"
FTP_PASSWORD_Xpath = ".//input[@id='password']"
FTP_LOGIN_BUTTON_Xpath = ".//span[@id='LoginButtonText']"
FTP_PREPROD_LINK= "https://commshare.spspreprod.in/#/ftp/inbound_edi/"
FTP_File_link = 'https://commshare.spspreprod.in/ftp/'
FTP_Refresh = ".//*[contains(@title,'Refresh')]"
FTP_inbound_edi = "https://commshare.spspreprod.in/ftp/inbound_edi/"
FTP_add_file = ".//*[contains(@id,'browseFileButtonPanel')]//input[@type='file']"
FTP_Logout = ".//*[contains(@loctext,'Logout')]"
FTP_upload = ".//button[@id='startUpload' and @type='button']"
upload = '//*[@id="queue"]/div/div/span[4]/span[4]/span'
# TT
preprod_click = "/html/body/app-reporting/div/div/nav-bar/div/nav/div/ul/sps-select/div"
preprod = '//*[@id="ui-select-choices-row-2-1"]/div/div'
Status_button = '//*[@id="advanced_search_dropdown"]/div[1]/div/div[1]/div[1]/div[3]/div/sps-select/div'
Accepted_click = ".//*[contains(@id,'ui-select-choices-row-5-1')][1]"
parcel_1_click = '//*[@id="parentTablesContainer"]/div[1]/table/tbody/tr[1]/td[2]/a'
parcel_2_click = '//*[@id="parentTablesContainer"]/div[1]/table/tbody/tr[2]/td[2]/a'
parcel_3_click = '//*[@id="parentTablesContainer"]/div[1]/table/tbody/tr[3]/td[2]/a'
search_parcel = ".//*[contains(@id,'advanced_search_by_input')]"
accepted1 = '//*[@id="parentTablesContainer"]/div[2]/table/tbody/tr[1]/td[1]/span'
accepted2 = '//*[@id="parentTablesContainer"]/div[2]/table/tbody/tr[2]/td[1]/span'
accepted3 = '//*[@id="parentTablesContainer"]/div[2]/table/tbody/tr[3]/td[1]/span'
file_broker_xpath = '/html/body/app-reporting/div/div/div/div/div[2]/div[2]/section/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/span[2]'
Download_xpath = ".//*[contains(@title,'Download')]"
BackToTransaction = '/html/body/app-reporting/div/div/div/div/div/header/a'
BackToSearch = '/html/body/app-reporting/div/div/div/div/div[2]/div[1]/div[1]/a'

# Common Locator
# XPath for Supplier Link
Company_Select_Link = '//*[@id="table1:10:commandLink2"]'

TRANSACTION_TRACKER_PROD_LINK = 'https://commerce.spscommerce.com/transaction-tracker/prod/transactions/'

xpath=".//*[@id='ui-select-choices-row-2-"
PARCEL_COUNT="html/body/app-reporting/div/div/div/div/div/section/sps-search-results-bar/div/div/div/div/span/span[3]"
VIEW="html/body/app-reporting/div/div/div/div/div/section/div[3]/div[1]/span/sps-select/div/a"
# SELECT_100=".//*[contains(text(),'100')]"
SELECT_100=".//*[@id='ui-select-choices-row-11-3']/div/div"
NEXT_SEARCH_BTN="html/body/app-reporting/div/div/div/div/div/section/div[3]/form/div/button[2]"

DROP_DOWN_LIST=".//*[contains(@id,'ui-select-choices-row-')]"
CUSTOMER_FROM_TT_FOR_COMPANY_1=".//*[@id='ui-select-choices-row-1-"
CUSTOMER_FROM_TT_FOR_COMPANY_2="']/div/div"
CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_1=".//*[@id='ui-select-choices-row-2-"
CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_2="']/div/div"

#def get_CM_parcels(self,input_sheet,row)

PARCEL_ID_1=".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr["
PARCEL_ID_2="]/td[2]"
STATUS_1=".//*[@id='parentTablesContainer']/div[2]/table/tbody/tr["
STATUS_2="]/td[1]"
DOCUMENT_ID_1=".//*[@id='parentTablesContainer']/div[2]/table/tbody/tr["
DOCUMENT_ID_2="]/td[5]"


LAST_PARCEL_ID=".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[1]/td[2]"

#process test files

FIRST_PARCEL_ID=".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[1]/td[2]/a"
PARCEL_FIRST_STAGE="//h4[contains(text(),'Transformations ')]/following::i[4]"
PARCEL_FIRST_STAGE_ID="//h4[contains(text(),'Transformations ')]/following::span[3]"
DOWNLOAD_LOGO_BUTTON=".//*[@id='parcels_drop']/following::i"

CLIENT_SECRET_JSON_FILE_PATH= '../Applications/Workflows/ProcessTestFiles/AppResources/Process Test File-7df61375a764.json'

PARCEL_ID_SEARCH_BOX=".//*[@id='advanced_search_by_input']"

TRANSAFORMATION="//aside[text()='Transformations']/following::a[@title='View'][1]/div/div"
TRANSAFORMATION1="html/body/div[1]/section/section/div/div/section/div/div[3]/div[1]/div/div[1]/div/div/div/a/i"


#FTP_PREPROD
FTP_USERNAME= ".//input[@id='username']"
FTP_PASSWORD= ".//input[@id='password']"
FTP_LOGIN_BUTTON= ".//span[@id='LoginButtonText']"
FTP_ADD_FILES= ".//*[@id='browseFileButtonPanel']"
FTP_ADD_FILES_BTN= ".//*[@id='browseFileButtonPanel']"
FTP_UPLOAD_FILES_BTN= ".//*[@id='startUpload']"

TRANSACTION_TRACKER_PREPROD_LINK= 'https://commerce.spscommerce.com/transaction-tracker/preprod/transactions/'
#T ransaction Tracker UI xpath
COMPANY_SEARCH_INPUTBOX=".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[2]/div[1]/div/companies-chosen-select/div/ul/li/input"
TRADING_SEARCH_INPUTBOX= ".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[2]/div[3]/div/trading-partner-chosen-select/div/ul/li/input"
START_DATE=".//*[@id='advanced_search_dropdown']/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/input"
END_DATE=".//*[@id='advanced_search_dropdown']/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div/div[1]/input"
DOCUMENT_TYPE=".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[3]/div[3]/div/input"
SERVICE=".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[3]/div[1]/div/sps-select/div/a/span[2]/span"
SEARCH_BTN="//button[@type='button']/following::button[@type='submit'][2]"
# SEARCH_BTN=".//*[@id='advanced_search_dropdown']/div[2]/div/div/button[2]"
DC4ROUTER=".//*[contains(text(),'DC4Router')]"
STATUS= ".//*[@id='advanced_search_dropdown']/div[1]/div/div[1]/div[1]/div[3]/div/sps-select/div/a/span[2]/span"
ACCEPTED= ".//*[@id='ui-select-choices-row-5-1']/div/div"
LAST24HRS= ".//*[@id='advanced_search_dropdown']/div[1]/div/div[2]/div/div/div/div/div[1]/div/div/button[1]"

PARCEL_ID_SEARCH_BOX=".//*[@id='advanced_search_by_input']"
xpath=".//*[@id='ui-select-choices-row-2-"
PARCEL_COUNT="html/body/app-reporting/div/div/div/div/div/section/sps-search-results-bar/div/div/div/div/span/span[3]"
VIEW="html/body/app-reporting/div/div/div/div/div/section/div[3]/div[1]/span/sps-select/div/a"
# SELECT_100=".//*[contains(text(),'100')]"
SELECT_100=".//*[@id='ui-select-choices-row-11-3']/div/div"
NEXT_SEARCH_BTN="html/body/app-reporting/div/div/div/div/div/section/div[3]/form/div/button[2]"
DROP_DOWN_LIST=".//*[contains(@id,'ui-select-choices-row-')]"
CUSTOMER_FROM_TT_FOR_COMPANY_1=".//*[@id='ui-select-choices-row-0-"
CUSTOMER_FROM_TT_FOR_COMPANY_2="']/div/div"
CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_1=".//*[@id='ui-select-choices-row-1-"
CUSTOMER_FROM_TT_FOR_TRADING_PARTNER_2="']/div/div"
#def get_CM_parcels(self,input_sheet,row)
PARCEL_ID_1=".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr["
PARCEL_ID_2="]/td[2]"
STATUS_1=".//*[@id='parentTablesContainer']/div[2]/table/tbody/tr["
STATUS_2="]/td[1]"
DOCUMENT_ID_1=".//*[@id='parentTablesContainer']/div[2]/table/tbody/tr["
DOCUMENT_ID_2="]/td[5]"
LAST_PARCEL_ID=".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[1]/td[2]"
#process test files

FIRST_PARCEL_ID=".//*[@id='parentTablesContainer']/div[1]/table/tbody/tr[1]/td[2]/a"
PARCEL_FIRST_STAGE="//h4[contains(text(),'Transformations ')]/following::i[4]"
PARCEL_FIRST_STAGE_ID="//h4[contains(text(),'Transformations ')]/following::span[3]"
DOWNLOAD_LOGO_BUTTON=".//*[contains(@title,'Download')]"
PROCESS_PATH='D:\processtestfiles.txt'

#with open(path) as f

TRANSAFORMATION="//aside[text()='Transformations']/following::a[@title='View'][1]/div/div"
TRANSAFORMATION1="html/body/div[1]/section/section/div/div/section/div/div[3]/div[1]/div/div[1]/div/div/div/a/i"

# Document type
PO_File = 850

TRANSACTION_TRACKER_PROD_LINK = 'https://commerce.spscommerce.com/transaction-tracker/prod/transactions/'
TRANSACTION_TRACKER_PREPROD_LINK= 'https://commerce.spscommerce.com/transaction-tracker/preprod/transactions/'

#process test files
FIRST_FIVE_PARCELS_FILE_PATH = r"C:\Users\Krishnabhashkar.Jha\Desktop\Edi_Data_Validator\AppResources\parcelIDsforSearch.txt"

#process test files

INPUT_PARCELS_FILE_PATH = r"C:\Users\Krishnabhashkar.Jha\Desktop\Edi_Data_Validator\AppResources\inputparcellist.txt"

# Parcel ID Paths
path_1 = '//*[@id="parentTablesContainer"]/div[1]/table/tbody/tr['
path_2 = ']/td[2]/a'

