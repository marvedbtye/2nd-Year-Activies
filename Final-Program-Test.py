import pandas as pd
import json
from pathlib import Path
import sys

class function_list: # main class to bundle all the functions

    # function to initialize several variables
    def __init__(self): 
        self.is_newFile = False
        self.jsonRead_dict = {}
        self.tempData = {
            "Item Code": [],
            "Item Name": [],
            "Beginning Stock": [],
            "Unit of Measure": [],
            "Value per Unit": [],
            "Reorder Stock": [],
            "On-hand Stock": [],
            "Total Value": []
        }

    # function for the declaration of the username, password, and its conditions
    def login(self): 
        self.username = "Small Food Business"
        self.password = "98123food"
        while True:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username != "Small Food Business" and password != "98123food":
                print("\nInvalid username and password.")
                print("Please try again.")
                continue
            elif username != "Small Food Business":
                print("\nInvalid username. Please try again.")
                continue
            elif password != "98123food":
                print("\nInvalid password. Please try again.")
                continue
            else:
                print("Logged in successfully.\n")
                break

    # function for loading an existing JSON file
    def load_data(self, joinPath): 
        with open(joinPath, "r") as openFile: 
            jsonRead = openFile.read()
        self.jsonRead_dict = json.loads(jsonRead) 
        
        
    # function for saving to a JSON file
    def save_data(self, joinPath, tempData): 
        with open(joinPath, "w") as saveFile:
            json.dump(tempData, saveFile)

    # function for the search/creation of a folder,"JSON Stock"
    # and the conditionals for the user-input file name
    def sys_bootup(self, fileExtend):
        self.joinPath = Path.cwd().joinpath("JSON Stock")
        if not self.joinPath.is_dir():
            self.joinPath.mkdir(parents=True)
            self.joinPath = self.joinPath.joinpath(fileExtend + ".json")
        else:
            self.joinPath = self.joinPath.joinpath(fileExtend + ".json")
        try:
            self.load_data(self.joinPath)
            print("File located.")
            self.is_newFile = False
        except FileNotFoundError:
            self.is_newFile = True
            print("File not found. Creating new file...")
            self.save_data(self.joinPath, self.tempData)
            self.load_data(self.joinPath)
            print("New file created.")

            
    # function for exiting the program   
    def sys_exit(self):
        self.load_data(self.joinPath)
        print("Program terminated.")
        sys.exit()

    # function for a separate print of the available services
    def show_services(self):
        print("\t\t\t\t\t\t\t\tSERVICES\n\n")
        print("\t\t\t\t\tCode\tDescription")
        print("\t\t\t\t\t[A]\t\tCheck Inventory")
        print("\t\t\t\t\t[B]\t\tAdd Items")
        print("\t\t\t\t\t[C]\t\tUpdate Items")
        print("\t\t\t\t\t[D]\t\tDelete Items")
        print("\t\t\t\t\t[E]\t\tStats for Nerds")
        print("\t\t\t\t\t[F]\t\tExit")
        

    # function for displaying the data using pandas table
    def display_table(self):
        if self.is_newFile == True:
            print("No data available.")
        else:
            table = pd.DataFrame(self.jsonRead_dict)
            print(table)
           
    # function to confirm the saving of the changes the user made 
    def confirm(self):
        confirm = ""
        while confirm == "":
            confirm  = input("Confirm to update data[y/n]: ")
            if confirm == "y" or confirm == "Y":
                self.is_newFile = False
                self.save_data(self.joinPath, self.jsonRead_dict)
                print("\nInventory updated.")
                print("This is your new inventory: \n")
                self.load_data(self.joinPath)
                self.display_table()
            elif confirm == "n" or confirm == "N":
                return
            else:
                print("Invalid code.")
                continue
            
    # function to display inventory data and revenue
    def srvcCode_A(self):
        choose = ""
        while choose == "":
            choose  = eval(input("Do you want to search for a specific item [1] or display the whole table [2]? "))
            if choose == 1:
                self.load_data(self.joinPath)
                keyDis = input("Enter the item name to search [case sensitive]: ")
                if keyDis not in self.jsonRead_dict["Item Name"]:
                    print("Item not found in the inventory.")
                    return 
                else:
                    self.load_data(self.joinPath)
                    getIndex_Dis = self.jsonRead_dict["Item Name"].index(keyDis)
                    displayDict = {key: [self.jsonRead_dict[key][getIndex_Dis]] for key in self.jsonRead_dict}
                    disTable = pd.DataFrame(displayDict)
                    print(f"\n{disTable}")
            elif choose == 2:   
                self.load_data(self.joinPath)
                self.display_table()
            else:
                print("Invalid code.")
                continue

        

        
        
    # function to add inventory data
    def srvcCode_B(self):
        print("\nThis is your current inventory:\n")
        self.load_data(self.joinPath)
        self.display_table()
        
        storCode = []
        storName = []
        storQuan = []
        storUnit = []
        storValue = []
        storReorder = []
        storOnHand = []
        storTotalVal = []

        
        
        
        srvcQuan = int(input("Type the quantity of your service: "))
        for i in range(srvcQuan):
            itmCode = input("\nItem Code: ")
            itmName = input("Item Name: ")
            itmQuan = input("Beginning Stock Quantity: ")
            itmUnit = input("Unit of Measure: ")
            itmValue = input("Item value (per unit of measure): ")
            itmReorder = input("Reorder Stock Quantity: ")
            itmOnHand = input("On-hand Stock Quantity: ")
            tempTotal = float((eval(itmQuan)+eval(itmReorder)) * eval(itmValue))
            print(f"\nTotal Value: \u20b1 {tempTotal}")
            
            storCode.append(itmCode)
            storName.append(itmName)
            storQuan.append(itmQuan)
            storUnit.append(itmUnit)
            storValue.append(itmValue)
            storReorder.append(itmReorder)
            storOnHand.append(itmOnHand)   
            storTotalVal.append(str(round(tempTotal,2)))
            
            newData = {
                "Item Code": storCode,
                "Item Name": storName,
                "Beginning Stock": storQuan,
                "Unit of Measure": storUnit,
                "Value per Unit": storValue,
                "Reorder Stock": storReorder,
                "On-hand Stock": storOnHand,
                "Total Value": storTotalVal
                }
            
            
            
            self.load_data(self.joinPath)
            for i in newData["Item Code"]: 
                self.jsonRead_dict["Item Code"].append(i)
            for i in newData["Item Name"]: 
                self.jsonRead_dict["Item Name"].append(i)
            for i in newData["Beginning Stock"]:
                self.jsonRead_dict["Beginning Stock"].append(i)
            for i in newData["Unit of Measure"]:
                self.jsonRead_dict["Unit of Measure"].append(i)
            for i in newData["Value per Unit"]:
                self.jsonRead_dict["Value per Unit"].append(i)
            for i in newData["Reorder Stock"]:
                self.jsonRead_dict["Reorder Stock"].append(i)
            for i in newData["On-hand Stock"]:
                self.jsonRead_dict["On-hand Stock"].append(i)
            for i in newData["Total Value"]:
                self.jsonRead_dict["Total Value"].append(i)
            
        add_items = pd.DataFrame(newData)
        print(f"\n {add_items}")
        self.confirm()
            
    
    # function to update the value and quantity of an item                    
    def srvcCode_C(self): 
        if self.is_newFile == True:
            print("No data available.")
        else:
            self.load_data(self.joinPath)
            self.display_table()
            keyUpd = input("Enter the item name to update [case sensitive]: ")
            if keyUpd not in self.jsonRead_dict["Item Name"]:
                print("Item not found in the inventory.")
                return 
            else:
                selectIndex = self.jsonRead_dict["Item Name"].index(keyUpd)
                newQuan = input("Enter the new beginning quantity: ")
                newVal = input("Enter the new value: ")
                newReorder = input("Enter the new reorder quantity: ")
                newOnHand = input("Enter the new on-hand quantity: ")
                newTotal = float((eval(newQuan)+eval(newReorder)) * eval(newVal))
                self.jsonRead_dict["Beginning Stock"][selectIndex] = newQuan
                self.jsonRead_dict["Value per Unit"][selectIndex] = newVal
                self.jsonRead_dict["Reorder Stock"][selectIndex] = newReorder
                self.jsonRead_dict["On-hand Stock"][selectIndex] = newOnHand
                self.jsonRead_dict["Total Value"][selectIndex] = str(newTotal)
                self.confirm()
                
    # function to delete an inventory data          
    def srvcCode_D(self): 
        if self.is_newFile == True:
            print("No data available.")
        else:
            self.load_data(self.joinPath)
            self.display_table()
            keyDel = input("Enter the item name to delete [case sensitive]: ")
            if keyDel not in self.jsonRead_dict["Item Name"]:
                print("Item not found in the inventory.")
                return 
            else:
                getIndex_Del = self.jsonRead_dict["Item Name"].index(keyDel)
                self.load_data(self.joinPath)
                del self.jsonRead_dict["Item Code"][getIndex_Del]
                del self.jsonRead_dict["Item Name"][getIndex_Del]
                del self.jsonRead_dict["Beginning Stock"][getIndex_Del]
                del self.jsonRead_dict["Unit of Measure"][getIndex_Del]
                del self.jsonRead_dict["Value per Unit"][getIndex_Del]
                del self.jsonRead_dict["Reorder Stock"][getIndex_Del]
                del self.jsonRead_dict["On-hand Stock"][getIndex_Del]
                del self.jsonRead_dict["Total Value"][getIndex_Del]
                
                self.confirm()
    
    #function to show the statistics
    def srvcCode_E(self): 
        totalQuan = 0
        totalReorder = 0
        totalonHand = 0
        endInv = 0
        begInv = 0
        newInv = 0
        expectedRev_total = 0
        actualRev_total = 0

        for i in range(len(self.jsonRead_dict["Item Name"])):
            quan = float(self.jsonRead_dict["Beginning Stock"][i])
            val = float(self.jsonRead_dict["Value per Unit"][i])
            reorder = float(self.jsonRead_dict["Reorder Stock"][i])
            onHand = float(self.jsonRead_dict["On-hand Stock"][i])
            totVal = float(self.jsonRead_dict["Total Value"][i])
            actualRevenue = (quan+reorder-onHand)*val
            beg = quan*val
            new = reorder*val
            end = onHand*val 
            

            
            totalQuan += quan
            totalReorder += reorder
            totalonHand += onHand

            endInv += end
            begInv += beg
            newInv += new
            expectedRev_total += totVal
            actualRev_total += actualRevenue
        
        

        
        
        #test delete
        print(totalQuan)
        print(totalReorder)
        print(totalonHand)
        print(begInv)
        print(newInv)
        print(endInv)
        
        cogs = (endInv + newInv) - endInv
        aveInventory = (begInv + endInv)/2
        gross = actualRev_total - cogs
        itr = cogs/aveInventory
        dsi = (aveInventory/cogs)*365
        sellTR = (((totalQuan+totalReorder)-(totalonHand))/(totalQuan+totalReorder))*100
            
            
        print(f"\nBeginning Inventory: \u20b1 {round(begInv,2)}") 
        print(f"Ending Inventory: \u20b1 {round(endInv,2)}") 
        print(f"Cost of Goods Sold: \u20b1 {round(cogs,2)}")  
        print(f"Expected Revenue: \u20b1 {round(expectedRev_total,2)}")  
        print(f"Actual Revenue: \u20b1 {round(actualRev_total,2)}")  
        print(f"Gross Profit: \u20b1 {round(gross,2)}")
        print(f"Inventory Turnover Ratio: {round(itr,2)}")
        print(f"Days Sale of Inventory: {round(dsi,2)}")
        print(f"Sell-Through Rate: {round(sellTR,2)}%")
        



        

    # function to prompt user whether to use another service or not
    def reSrvc(self):
        while True:
            reSrvc = input("Would you like to use another service? [y/n] ")
            if reSrvc == "Y" or reSrvc == "y":
                    self.show_services()
                    srvcCode = input("\nEnter Service Code: ")
                    if srvcCode == "A" or srvcCode == "a":
                        self.srvcCode_A()
                    elif srvcCode == "B" or srvcCode == "b":
                        self.srvcCode_B()
                        self.confirm()
                    elif srvcCode == "C" or srvcCode == "c":
                        self.srvcCode_C()
                        self.confirm()
                    elif srvcCode == "D" or srvcCode == "d":
                        self.srvcCode_D()
                        self.confirm()
                    elif srvcCode == "E" or srvcCode == "e":
                        self.srvcCode_E()
                    elif srvcCode == "F" or srvcCode == "f":
                        self.sys_exit()
                    else:
                        print("\nInvalid code. Please try again.")
                        continue
            elif reSrvc == "N" or reSrvc == "n":
                self.sys_exit()
            else:
                print("Invalid code.")
                continue

# main function to layout the system
def main():
    print("\n\t\t\t\t\t\t Stock Count Tracking System \t\t\t\t\t\t")
    func = function_list()
    func.login()
    fileExtend = input("Type in any file name: ")
    func.joinPath = fileExtend + ".json" 
    func.sys_bootup(fileExtend) 
    func.show_services()
    while True:
        srvcCode = input("Type the code of your choice: ")
        if srvcCode == "A" or srvcCode == "a":
            func.srvcCode_A()
            func.reSrvc()
        elif srvcCode == "B" or srvcCode == "b":
            func.srvcCode_B()
            func.reSrvc()
        elif srvcCode == "C" or srvcCode == "c":
            func.srvcCode_C()
            func.reSrvc()
        elif srvcCode == "D" or srvcCode == "d":
            func.srvcCode_D()
            func.reSrvc()
        elif srvcCode == "E" or srvcCode == "e":
            func.srvcCode_E()
            func.reSrvc()
        elif srvcCode == "F" or srvcCode == "f":
            func.sys_exit()
        else:
            print("Invalid code.")
            continue
    

main() # calling the main function
    
