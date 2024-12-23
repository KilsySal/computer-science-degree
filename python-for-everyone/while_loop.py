name = input("Enter you name: ")
while name == " ":
    print("Enter a valid name.")
    name = input("Enter you name:")
print(f"Hello {name}")
# 'f' alow to add a funtion inside a string
age = int(input("Enter you age: "))
while age < 0:
    print("Enter a valid age.")
    age = int(input("Enter you age: "))
print(f"{age} is grate. You can prosead.")

lang = input("What languaje are you cunrrently learning? ")
while not lang == "spanish":
    print("It has to be an specific language.")
    lang = input("What languaje are you cunrrently learning? ")
print(f"Welcome {name} you are {age} and learning {lang}.")
