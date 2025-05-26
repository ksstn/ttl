# number 1. rental car
car = input("\nWhat kind of rental car would you like?\n")
print (f"Let me see if I can find you a {car}.\n")

# number 2. restaurant seating
seats = input("How many people are in their dinner group?\n")
seats = int(seats)
if seats > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")
    #TRY LANG ITO

# number 3. pizza toppings
prompt = "\nEnter a pizza topping that you like:"
prompt += "\nEnter 'quit' if you want to finish the program.\n"
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f"\nI'll add '{message}' to your pizza.")

