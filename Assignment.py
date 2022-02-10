## Code Write By:
## Tee Chor Yang
## Lee Jia Qian

import os
## Starting Page
def Start():
    print("\n--- Welcome To SOFS ---\n 1. View As Guest \n 2. Login As Customer \n 3. New Registration \n 4. Login As Admin \n 5. Exit ")
    option = int(input("Select Option: "))
    if option == 1:
        Guest() #User To Guest Page
    elif option == 2:
        Customer() #User To Customer Login
    elif option == 3:
        Register() #User To Registration Page
    elif option == 4:
        Adminlogin() #User To Admin Login
    elif option == 5:
        print("\nExiting...\nThank You!!") #Program End
    else:
        print("\nInvalid Input\nPlease Try Again\n")
        Start()

## Registration Page
def Register():
    print("\n~~~ Registration Page ~~~")
    Username = (input("Enter Username: "))
    Password = (input("Enter Password: "))
    Customer = open("CustomerInfo.txt","r")
    if Username in Customer.read():
        print("\nInvalid Sign-Up\nUsername Is Taken\nType 0 To Proceed")
        Customer.close()
        Exit = int(input("Select Option: "))
        if Exit == 0:
            Start()
    else:
        Customer = open("CustomerInfo.txt","a")
        Customer.write(Username)
        Customer.write(" ")
        Customer.write(Password)
        Customer.write("\n")
        Customer.close()
        print("\nSign-Up Complete\nYou May Proceed To Login\nType 0 To Exit")
        Exit = int(input("Select Option: "))
        if Exit == 0:
            Start()
        else:
            print("\nInvalid Option")
            Start()

## Category Wise
def Menu():
    print("\n~~~ Menu ~~~")
    #Display Category
    print ("\nCategory:\n-------------------------")
    with open('MasterCategory.txt', 'r') as f:
        for line in f:
            y = line.split()
            print(">>> ", y)
            print ("-------------------------")

    #Choose Category
    categoryrecord = (input("Enter Category Name: ") + ".txt")
    with open(categoryrecord, 'r') as infile:
        data = infile.read()
        li = data.splitlines()
        print (f"\nCategory         : {categoryrecord.replace('.txt','')}")
        print("---------------------------------------------------")
        #Display all items based category
        for ele in li:
            detail = ele.split(";")
            print("Items ID         :", detail[0])
            print("Items Name       :", detail[1])
            print("Price(RM)        :", detail[2])
            print("===================================================")
    print("")

## Guest Page        
def Guest():
    print("\n~~~ Guest Page ~~~\n 1. View Menu\n 2. Register\n 3. Back")
    option = int(input("Select Option: "))
    if option == 1: #Opens food file and show Full Menu
        Menu()
        while True:
            print("1 for Back to Select Category\n2 for Exit")
            opt = int(input("Opt: "))
            if opt == 1:
                Menu()
            elif opt == 2:
                Guest()
                return False
            else:
                print("Invalid Input")
                Guest() 
                return False
    elif option == 2:
        Register() #user to registration
    elif option == 3:
        Start() #return user to main page

## Registered Customer/ Customer Page
def RegisteredCust():
    print("\n~~~ Customer Page ~~~\n 1. View Menu\n 2. Order\n 3. Proceed To Payment\n 4. Back")
    option =  int(input("Select Option: "))
    if option == 1:
        Menu()
        while True:
            print("1 for Back to Select Category\n2 for Exit")
            opt = int(input("Opt: "))
            if opt == 1:
                Menu()
            elif opt == 2:
                RegisteredCust()
                return False
            else:
                print("Invalid Input")
                RegisteredCust()  
                return False
        
    elif option == 2:
        OrderID = input("Enter Username: ")
        def OrderPage(): #Customer Order Page
            print("\n~~~ Order Page ~~~")
            #Category Menu
            with open('MasterCategory.txt', 'r') as insidefile:
                data = insidefile.read()
                li = data.splitlines()
                print (f"Hello, {OrderID}")
                print ("Category Name: ")
                print ("-------------------------------")
                #Display all Category
                for ele in li:
                    print(">> ", ele)
                    print ("-------------------------------")
            print("")

            #Enter Category Name or 0 to exit
            print ("Enter [0] to Exit")
            choosecategory = (input("Enter [Category Name] to Procced Order: ") + ".txt")
            if choosecategory == "0.txt":   ## In the end might show error, but not a problem. 0 idea why can not use .replace.
                print("Exiting...")
                RegisteredCust()
            else:
                pass

            while True:
                with open(choosecategory, 'r') as infile:
                    data = infile.read()
                    li = data.splitlines()
                    print (f"\nCategory         : {choosecategory.replace('.txt','')}")
                    print("---------------------------------------------------")
                    #Display all items based category
                    for ele in li:
                        detail = ele.split(";")
                        print("Items ID         :", detail[0])
                        print("Items Name       :", detail[1])
                        print("Price(RM)        :", detail[2])
                        print("===================================================")
                print("")
                print ("Enter [0] to Reselect Category")
                Cart = str(input("Enter [Items ID] To Add To Cart: "))
                if choosecategory == 0:
                    print("Exiting...")
                    OrderPage()
                else:
                    pass
                
                with open(choosecategory,"r") as Orders:
                        MDOrder = Orders.readlines()
                        for MD in MDOrder:
                            MD = MD.strip().split(";")
                            if Cart == MD[0]: # Add Order Into CustomerOrder.txt
                                print("\nThe Food Item Below Has Been Added To Cart")
                                print(MD[0] + " " + MD[1] + " " + MD[2]) 
                                CustomerOrder = str(OrderID) + "," + MD[0] + "," + MD[1] + "," + MD[2] + "\n"
                                with open("CustomerOrder.txt","a") as ADD:
                                    ADD.write(CustomerOrder)
                                    # print("Returning Back To OrderPage...")
                                    # OrderPage()

                addmoreitems = int(input("Do You Want to Leave this Category?\n [1] for YES\n [0] for NO\nOpt: "))
                if addmoreitems == 1:
                    OrderPage()
                    return False
                elif addmoreitems == 0:
                    continue
                else:
                    print ("Invalid Option")
                    print("Exiting to Order Page....")
                    OrderPage()
                    return False 
        OrderPage()

    elif option == 3:
        def Payment(): # Payment Page
            print("\n~~~ Payment Page ~~~\n 1. Check Cart \n 2. Check-Out\n 3. Back")
            option = int(input("Select Option: "))
            if option == 1:
                Check = input("Enter Username: ")
                print("\n=====================================\nThese Are The Food Items In Your Cart\n=====================================")
                with open("CustomerOrder.txt","r") as CheckCart:
                    CCart = CheckCart.readlines()
                    for CC in CCart:
                        CC = CC.strip().split(",")
                        if Check == CC[0]:
                            print(CC[1] + " " + CC[2] + " " + CC[3])
                Exit = int(input("0 To Return: "))
                if Exit == 0:
                    Payment()
                else:
                    print("\nInvalid Input\nPlease Make Sure Input Is Correct\nReturning To Payment Page...")
                    Payment()
            elif option == 2:
                Pay = input("Enter Username: ")
                print("\nSelect Payment Method\n 1. Cash\n 2. Card\n 3. Back")
                option = int(input("Select Option: "))
                if option == 1:
                    with open("CustomerOrder.txt","r") as Count:
                        Amount = Count.readlines()
                        Total = 0
                        for Cash in (Amount):
                            Cash = Cash.strip().split(",")
                            if Pay == Cash[0]:
                                Add = float(Cash[3])
                                Total += Add
                    print("\n===================================\nYour Total is RM",Total,"\n===================================\nThank You For Ordering From SOFS!!!\nHave A Good Day!!!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    Paid = str(Pay) + "," + "Cash" + "," + str(Total) + "\n"
                    with open("CustomerPayment.txt","a") as Cash:
                        Cash.write(Paid)
                        
                elif option == 2:
                    with open("CustomerOrder.txt","r") as Count:
                        Amount = Count.readlines()
                        Total = 0
                        for Card in (Amount):
                            Card = Card.strip().split(",")
                            if Pay == Card[0]:
                                Add = float(Card[3])
                                Total += Add
                    print("\n===================================\nYour Total is RM",Total,"\n===================================\nThank You For Ordering From SOFS!!!\nHave A Good Day!!!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    Paid = str(Pay) + "," + "Card" + "," + str(Total) + "\n"
                    with open("CustomerPayment.txt","a") as Card:
                        Card.write(Paid)
                
                elif option == 3:
                    print("\nReturning To Payment Page...")
                    Payment()
            elif option == 3:
                print("\nReturning To Customer Page...")
                RegisteredCust()
        Payment()
    elif option == 4:
        print("\nReturning To Start Page...")
        Start()
    else:
        print("\nInvalid Input\nPlease Make Sure Input Is Correct")
        RegisteredCust()

## Customer Login       
def Customer():
    print("\n~~~ Customer Login Page ~~~")
    Cust_User = input("Enter Username: ")
    Cust_Pass = input("Enter Password: ")
    for login in open("CustomerInfo.txt","r").readlines(): #Read the lines
        login_info = login.split() # Split on the space
        if Cust_User == login_info[0] and Cust_Pass == login_info[1]:
            print("\n~~ Login Successfull ~~")
            RegisteredCust()
            return True
    else:
        print("\nLogin Failed\nPlease Make Sure Input Is Correct\nType 0 To Exit")
        Exit = int(input("Select Option: "))
        if Exit == 0:
            Start()
        else:
            print("\nInvalid Input\nReturning To Main Page...")
            Start()
        return False

## Login to Access System.
def Adminlogin():
    print("\n~~~ Admin Login Page ~~~")
    Admin_User = input("Enter Username: ")
    Admin_Pass = input("Enter Password: ")
    print ("\nLogging In...")
    for login in open("AdminInfo.txt","r").readlines(): #Read the lines
        login_info = login.split() # Split on the space, and store the results in a list of two strings
        if Admin_User == login_info[0] and Admin_Pass == login_info[1]:
            print("Login Successfully !!")
            AdminPage()
            return True
    else:
        print("\nLogin Failed !")
        print("Please Make Sure Enter Correct Username & Password!\nType (1) To Try Again\nType (0) To Exit")
        loginfiled = int(input("Select Option: "))
        if loginfiled == 1 :
            Adminlogin()
        elif loginfiled == 0 :
            print("Exiting to Starting Page...")
            Start()
        else: 
            print("Invalid Option")
            print("Please Try Again...")
            Adminlogin()
        return False

## Admin Page
def AdminPage():
    print("\n~~~ Admin Page ~~~")
    print(" 1. Add Food Item Category-wise \n 2. Modify Food Item \n 3. Display All Records \n 4. Search Specific Record  \n 5. Exit ")
    option = int(input("Select Option: "))
    if option == 1:
        AddCategory()
    elif option == 2:
        ModifyItems()
    elif option == 3:
        DisplayRecord()
    elif option == 4:
        SearchRecord()
    elif option == 5:
        print("\nExiting...")
        Start()
    else:
        print("Invalid Option")
        print("Please Try Again...")
        AdminPage()

## Add Food Item Category-wise
def AddCategory():
    print("\n~~~ Add Food Item Category-wise ~~~")
    print("> Enter New Category Name to Create New Category and Add Items. <\n> Enter Existing Category Name to Add New Items. <\n")
    #Enter Catetory Name
    newcategory = (input("Enter Category Name: ") + ".txt")
    print ("Loading...")

    #Store into a Master File
    r = open("MasterCategory.txt","r")
    readmaster = r.read()
    r.close()
    masterlist = []
    masterlist = readmaster
    if newcategory.replace('.txt','') not in masterlist:
        s = open("MasterCategory.txt","a")
        s.write("\n")
        s.write(newcategory.replace('.txt',''))
        s.close()
    else:
        pass
        
    #Create a file if file does not exist
    f = open(newcategory, "a")
    f.close()


    print ("\nLoading Successfully !")

    #Add Items
    additem = int(input("\nAdd Items?\n 1 for YES\n 0 for NO\nOpt: "))
    if additem == 1:
        while True:
            items = []
            print("\n~~~ Add Items ~~~")
            itemsid = input("Enter Item ID: ")
            itemsname = input("Enter Item Name: ")
            itemsprice = input("Enter Item Price(RM): ")
            #Store in items list 
            items.append(itemsid)
            items.append(itemsname)
            items.append(itemsprice)  

            f = open (newcategory, "a")

            for ele in items:  # all element in items
                f.write(ele + ";")
            f.write('\n')
            f.close()

            # Add more items
            moreitems = int(input("Add More Items?\n 1 for YES\n 0 for NO\nOpt: "))
            if moreitems == 1:
                continue
            elif moreitems == 0:
                print ("Items Added Successfully")
                AdminPage()
                return False
            else:
                print ("Invalid Option")
                print("Exiting to Admin Page....")
                AdminPage()
                return False 

    elif additem == 0:
        print("Exiting to Admin Page....")
        AdminPage()  
    else :
        print ("Invalid Option")
        print("Exiting to Admin Page....")
        AdminPage()
        
## Modify Food Items
def ModifyItems():
    print("\n~~~ Modify Food Items ~~~")
    # Display and Choose Category
    f = open ("MasterCategory.txt","r")
    print ("Existing Category: ")
    print ("----------------------")
    print (f.read())
    print ("----------------------")
    f.close()
    categorymodify = (input("Enter Category Name: ") + ".txt")

    # Open the category and show items
    while True:
        with open(categorymodify, 'r') as infile:
            data = infile.read()
            li = data.splitlines()
            print ("")
            #Display all elements with NO.
            for ele in li:
                print("Items No.[", li.index(ele)+1, "] >>>", ele)

        #Use items no. to choose modify item
        items_modify = int(input("\nEnter [Items No.] to Modify: "))

        #Show the details of choosen item
        itemformodify = li[items_modify-1]
        detail = itemformodify.split(";")
        print(f"\nItem No.{items_modify}: ")
        print("===================================================")
        print("Items ID         :", detail[0])
        print("Items Name       :", detail[1])
        print("Price(RM)        :", detail[2])
        print("===================================================")

        print ("\nModifying:\t",itemformodify)

        #Modify Items
        newele = input("\nEnter New [ItemsID;Items;Price(RM)] : ")
        print("\nChanging...\n")
        print(li[(items_modify - 1)], ">>>>>", newele)

        li[(items_modify - 1)] = newele
        print("\nResults:")
        print("===================================")
        print(f"\nCategory: {categorymodify.replace('.txt', '')}")
        for ele in li:
            print(ele)

        # Update File
        my_file = open(categorymodify, "w")
        for item in li:
            my_file.writelines(item + "\n")
        my_file.close()

        # Modify more items
        modifymoreitems = int(input("\nModify More Items?\n 1 for YES\n 0 for NO\nOpt: "))
        if modifymoreitems == 1:
            continue
        elif modifymoreitems == 0:
            print ("Items Modified Successfully")
            AdminPage()
            return False
        else:
            print ("Invalid Option")
            print("Exiting to Admin Page...")
            AdminPage()
            return False 

## Display All Records
def DisplayRecord():
    print("\n~~~ Display Records ~~~")
    print("Check Records:\n  1. Food Category\n  2. Food Items Category-wise\n  3. Customer Orders\n  4. Customer Payment\n  5. Exit to Admin Page")
    recordopt = int(input("Opt(1-5): "))
    if recordopt == 1:
        #Food Category
        print ("/\/\ Food Category /\/\ \n")
        with open('MasterCategory.txt', 'r') as insidefile:
            data = insidefile.read()
            li = data.splitlines()
            print ("Existing Category:")
            print ("===============================")
            #Display all Category
            for ele in li:
                print(">>>  ", ele)
                print ("===============================")
        print("")
        os.system('pause') #Press any key to continue
        DisplayRecord()

    elif recordopt == 2:
        #Food Items Category-wise
        print ("/\/\ Food Items Category-wise /\/\ \n")
        #Display Category
        print ("Category:\n-------------------------")
        with open('MasterCategory.txt', 'r') as f:
            for line in f:
                y = line.split()
                print(">>> ", y)
                print ("-------------------------")

        #Choose Category
        categoryrecord = (input("Enter Category Name: ") + ".txt")
        with open(categoryrecord, 'r') as infile:
            data = infile.read()
            li = data.splitlines()
            print (f"\nCategory         : {categoryrecord.replace('.txt','')}")
            print("---------------------------------------------------")
            #Display all items based category
            for ele in li:
                detail = ele.split(";")
                print("Items ID         :", detail[0])
                print("Items Name       :", detail[1])
                print("Price(RM)        :", detail[2])
                print("===================================================")
        print("")
        os.system('pause') #Press any key to continue
        DisplayRecord()
    
    elif recordopt == 3:
        #Customer Orders
        print ("/\/\ Customer Orders /\/\ \n")
        with open('CustomerOrder.txt', 'r') as insidefile: 
            data = insidefile.read()
            li = data.splitlines()
            print ("Customer Orders: ")
            print ("==============================================================")
            #Display all order
            for ele in li:
                print(">>>  ", ele)
                print ("==============================================================")
        print("")
        os.system('pause') #Press any key to continue
        DisplayRecord()

    elif recordopt == 4:
        #Customer Payment
        print ("/\/\ Customer Payment /\/\ \n")
        with open('CustomerPayment.txt', 'r') as insidefile:
            data = insidefile.read()
            li = data.splitlines()
            print ("Customer Payment: ")
            print ("===============================")
            #Display all payment
            for ele in li:
                print(">>>  ", ele)
                print ("===============================")
        print("")
        os.system('pause') #Press any key to continue
        DisplayRecord()

    elif recordopt == 5:
        #Exit
        print("\nExiting to Admin Page....")
        AdminPage()
    
    else:
        #Try again
        print("\nInvalid Option")
        print("Please Try Again...")
        DisplayRecord()

## Search Specific Record 
def SearchRecord():
    print("\n~~~ Search Records ~~~")
    print("Check Records:\n  1. Customer Order\n  2. Customer Payment\n  3. Exit to Admin Page")
    searchopt = int(input("Opt(1-3): "))

    if searchopt == 1:
        #Customer Orders
        print ("\n/\/\ Customer Order /\/\ \n")
        #Search by Order Username
        searchorder = input("Enter Order Username: ")
        f = open ('CustomerOrder.txt', 'r')
        content = f.read()
        content_listbyline = content.splitlines()
        f.close()
        print (f"\nChecking         : {searchorder}")
        print("+++++++++++++++++++++++++++++++++++++++")
        for username in content_listbyline:
            detail = username.split(",")
            if searchorder in detail[0]:
                print("Order ID         :", detail[1])
                print("Order Items      :", detail[2])
                print("Amount           :", detail[3])
                print("+++++++++++++++++++++++++++++++++++++++")
        os.system('pause') #Press any key to continue
        SearchRecord()
        
    elif searchopt == 2:
        #Customer Payment
        print ("\n/\/\ Customer Payment /\/\ \n")
        #Search by Order ID
        searchorder1 = input("Enter Order ID: ")
        f = open ('CustomerPayment.txt', 'r')
        content = f.read()
        content_listbyline = content.splitlines()
        f.close()
        print (f"\nChecking             : {searchorder1}")
        print("+++++++++++++++++++++++++++++++++++++++")
        for username2 in content_listbyline:
            detail = username2.split(",")
            if searchorder1 in detail[0]:
                print("Payment Method       :", detail[1])
                print("Total Amount         :", detail[2])
                print("+++++++++++++++++++++++++++++++++++++++")
        os.system('pause') #Press any key to continue
        SearchRecord()
    
    elif searchopt == 3:
        #Exit
        print("\nExiting to Admin Page....")
        AdminPage()
    
    else:
        #Try again
        print("\nInvalid Option")
        print("Please Try Again...")
        SearchRecord()

Start()