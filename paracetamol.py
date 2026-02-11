age = int(input("What is your age? ")) and weight = float(input("What is your weight? "))

if age >= 12 and age < 130 and weight > 0 or weight <= 100:
    print("Take 2 500mg tablets.")
elif age > 0 and age < 130 and weight > 0 and weight < 200:
    print(f"Recommended dosage is {weight*10} milligrams.")
else:
    print("Age/weight is impossible.")
