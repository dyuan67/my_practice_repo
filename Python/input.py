'''
name = input("Please ener your name: ")
    # Prompts the user to enter name
    # When they do, it will be stored in variable name
print("Hello, " + name)
#The , will just naturally add a space
# For print statements with numbers, use a , instead of + (will be error)

num = input("Enter a number: ")
print(num)
double = num*2
print(double)
    # This will output 55 because thinks the number is a string
num2 = int(input("Enter a number: ")) # Cast into an int or float
    # Must enter a number because we are casting it as an int
    # If we were treating a string as an int will also cause error
double2 = num2*2
print(double2)

try: # If want user to keep entering a number until correct, use a while loop and boolean
    num = int(input("Enter a number: "))
    print(num)
    double = num*2
    print(double)
except:
    print("You didn't enter a number")

print('The rain in Spain', end = " ") # Does not print next statement into the next line
print("stays mainly in the plain.")

'''

with open("movies.txt") as file:
    for line in file:
        #line = line.strip()
        print(line.strip()) #Normally there is a blank print line in between each,
            # doing the strip gets rid of the extra line

with open("heights.txt") as file:
    for line in file: #Iterates through each line
        info = line.strip().split() #Splits each element in line by spaces
        # Info will be a list with these elements: [Thomas, Jones, 70] for each line
        print(info)
        info[2] = int(info[2])
        print(info)


file_name = input("Enter a file name: ")
#Could have also done it with enumerate
with open(file_name) as file:
    count = 1
    for line in file:
        print(str(count) + ". " + line.strip())
        count+=1