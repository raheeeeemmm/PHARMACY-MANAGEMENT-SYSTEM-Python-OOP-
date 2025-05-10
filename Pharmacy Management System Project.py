from random import randint
from abc import ABC, abstractmethod
import sys
r = randint(10000,99999)
print("\nWelcome To Pharmacy Management System!\n") # Basic name display!

class Error(Exception): # class made for exceptional handling to be used later!
    pass

class ValueTooSmallError(Error): # class made for exceptional handling to be used later!
    pass

class abstract(ABC):
    _x = False # to be used in credentials function in next class as a checker in check function to determine weather 
                #the program will enter the loop outside the classes or not!
    @abstractmethod
    def credentials(): #used as a blueprint! Will be used later as to be saied that it will be overwritten (that's the purpose).
        pass
    def checking():
        pass


class Medicine:
    __y = False
    admin = 'pharmacy'
    pswd = 'qqq'

    @property
    def Get_Details(self): #getting 4 things from the user: (Id, Rate, Power & Stock)
        self.__id = input("\nEnter Medicine ID: ")
        while True:
            try:
                self.rate = int(input("Enter Rate Per Packet: ")) 
                if (self.rate <= 0):
                  raise ValueTooSmallError
                break
            except ValueError as e:
                print("\nINVALID LITERAL for int() with Base 10", e)
                print("Try again!")
            except ValueTooSmallError:
               print("Price can Never be Zero-0 or any Negative Value!")
        while True:
            try:
                self.power = int(input("Power of that Medicne/Tablet (i.e; 250mg, 500mg): "))
                if (self.power <= 0):
                  raise ValueTooSmallError
                break
            except ValueError as e:
                print("\nINVALID LITERAL for int() with Base 10", e)
                print("Try again!")
            except ValueTooSmallError:
               print("Price can Never be Zero-0 or any Negative Value!")
        while True:
            try:
                self.stock = int(input("Enter Available Stock: "))
                if (self.stock <= 0):
                    raise ValueTooSmallError
                break
            except ValueError as e:
                print("\nINVALID LITERAL for int() with Base 10", e)
                print("Try again!")
            except ValueTooSmallError:
               print("Stock can only be in integer & also not any Negative value\nTry again!")

    def credentials(abstract): #person is being called here from abstract class to be overwritten!
        for i in range(3): # for username
            m = input("\nLogin ID: ").lower()
            if (m == Medicine.admin):
                Medicine.__y = True
                break
            else:
                print("\nWrong Details!")
                abstract._x = False

        if (Medicine.__y == True):
            for j in range(3): #for password
                w = input("Enter Passcode: ").lower()
                if (w == Medicine.pswd):
                    P.Get_Details
                    print("\nYOU HAVE BEEN SUCCESSFULLY LOGGED IN!")
                    abstract._x = True
                    break
                else:
                    print("\nWrong Passcode!")
                    abstract._x = False
        else:
            abstract._x = False
    
    def checking(abstract):
        if abstract._x == True:
            return True
        else:
            print("\nYou have Entered Wrong Details!\nYou have been LOGGED OUT!")
            return False
    
    def Display_Details(self):
        print("(ID:",self.__id, ") (Price:",self.rate, ") (Power:",self.power, ") (Stock:",self.stock,")")
	
    def Setter_id(self, id): #being used her as a searcher to verify that if indeed something exists or not!
      if self.__id == id:   #also Setter from Setter - Getter!
          return True
      else:
          return False

    def getter_id(self):  #Simply Getter from Setter - Getter!
      return self.__id

    def Sale(self):    # purchasing 
        print("\nPresent Stock is:", self.stock)
        d = input("Enter Purchaser Name: ")
        if(self.stock > 0):
            q = int(input("Enter Quantity to Buy: "))
            if (q <= self.stock):
                total = q * self.rate
                print("\nAmount:",total)
                self.stock -= q
                
                disc = 0
                if total in range(0,500):
                    disc = 0 / 100 * total
                    finalp = total - disc
                    print("\nDiscount - 0% :",disc)
                elif total in range(501,1000):
                    disc = 5 / 100 * total
                    finalp = total - disc
                    print("\nDiscount - 5% :",disc)
                elif total in range(1001,1500):
                    disc = 10 / 100 * total
                    finalp = total - disc
                    print("\nDiscount - 10% :",disc)
                elif total in range(1501,2500):
                    disc = 20 / 100 * total
                    finalp = total - disc
                    print("\nDiscount - 20% :",disc)
                else:
                    disc = 25 / 100 * total
                    finalp = total - disc
                    print("\nDiscount - 25% :",disc)
                
                #Receipt:
                print("\n-----------------------")
                print("-----------------------")
                print("----------PMS----------")
                print("-----------------------")
                print(" "*18 ,r)
                print("Your Medicine is:\n(",self.__id,")")
                print('\nDeduction = ',total,"-",disc)
                print("BILL:",finalp,"Rs only!\n")
                print("\nThank- You!", d)

            else:
                print("Not Enough Quantity Available!")
        else:
            print("Not Enough Stock Available!")

    def display(self,id):   # to simply change name of any Medicine
        self.__id = input("Enter new ID: ")
        print("\nUpdated Name is:", self.__id)

    def updater_stock(self,id):
        q = input("Add or New: ").lower()
        if q == 'add':
            n = int(input("Add/Subtract Stock: "))
            self.stock += n
            print("\nUpdated Stock of",self.__id, "is: ", self.stock)
        else:
            while True:
                try:
                    self.stock = int(input("New Stock: "))
                    if (self.stock <= 0):
                        raise ValueTooSmallError
                    print("\nUpdated Stock of",self.__id, "is: ", self.stock)
                    break
                except ValueError as e:
                    print("\nINVALID LITERAL for int() with Base 10", e)
                    print("Try again!")
                except ValueTooSmallError:
                    print("Stock can only be in integer & also not any Negative value\nTry again!")
            
class End(Medicine):
    
    @staticmethod
    def display():
        print("\nThank-You!\n\n***********************\nProject By: Abdul Rahim, Syed Dawood, Raza Ullah, Huzaifa Nasir & Saad Ashraf\n***********************")

# ----------------------
L = [] # to append all details!
S = End()

try:
    n = int(input("How many Medical-Items to add: "))
except ValueError:
    print("Invalid Literal for int() with Base - 10: ")

for i in range(n):
    P = Medicine()
    P.credentials()
    L.append(P)
# ----------------------
while P.checking():
    print("""\n***********************
    Main - Menu:
***********************""")
    print("\n1-  Show All Medics Details.\n2-  Add New Information.\n3-  Search By ID/Name.\n4-  Delete Single Item.\n5-  Delete All Records.\n6-  Purchase.\n7-  Purchase Multiple.\n8-  Update ID.\n9-  Update Stock.\n10- Exit\n")
    ch = int(input("***********************\nEnter Your Choice: "))

    if ch == 1:
        print("\nMedics Available:\n")
        for c in L:
            if L == []:
                print("No Medics Available in Stock!")
            else:
                c.Display_Details()
    elif ch == 2:
        o = int(input("\nHow Many More items to Add: "))
        for i in range(o):
            P = Medicine()
            P.credentials()
            L.append(P)
    elif ch == 3:
        id = input("\nEnter Medic ID/Name to Search: ")
        found = False
        for c in L:
            found = c.Setter_id(id)
            if found == True:
                print("Details From ID Found:")
                c.Display_Details()
                break
        if not found:
            print("Not - Found!")
    elif ch == 4:
        id = input("\nEnter Medicine ID to Delete: ")
        found = False
        for c in L:
            found = c.Setter_id(id)
            if found == True:
                L.remove(c)
                print("Medic-Item has Been Deleted!")
                break
        if not found:
            print("Not - Found!")
    elif ch == 5:
        L.clear()
        print("All Medical Details has been Removed!\nDatabase is EMPTY!")
    elif ch == 6:
        q = input("\nEnter ID/Name of Medical Item to Purchase: ")
        found = False
        for c in L:
            found = c.Setter_id(q)
            if found == True:
                print("\nRECEIPT:")
                c.Sale()
                S.display()
        if not found:
            print("Not - Found!")
    elif ch == 7:
        i = int(input("How Many Medical items to Purchase: "))
        for r in range(i):
            q = input("\nEnter ID/Name of Medical Item to Purchase: ")
            found = False
            for c in L:
                found = c.Setter_id(q)
                if found == True:
                    print("\nRECEIPT:")
                    c.Sale()
                    S.display()
            if not found:
                print("Not - Found!")
    elif ch == 8:
        id = input("\nEnter Medic ID/Name to Update: ")
        found = False
        for c in L:
            found = c.Setter_id(id)
            if found == True:
                print("ID Found:")
                c.display(id)
                break
        if not found:
            print("Not - Found")
    elif ch == 9:
        id = input("\nEnter Product ID to Update Stock in: ")
        found = False
        for c in L:
            found = c.Setter_id(id)
            if found == True:
                print("ID Found:")
                c.Display_Details()
                c.updater_stock(id)
                break
        if not found:
            print("Not - Found")
    elif ch == 10:
        S.display()
        break
    else:
        print("Invalid Choice - Try Again!")