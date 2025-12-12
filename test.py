age = int(input("Enter your age:"))
if age >= 18:
    print("You can watch any movie(including Adult-rated)")
elif age >= 13 and age < 18:
    print("You can watch movies rated PG-13 and lower-rated movies.")
elif age >= 7 and age < 13:
    print("You can watch G and PG-rated movies.")
elif age < 7:
    print("You should watch only G-rated(General Audience) movies.")
    

