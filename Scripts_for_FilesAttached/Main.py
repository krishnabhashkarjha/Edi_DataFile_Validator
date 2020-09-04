# -*- coding: utf-8 -*-

import pandas as pd
# from ExtractOperations import ExtractIDs
from Scripts_for_FilesAttached.ExtractOperations import ExtractIDs
from AppResources import ElementLocators_For_FilesAttached as Element
# from FileOperations import File_Operations
from Scripts_for_FilesAttached.FileOperations import File_Operations

class Main_Executor():
    def __init__(self):
        self.df_InputFile = pd.read_excel(Element.INPUT_FILE_PATH, sheet_name='ParcelsAttached')

    
    def Execute_ExtractIDs(self):
        self.supplier_name = self.df_InputFile.iloc[0][0]               #get supplier name from input file
        self.retailer_name = self.df_InputFile.iloc[0][1]
        extract = ExtractIDs(self.supplier_name)
        extract.Login()
        extract.Nexus()
        extract.search_company()
        extract.ScrapePages()
        self.df_IDs = extract.SaveIDs()
        print(self.df_IDs)
        
    def Execute_FileSelection(self):
        validateFile = File_Operations(self.df_IDs,self.retailer_name)
        validateFile.files_selector()
        validateFile.remove_tilt()
        validateFile.Setup_IDs_Validation()
        validateFile.ST_and_GE_Validation()
        validateFile.ST_and_SE_Validation()