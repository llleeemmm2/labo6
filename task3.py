lastNameYoungest = ""
firstNameYoungest = ""
minAge = float("inf")

lastNameOldest = ""
firstNameOldest = ""
maxAge = float("-inf")

with open("deti.txt", "r", encoding='utf-8') as file:
    for line in file:
        lastName, firstName, age = line.strip().split()
        age = int(age)

        if age < minAge:
            minAge = age
            lastNameYoungest = lastName
            firstNameYoungest = firstName

        if age > maxAge:
            maxAge = age
            lastNameOldest = lastName
            firstNameOldest = firstName

with open("youngest.txt", "w", encoding='utf-8') as file:
    file.write(f"Младший ребенок: {lastNameYoungest} {firstNameYoungest} {minAge}")

with open("oldest.txt", "w", encoding='utf-8') as file:
    file.write(f"Старший ребенок: {lastNameOldest} {firstNameOldest} {maxAge}")