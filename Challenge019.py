#----------* CHALLENGE 19 *----------
#Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”, if they enter a 2, display
#“Well done”, if they enter a 3, display “Correct”. If they enter anything else, display “Error message”.

answer = int(input("Enter 1, 2 or 3: "))

if answer == 1:
    print("Thank you.")
elif answer == 2:
    print("Well done.")
elif answer == 3:
    print("Correct.")
else:
    print("Error message.")