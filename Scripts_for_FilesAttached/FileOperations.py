import tkinter as tk
from tkinter import filedialog
from Utilites.LogFileUtility import LogFileUtility as lo
import pandas as pd


class File_Operations():
    def __init__(self, df_IDs, retailer_name):
        self.retailer_name = retailer_name
        self.df_IDs = df_IDs
        self.df_IDs = self.df_IDs.loc[(self.df_IDs['Retailer Name'] == self.retailer_name)]
        # self.df_IDs.loc[(test_df_IDs['Retailer Name'] == self.retailer_name)

    def files_selector(self):
        root = tk.Tk()

        root.withdraw()
        root.attributes("-topmost", True)
        self.file_paths = filedialog.askopenfilenames(parent=root, initialdir="C:/Users/Krishnabhashkar.Jha/Downloads")
        print(self.file_paths)
        self.no_of_files = len(self.file_paths)
        print(self.no_of_files, " number of files are selected")

    def Setup_IDs_Validation(self):
        i = 1
        for self.file_path in self.file_paths:
            # print(df_IDs.head())
            test_df_IDs = self.df_IDs
            test1 = open(self.file_path)
            test_data = test1.readlines()
            delimeter = test_data[0][3]
            # self.delimeter = str(test_data[0].split('*')[6])

            test_Retailer_Qual = str(test_data[0].split(delimeter)[5])
            test_ISA_Retailer_field = str(test_data[0].split(delimeter)[6]).strip()
            test_GS_Retailer_field = str(test_data[1].split(delimeter)[2]).strip()

            test_Supplier_Qual = str(test_data[0].split(delimeter)[7])
            test_ISA_Supplier_field = str(test_data[0].split(delimeter)[8]).strip()
            test_GS_Supplier_field = str(test_data[1].split(delimeter)[3]).strip()

            test_df_IDs = test_df_IDs.loc[(test_df_IDs['Retailer ISA ID'] == test_ISA_Retailer_field) & (
                        test_df_IDs['Retailer Group ID'] == test_GS_Retailer_field) & (
                                                      test_df_IDs['Retailer Qual'] == test_Retailer_Qual)]
            print('File', i, 'IDs Validated')
            if test_df_IDs.empty:
                print('       Retailer The ISA ids did not match')

            test_df_IDs = test_df_IDs.loc[(test_df_IDs['Supplier ISA ID'] == test_ISA_Supplier_field) & (
                        test_df_IDs['Supplier Group ID'] == test_GS_Supplier_field) & (
                                                      test_df_IDs['Supplier Qual'] == test_Supplier_Qual)]
            if test_df_IDs.empty:
                print('       Supplier The ISA ids did not match')
            i = i + 1
            print("______________________________________________________________")


    def ST_and_GE_Validation(self):
        lo.log_to_file(self, "INFO", " Executing Edi_validator.ST_and_SE_validation()")
        k = 1
        for self.file_path in self.file_paths:
            print('File', k, 'IDs Validated')
            with open(self.file_path, 'r') as fi:
                i = 0
                for line in fi:
                    # print(line)
                    if line.startswith('ST'):
                        # print(line)  # output: ST*850*113986
                        i += 1
                print(f"Number of Time ST is present : {i}")
                ST_Count = str(i)
            fi.close()
            with open(self.file_path, 'r') as fii:
                j = 1
                for line in fii:
                    if line.startswith('GE'):
                        # print(line)
                        GE_line = line
                        break
                    j += 1
                # print("GE is present at line Number :", j)
            fii.close()
            GE_count = str(GE_line.split('*')[1])
            print(f"GE side number is : {GE_count}")
            if ST_Count == GE_count:
                print("GE count is equal to count of ST segment present in the file.")
            else:
                print("Something went Wrong")
            k += 1
            print("______________________________________________________________")

    def ST_and_SE_Validation(self):
        lo.log_to_file(self, "INFO", " Executing Edi_validator.ST_and_SE_validation()")
        k = 1
        for self.file_path in self.file_paths:
            print('File', k, 'IDs Validated')
            file = open(self.file_path, 'r')
            linelist = file.readlines()
            file.close()
            if len(linelist) <= 2:
                with open(self.file_path, 'r') as f:
                    for line in f.readlines():
                        first_line = line.split("GS")[0]
                        # print(first_line)
                        delemitor = first_line.split("ISA")[1][0:1]
            else:
                f = open(self.file_path, 'r')
                first_line = f.readline()
                delemitor = first_line.split("ISA")[1][0:1]
            with open(self.file_path, 'r') as fii:
                j = 1
                for line in fii:
                    # print(line)
                    if line.startswith('SE'):
                        # print(line)  # output: SE*39*113986
                        for ch in [delemitor]:
                            if ch in line:
                                y = line.split(delemitor)
                        SE_at_second_position = y[1]
                        # print(SE_at_second_position)
                        break
                    j += 1
                # print("SE is present at line no : ", j)
            fii.close()
            line_no_at_which_SE_is_present = j
            no_of_lines_between_ST_and_SE = line_no_at_which_SE_is_present - 2
            print(f"Number of Line between ST and SE is : {str(no_of_lines_between_ST_and_SE)}")  # output 39
            print(f"SE at second positins : {str(SE_at_second_position)}")  # output 39

            if str(SE_at_second_position) == str(no_of_lines_between_ST_and_SE):
                print("Line difference between ST and SE segments is correct")
            else:
                print("Line difference between ST and SE segments is not correct")
            k += 1
            print("______________________________________________________________")

    def file_len(self):
        for self.file_path in self.file_paths:
            with open(self.file_path) as f:
                line_count = 0
                for line in f:
                    line_count += 1
            return line_count

    def remove_tilt(self):
        lo.log_to_file(self, "INFO", " Executing Edi_validator.remove_delimiters()")
        k = 1
        for self.file_path in self.file_paths:
            print('File', k, 'IDs Validated')
            file_lens = self.file_len()
            file1 = open(self.file_path, "r")
            data = file1.read()
            # if only one line present in file
            if file_lens == 1:
                for tilt in ['|','~', '☐']:
                    if tilt in data:
                        data = data.replace(tilt, "\n")
            else:
                for tilt in ['~', '|', '☐']:
                    if tilt in data:
                        data = data.replace(tilt, "\n")
            file1.close()
            # print(data)
            file1 = open(self.file_path, "w")
            file1.write(data)
            file1.close()
            print("Successfull Delimiters are Removed from this file.")
            k += 1
            print("______________________________________________________________")