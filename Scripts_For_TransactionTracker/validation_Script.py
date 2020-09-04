class Edi_Validator():

    def __init__(self,lo,Sender_Qualifiers,Receiver_Qualifiers,fname,Supplier_Version,Retailer_Version,
                 GS_Supplier_Version,GS_Retailer_Version,Document_version):
        self.lo = lo
        self.Sender_Qualifiers = Sender_Qualifiers
        self.Receiver_Qualifiers = Receiver_Qualifiers
        self.fname = fname
        self.Supplier_Version = Supplier_Version
        self.Retailer_Version = Retailer_Version
        self.GS_Supplier_Version = GS_Supplier_Version
        self.GS_Retailer_Version = GS_Retailer_Version
        self.Document_version = Document_version

    def file_len(self):
        with open(self.fname) as f:
            line_count = 0
            for line in f:
                line_count += 1
        return line_count

    def validation_for_Qualifiers(self):
        self.lo.log_to_file(self, "INFO", " Executing Edi_validator.validation_for_Qualifiers()")
        file1 = open(self.fname, "r")
        data = file1.readlines()
        sender_qualifiers = str(data[0].split('*')[7])
        receiver_qualifier = str(data[0].split('*')[5])
        if sender_qualifiers == str(self.Sender_Qualifiers) or receiver_qualifier == str(self.Receiver_Qualifiers):
            print(f"Supplier and Retailer Qualifier is Matched {sender_qualifiers} and {receiver_qualifier}")
        else:
            print(f"Supplier and Retailer Qualifier is NOT Matched {sender_qualifiers} and {receiver_qualifier}")
        print("______________________________________________________________")

    def Document_versions(self):
        self.lo.log_to_file(self, "INFO", " Executing Edi_validator.Document_version()")
        file1 = open(self.fname, "r")
        data = file1.readlines()
        Doc_version = str(data[0].split('*')[12])
        # print(Doc_version)
        if Doc_version == self.Document_version:
            print(f"Document Version Is MATCHED {Doc_version}.")
        else:
            print("Document version is NOT Matched.")
        print("______________________________________________________________")

    def remove_delimiters(self):
        self.lo.log_to_file(self, "INFO", " Executing Edi_validator.remove_delimiters()")
        file_lens = self.file_len()
        file1 = open(self.fname, "r")
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
        file1 = open(self.fname, "w")
        file1.write(data)
        file1.close()
        print("Successfull Delimiters are Removed from this file.")
        print("______________________________________________________________")

    def presence_of_U(self):
        self.lo.log_to_file(self, "INFO", " Executing Edi_validator.presence_of_U")
        file_lens = self.file_len()
        file1 = open(self.fname, "r")
        data = file1.read()
        if file_lens == 1:
            self.remove_delimiters()
            pass
        else:
            for u in ['*U*']:
                if u in data:
                    print("Mandatory U Segment is present in this File.")
                else:
                    print("Mandatory U Segment is NOT In this File.")
        print("______________________________________________________________")

    def validate_supplier_retailer_cability_version(self):
        self.lo.log_to_file(self, "INFO", " Executing Edi_validator.validate_supplier_retailer_cability_version()")
        file1 = open(self.fname, "r")
        data = file1.readlines()
        ISA_Retailer_field = str(data[0].split('*')[6])
        ISA_Supplier_field = str(data[0].split('*')[8])
        GS_Supplier_field = str(data[1].split('*')[3])
        GS_Retailer_field = str(data[1].split('*')[2])
        try:
            if self.Retailer_Version == ISA_Retailer_field or GS_Retailer_field == self.GS_Retailer_Version:
                print("ISA and GS Retailer Version Matched")
            else:
                print("ISA and GS Retailer Version Not Matched")
            if ISA_Supplier_field == self.Supplier_Version or GS_Supplier_field == self.GS_Supplier_Version:
                print("ISA and GS Supplier Version Matched")
            else:
                print("ISA and GS Supplier Version not Matched")
        except:
            pass
        print("______________________________________________________________")

    def ST_and_GE_Validation(self):
        self.lo.log_to_file(self, "INFO", " Executing Edi_validator.ST_and_SE_validation()")
        with open(self.fname, 'r') as fi:
            i = 0
            for line in fi:
                # print(line)
                if line.startswith('ST'):
                    # print(line)  # output: ST*850*113986
                    i += 1
            print(f"Number of Time ST is present : {i}")
            ST_Count = str(i)
        fi.close()
        with open(self.fname, 'r') as fii:
            j = 1
            for line in fii:
                if line.startswith('GE'):
                    # print(line)
                    GE_line = line
                    break
                j += 1
            # print("GE is present at line Number :", j)
        fii.close()
        # file1 = open(self.fname, "r")
        # data = fii.readlines()
        GE_count = str(GE_line.split('*')[1])
        print(f"GE side number is : {GE_count}")
        if ST_Count == GE_count:
            print("GE count is equal to count of ST segment present in the file.")
        else:
            print("Something went Wrong")
        print("______________________________________________________________")

    def ST_and_SE_Validation(self):
        self.lo.log_to_file(self, "INFO", " Executing Edi_validator.ST_and_SE_validation()")
        file = open(self.fname, 'r')
        linelist = file.readlines()
        file.close()
        if len(linelist) <= 2:
            with open(self.fname, 'r') as f:
                for line in f.readlines():
                    first_line = line.split("GS")[0]
                    # print(first_line)
                    delemitor = first_line.split("ISA")[1][0:1]
        else:
            f = open(self.fname, 'r')
            first_line = f.readline()
            delemitor = first_line.split("ISA")[1][0:1]
            # first_line = first_line.split()[-1]
            # line_separator = first_line[-1:]
            # print(line_separator)
            # print(delemitor)

        with open(self.fname, 'r') as fii:
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
        print("______________________________________________________________")

    def Interchange_Header_Segment_Validation(self):
        self.lo.log_to_file(self, "INFO", " Executing Edi_validator.Interchange_Header_Segment_Validation()")
        file = open(self.fname, 'r')
        linelist = file.readlines()
        file.close()
        if len(linelist) <= 2:
            with open(self.fname, 'r') as f:
                for line in f.readlines():
                    first_line = line.split("GS")[0]
                    # print(first_line)
        else:
            f = open(self.fname, 'r')
            first_line = f.readline()
            first_line = first_line.split()[-1]
            line_separator = first_line[-1:]
            # print(line_separator)
            if line_separator == ">":
                print(f"Ending of Interchange Header segment should be with {str(line_separator)} is there.")
            else:
                print(f"Ending of Interchange Header segment should be with {str(line_separator)} is NOT there.")
        print("______________________________________________________________")

    def spacing_validation(self):
        self.lo.log_to_file(self, "INFO", " Executing Edi_validator.spacing_validation()")
        file = open(self.fname, 'r')
        for line in file:
            fields = line.split('*')
            # print(fields)   # output : ISA 1st line.
            if fields[0] == "ISA":
                print(f"ID : {str(fields[6])}" f" ID : {str(fields[8])}")
                print(f"ISA_ID:{str(len(str(fields[6])))}" f"  ISA_ID:{str(len(str(fields[8])))}")
                print(f"ISA:{str(len(str(fields[2])))}" f"  ISA:{str(len(str(fields[4])))}")
            break
        print("______________________________________________________________")