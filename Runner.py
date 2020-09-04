from Scripts_For_TransactionTracker import Runner_for_TransactionTracker as TT
from Scripts_for_FilesAttached import Runner_for_FilesAttached as FA
import self as self

if __name__ == '__main__':
    print("Enter File : ")
    input = input()
    if input == "FA":
        FA.FilesAttached()
    elif input == "TT":
        TT.TransactionTracker(self)


