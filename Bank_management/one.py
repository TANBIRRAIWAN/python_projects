balance = 5000
account = 12345

print(f"\n\n=====Welcome To Basic Bank =====")
pin = int(input("Enter Your Pin Number = "))

if pin == account:
    while True:

        print("****Welcome Dear Customer *****\n")
        print(f"\t\t1. Check Your Current Balance  ")
        print(f"\t\t2. Withdraw Your Money ")
        print(f"\t\t3. Deposit Money To Your Account ")
        print(f"\t\t4. Transfer balance to another account ")
        print(f"\t\t5. Exit.\n\n ")

        choice = int(input("Enter Your Choice = "))

        if choice == 1:
          
          print(f"Your Current Balance is {balance}")

        elif choice ==2:
          amount = int(input("Enter Withdraw Amount = "))
          if amount < balance:
             balance -= amount
             print(f"You Have withdraw {amount} Taka.\n Your Current Balance is {balance} TAka")

          else:
             print(f"You Do not have Enough balance to withdraw!!\n Your Balance is {balance} Taka.")

        elif choice ==3 :
          deposit = int(input("Enter Your Deposit Balance = "))
          pbalance = balance
          balance += deposit
          print(f"you Have Deposited {deposit} Taka Successfully !!")
          print(f"Your Balance was {pbalance} Taka.")
          print(f"Current Balance is {balance} Taka.")        
        


        elif choice == 4:
          taccount = int(input("Enter Transfer Account = "))
          tbalance = int(input("How much would you like to transfer = "))
          pin = int(input("Enter Your Pin Number = "))

          if pin == account:
              if tbalance < balance :
                  print(f"You have successfully transfered {tbalance} Taka to Account num is {taccount}\n")
                  print(f"After Transfer Your Current Balance is {balance - tbalance} Taka.")

              else:
                  print("Sorry !! You Transfer More Than Your Balance .!! Try Again !!")

          else:
             print("Your Pin is Incorrect !! Sorry !!")

        elif choice == 5 :
           break


        else:
          print("You Have pressed Invalid Number !!")

    
else:
    print("Sorry Your Password is Wrong !! Try Again later!!")

