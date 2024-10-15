
from tabulate import tabulate
import sys


Table1 = { "BookingName":"", "BookState":False, "PeopleNumber":0}
Table2 = { "BookingName":"", "BookState":False, "PeopleNumber":0}
Table3 = { "BookingName":"", "BookState":False, "PeopleNumber":0}
Table4 = { "BookingName":"", "BookState":False, "PeopleNumber":0}
Table5 = { "BookingName":"", "BookState":False, "PeopleNumber":0}

def main():

    print(" \nWelcome to our restaurante ")
    while True:
        process_menu()
        try:
            num = int(input("Choose the number for your process: "))
        except ValueError:
            print("Enter a number (1-4)")

        match num:
            case 1:
                Table_menu()
                TableNum = take_table_num()
                name,PeopleNumber = take_inputing()
                print(Booking(TableNum,name,PeopleNumber))
            case 2:
                Name = get_Name()
                print(Change_the_book(Name))
            case 3:
                Name = get_Name()
                check_cancel_Name(Name)
                if check_cancel_Name(Name) != f"\nname: {Name} Not Found":
                    Name, x = check_cancel_Name(Name)
                    sure = check_sure()
                    print(Cancel_the_book(sure,x))
                else: print(f"\nname: {Name} Not Found")
            case 4:
                Exiting()
            case _:
                print("Enter a valid number")

def take_table_num():
        while True :
            try :
                TableNum = int(input("Choose a table via number: "))
                if TableNum > 5 or TableNum < 1 :
                    raise ValueError
                x = eval(f"Table{str(TableNum)}")
                if x["BookState"] == True:
                    raise Exception("this table isn't free")
                return TableNum
            except ValueError :
                print("there is no table with this number\n")
            except Exception as e : 
                print(str(e))

def take_inputing():

    while True : 
        name = get_Name()
        if name != None:  
            break
    
    while True :
        try :
            PeopleNumber = int(input("Number of people who are coming: "))
            if PeopleNumber > 0 :
                break
        except ValueError:
            print("Enter a number")
    return (name,PeopleNumber)

def get_Name():

    while True:
        is_valid = True
        Name = input("Enter book name: ").title() 
        for i in Name.split(" ") : 
            if not i.isalpha():
                is_valid = False
                print("Enter a name without numbers")
                break
                    
        if is_valid:
            return Name

def Booking(TableNum,name,PeopleNumber):

        x = eval(f"Table{str(TableNum)}")
        x["BookingName"] = name
        x["BookState"] = True
        x["PeopleNumber"] = PeopleNumber 
        return("================\nSuccessful book\n================")

def Change_the_book(Name):

        for i in range(1,6):
            x = eval(f"Table{str(i)}")
            if x["BookingName"] == Name :
                print("\nEnter your changes : ")
                BookingName,People_Number = take_inputing()

                x["BookingName"] = BookingName
                x["PeopleNumber"] = People_Number
                return("================\nSuccessful change\n================")

        return(f"\nname: {Name} Not Found")

def check_cancel_Name(Name):
    for i in range(1,6):
        x = eval(f"Table{str(i)}")
        if x["BookingName"] == Name:
            return Name,x
            
    return(f"\nname: {Name} Not Found")

def check_sure():
    sure = input("\nare you sure you want to cancel? (Y/N) ").upper()
    while sure not in ("Y","YES","NO","N"):
        print("Enter 'Y' or 'N': ")
    return sure

def Cancel_the_book(sure,x):
        if sure in ("Y","YES"):
                x["BookingName"] = " "
                x["BookState"] = False
                x["PeopleNumber"] = 0
                return("===================\nCanceled Successfully\n===================")
        else: return ""

def Exiting():
    sys.exit("\n===================================\nThank you for choose our restaurante\n===================================\n")

def process_menu():
        verbs = [["1","book a table"], ["2","change the book"], ["3","cancel the book"], ["4","Exit"]]
        print(f"\n{tabulate(verbs,headers='firstrow',tablefmt='grid')}")

def Table_menu():
    tables = [["1","table1"],["2","table2"],["3","table3"],["4","table4"],["5","table5"]]
    print(f"\n{tabulate(tables,headers='firstrow',tablefmt='grid')}")

if __name__ == "__main__" :
    main()
