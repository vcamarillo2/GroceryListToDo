# To-Do List: Grocery Shopping PT 2
# 1/12/24
#Viri
# Initialize
list = []

# Functions
# Welcomes the user to the automated list
def intro(): 
    print ("Getting hungry? It's time to go to the store!")
    print(" MENU: 1. Add a item\n 2. View current list\n 3. Mark as completed\n 4. Remove item\n 5. Exit\n 6. Clear the list\n 7. Sort list alphabetically\n 8. Returns number of items in your list\n ")
# Presents user with options via a menu
def menu():
    option = int(input("Please select one of the 5 options in the MENU (1-5): "))
    if option == 1:
        answer = input("What do you want to add to the list?")
        list.append(answer)
        menu()
    if option == 2:
        print(list)
        menu()
    if option == 3:
        ans=input("What item do you want to mark as gathered?: ")
        i= list.index(ans)
        Number= list[i]
        list[i]=("☒"  + Number)
        menu()
    if option == 4:
        remove = int(input("What item do you want to remove? Enter 0 for the first item, 1 for the second..etc.: "))
        list.pop(remove)
        menu()
    if option == 5:
        print("Thank you for using our list automator!")
        exit()
    if option==6:
        list.clear()
        print("Done!")
        menu()
    if option==7:
        list.sort()
        print("Finished!")
        menu() 
    if option==8:
        print(len(list))
    else:
        print("Error. You entered a wrong input, try again")
        menu()
# Runs the other functions together
def grocerylist():
    intro()
    menu()

# Main
grocerylist()