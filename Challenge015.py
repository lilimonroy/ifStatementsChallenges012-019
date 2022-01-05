#----------* CHALLENGE 15 *----------
#Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”, 
# otherwise display the message “I don’t like [colour], I prefer red”.

colour = input("What's your favorite colour: ")

if colour.lower() in ['red']:
    print("I like red too")
else:
    colour.lower()
    print("I don't like",colour,", I prefer red.")