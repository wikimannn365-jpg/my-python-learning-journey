with open("myfamily.csv", "r") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} curently resides in {row[1]}")