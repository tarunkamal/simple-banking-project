balance = 1000
correct_pin = 1234
a=int(input("Enter the PIN."))
if a!=1234 :
      print("Invalid PIN!")
      exit()

print("\nPIN accepted. Welcome to our Bank!")      

while True :
    
    print("\t----MAIN MENU----")
    print("Current Balance :", balance)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    
    choice=int(input("enter the choice :"))    
   
   
    if choice == 1:
       amount=int(input("Enter the amount to be deposited :"))
       balance = balance + amount
       print("Congrats!", amount, "successfully deposited!")

    elif choice == 2 :
       amount=int(input("Enter the amount to be withdrawn :"))
       if amount > balance :
           print("Transaction denied!! Insufficinent funds.")
       else :
           balance = balance - amount
           print("Congrats!", amount, "successfully withdrawn!")

    elif choice == 3:
        print("Your current balance is :", balance)

    elif choice == 4 :
        print("Thank you for using our service. Goodbye!!")
        break

    else :
        print("Invalid choice!! Choose between 1-4")
      


      
