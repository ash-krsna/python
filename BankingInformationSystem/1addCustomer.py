import pickle
import sys
sys.path.append("D:\\Python\\BankingInformationSystem")
from nameValidation import validatename
from nameExcept import ZeroNameLengthError, SpaceError, InvalidNameError
def isunique(lst):
    with("D:\\Python\\BankingInformationSystem\\customer.data","rb") as fp:
        records = []
        while(True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
        #found = True
        for record in records:
            if(recod[0] == lst[0]):
                found = False
                break
        return found

def addcustomer():
    with open("D:\\Python\\BankingInformationSystem\\customer.data","ab") as fp:
        while(True):
            try:
                print("-"*50)
                custno = int(input("\tEnter Customer Number:"))
                name = input("\tEnter Customer Name:")
                custname = validatename(name)
addcustomer()
