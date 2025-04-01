def find_minimum_notes(amount):   
    notes_100=amount//100
    amount%=100
    # remaining amount afetr 100
    notes_50=amount//50
    amount%=50
    #remaining amount after 50
    notes_10=amount//10
    amount%=10
    #ammout after 10
    if amount!=0:
        print("Enter amount multiple of 10: ")
    else:
        notes_100 != 0 and print(f"Number of 100 rs notes is: {notes_100}")
        notes_50 != 0 and print(f"Number of 50 rs notes is: {notes_50}")
        notes_10 != 0 and print(f"Number of 10 rs notes is: {notes_10}")    
    
    

input_amount=int(input("Enter Amount: "))
find_minimum_notes(input_amount)