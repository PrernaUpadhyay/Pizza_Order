#Pizza order
print("Welcome to Python Pizza Deliversies!")
size=input("What size pizza do you want ? S,M or L:")
toppings=input("Do you want toppings on your pizza?Yor N:")
extra_cheese=input("Do you want extra cheese ?Y or N:")

#Size of the pizza
bill=0
if size=="S":
    bill +=15
elif size=="M":
    bill +=20
elif size=="L":
    bill+=25
else:
    print("You typed the wrong inputs")

#toppings
if toppings =="Y":
    if size =="S":
        bill +=2
    else:
        bill+=3

#cheese
if extra_cheese=="Y":
    bill +=1

print(f"Your final bill is:{bill}.")

