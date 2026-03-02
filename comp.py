'''This program looks through a randomly generated list to find 2 adjacent numbers that sum to the input'''

search = 0
list = (1,2,3,4) # set the list of numbers

search = int(input("Enter input: ")) # enter number to look for numbers that sum to
found = False # Unless a number is found later a failure message will be printed

# Following code checks each number in the list for if there is a number after it in the list that adds to the input
for n1 in range(1,len(list)):
    searchnum = search - list[n1]
    for n2 in range(n1,len(list)):
        if list[n2] == searchnum and n1 != n2:
            print(f"{list[n1]}, {list[n2]} sum to {list[n1]+list[n2]}")
            found = True

if found == False:
    print(f"Numbers that sum to {search} not found.") # If we don't find two numbers that sum to the input, we return a failure message