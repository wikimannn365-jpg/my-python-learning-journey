name = input("What's your name: ").strip().capitalize()
location = input("where do you currently reside in: ").strip().capitalize()
with open("myfamily.csv", "a") as file:
    file.write(f"{name},{location}\n")