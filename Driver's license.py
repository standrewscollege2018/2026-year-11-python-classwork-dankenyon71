'''This programs stores the data of student drivers and allows user to change their data'''

names = ["Maximillian", "Katherine", "Dan", "Brian", "Mickey"]
licenses = ["No license", "No license", "No license", "No license", "No license"]
changing = None
newlicense = None

while changing != 0:
    print("Student driver status")
    print("=====================")
    for i in range(len(names)):
        print(f"{i+1}. {names[i]:15} {licenses[i]:}")
        changing = None
    while changing == None:
        try:
            changing = int(input("Select student to update (0 to quit): "))
        except ValueError:
            print("Invalid Value.")
            changing = None
        if changing != 0 and changing < (len(names)+1) and changing >= 1:
            newlicense = input("Enter new status (No license, Learners, Restricted, Full): ")
            if newlicense == "No license" or newlicense == "Learners" or newlicense == "Restricted" or newlicense == "Full":
                licenses[changing-1] = newlicense
            else:
                print("Invalid license type.")
                changing = None
        elif changing > (len(names)) or changing < 0:
            print("Invalid student.")
            changing = None