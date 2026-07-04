#ATM Simulator 

pin_verification=int(input("Create a pin-->"))

transactions=[]
balance=500
while True:
    print("\n====== ATM SIMULATOR ======")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")
    
    choice=int(input("\nEnter your choice:"))
    
    if choice==1:
        print(f"\nCurrent Balance:₹{balance}")
        
    elif choice==2:
        print("\n===Deposit Money===")
        amount=int(input("\nEnter amount to deposit:"))
        balance+=amount
        transactions.append(f"Deposited ₹{amount}")
        print(f"\n₹{amount} deposited Successfully!")
        print(f"Current Balance:₹{balance}")
        
    elif choice==3:
        print("\n===Withdraw Money===")
        
        pin=int(input("\nEnter PIN-->"))
        if pin!=pin_verification:
            print("\nIncorrect pin!!")
            print("\nTry Again!")
            continue
            
        else:
            print("\nDone👍")
            
        amount=int(input("\nEnter your amount:"))
        if amount<=balance:
            balance-=amount
            transactions.append(f"Withdraw ₹{amount}")
            print(f"\n₹{amount} withdrawn successfully!")
            print(f"Current Balance:₹{balance}")
        else:
            print("\n==Insufficient Balance==")
            
    elif choice==4:
        print("\n===Transaction History===")
        if len(transactions)==0:
            print("\nNo Transactions yet!")
        else:
            for transaction in transactions:
                print(transaction)
            
    elif choice==5:
        print("\nThank you for using the ATM!")
        break
    
    else:
        print("\nInvalid choice!!")
        