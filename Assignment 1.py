# Program Name  : Shopping program
# Created by    : Francois Mindiel
# Created date  : 05/03/16
# Version       : 1.0
# Description   :
# Mr Key has assigned me with the creation of a shopper program for his supermarket.
# It is intended for his loyal customers, to choose their favorite product items from the site,
# making sure that after selecting product items the program calculates the total cost of the items.

# Update History:

companyname = "3 Triangles Supermarket"                 # Name of company stored as string
totalcost=0                                             # variable to store total cost of items selected
quitshop=False                                          # While False, while loop will keep asking for new items
selecteditems=""                                        # String used to store items intended to be bought


while quitshop == False:                                # Loop will keep going until quitshop == True

    print ("Let's go shopping! ")

    print ("Welcome to the " + companyname + " online store!")
    print ("  ")

    print ("What's on the menu? \n")                    # This part is to display items list in a numbered list

    print (" 1. Shapes (Pizza flavour) \t $ 3.50")
    print (" 2. Colgate toothpaste \t\t $ 7.00")
    print (" 3. Balloons (12 pack) \t\t $ 1.00")
    print (" 4. Red Lecture book (2B8) \t $ 2.50")
    print (" 5. Vanilla scented candle \t $ 5.50")
    print (" 6. AA batteries (4 pack) \t $10.00")
    print (" 7. Panadol (pack of 12) \t $12.50")
    print (" 8. Bananas (bunch of 3) \t $ 5.50")
    print (" 9. Sudocrem 10g net \t\t $18.50")
    print ("10. Black pens (set of 3) \t $ 6.75")
    print (" 0. Quit - This ends your session and prints your final bill!")

    choice = input("\nPlease enter the products you want to buy:")              # to ask user to choose product number

    if (choice == "1"):
        print("You have chosen product 1, Shapes (Pizza flavour)")
        print("that will be $3.50")
        selecteditems = selecteditems + "\nShapes (Pizza flavour) \t $ 3.50"    # increment value of selected items with name of chosen product
        totalcost = totalcost + 3.50                                            # increment value of total cost with cost of selected item

    elif (choice == "2"):
        print("You have chosen product 2, Colgate toothpaste")
        print("that will be $7.00")
        selecteditems = selecteditems + " \nColgate toothpaste \t\t $ 7.00"
        totalcost = totalcost + 7.00

    elif (choice == "3"):
        print("You have chosen product 3, Balloons (12 pack)")
        print("that will be $1.00")
        selecteditems = selecteditems + " \nBalloons (12 pack) \t\t $ 1.00"
        totalcost = totalcost + 1.00

    elif (choice == "4"):
        print("You have chosen product 4, Red Lecture book (2B8)")
        print("that will be $2.50")
        selecteditems = selecteditems + "\nRed Lecture book (2B8) \t $ 2.50"
        totalcost = totalcost + 2.50

    elif (choice == "5"):
        print("You have chosen product 5, Vanilla scented candle")
        print("that will be $5.50")
        selecteditems = selecteditems + "\nVanilla scented candle \t $ 5.50"
        totalcost = totalcost + 5.50

    elif (choice == "6"):
        print("You have chosen product 6, AA batteries (4 pack)")
        print("that will be $10.00")
        selecteditems = selecteditems + "\nAA batteries (4 pack) \t $10.00"
        totalcost = totalcost + 10.00

    elif (choice == "7"):
        print("You have chosen product 7, Panadol (pack of 12)")
        print("that will be $12.50")
        selecteditems = selecteditems + "\nPanadol (pack of 12) \t $12.50"
        totalcost = totalcost + 12.50

    elif (choice == "8"):
        print("You have chosen product 8, Bananas (bunch of 3)")
        print("that will be $5.50")
        selecteditems = selecteditems + "\nBananas (bunch of 3) \t $ 5.50"
        totalcost = totalcost + 5.50

    elif (choice == "9"):
        print("You have chosen product 9, Sudocrem 10g net")
        print("that will be $18.50")
        selecteditems = selecteditems + "\nSudocrem 10g net \t\t $18.50"
        totalcost = totalcost + 18.50

    elif (choice == "10"):
        print("You have chosen product 10, Black pens (set of 3)")
        print("that will be $6.75")
        selecteditems = selecteditems + "\nBlack pens (set of 3) \t $ 6.75"
        totalcost = totalcost + 6.75

    elif (choice == "0"):
        quitshop = True                                                         # used to change quitshop to True to exit loop

    else:                                                                       # used to ensure valid input only are available
        print("Wrong choice!")

    print ("\nYou have spent this much so far: " + "$%0.2f" %(totalcost))       # $%0.2f to display total cost with $ sign and 2 decimal points


print ("\n"*10)
print ("Thank you for shopping with us!")
print ("Below is your cart inventory")
print ("Selected Items: " + selecteditems)
print ("")
print ("Total Cost:\t\t\t\t " + "$%0.2f" %(totalcost))                          # $%0.2f to display total cost with $ sign and 2 decimal points










# This is the end of the program
# Francois Mindiel ID 2804582
# This work is protected by copyright laws!