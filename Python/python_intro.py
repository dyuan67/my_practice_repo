print("Hello, World!") 
#There is no difference between "x" and 'x' in Python
    #Just follow Java "Double quotes for strings" and 'single quotes for chars'
        #But really does not matter
# fast easy comment
'or use single quotes'
'''
use this to make a few lines
of comments.

'''

# No need to assign type
x = 100
x = "hello"
x = [1, 2, 3]
print(x)

x = 100
y = 10
# Using x/y will result in a float (10.0)
# But if // (Floor division) it will chop off the decimal end (6.8 becomes 6) *Only if both are integers
results = x//y
print(results)
print(int(x/y)) # Cast it into an integer

# Naming convension: all lowercase, separated by _
min_value = min(1, 2, 3)
print(min_value)

raised = pow(2, 3)
print(raised)
raised = 2**3   # Also 2^3
print(raised)

x = 1
y = 0
if x<0:
    print("x is negative")
elif x>0:
    print("x is positive")
else:
    print("x is zero")

start = 10
end = 100
# Instead of && and ||, write out and and for
if x > start and x < end:
    print("x is within range")
if x < start or x > end:
    print("x is not in range")

''' Can split the if statment into two lines using parenthesis 
z = 0
if (z == 0 //To have equality it must be ==, not just = (that is equal to, which does not work)
    and x == 1):
    print("fine")

'''

count = 0
# If accidently infinite loop, command + c will stop
while count < 5:
    print(count)
    count = count + 1
    # count+ = 1

# for (int i = 0; i < 5; i++)
for i in range(5): #by default the loop starts at 0
    # print(i) each number is a new line
    print(i, end = " ")
print() # prints next stuff on a new line

#range(1, 5) == starts at 1, ends at 4 (non-inclusive)
for i in range (1, 5):
    print(i, end = " ")
print()

#range(1, 15, 2) == Starts at 1, end at 14 (15 non-inclusive), and adds 2 (intervals)
for i in range (1, 15, 2):
    print(i, end = " ")
print()

lst = [2, 4, 6, 8]
for i in range(len(lst)):
    print(i, lst[i])
        # will print 1st variable space then next variable
        # len(lst) is length of list
        # still where the index of the value is one less because starts at 0

# the variable name can be anything, no need to be labled val or i
for val in lst:
    print(val, end = " ")
        # For loop for lists, where it stores the component of the list into val
for i, val in enumerate(lst):
    print(i, val)
        # i is the index value, and still stores value of lst in val
print()


print("Practice")
# Exercise 1
for i in range (1, 21):
    if i % 3 == 0:
        print(i,  end = " ")
print()

# Exercise 2
sum = 0
count = 1
while count < 51:
    if count % 2 == 0:
        sum = count + sum
        count+= 1
    else:
        count+= 1
print(sum)

# Exercise 3
numbers = [5, 8, 2, 15, 10, 3, 7]
# for i, num in enumerate(numbers):
#     if numbers[i] > 5:
#         print(num, end = " ")
for num in numbers:
    if num > 5:
        print(num, end = " ")
print()

# Exercise 4
lst1 = [1, 2, 3, 4, 5,]
lst2 = []
lst2.append(lst1[0])
    #list.append is adding elements to the lst
for i in range(len(lst1)):
    lst2.append(lst2[i - 1] + lst1[i])
print(lst2)


def hello_world():
    print("Hello, World!")
hello_world()

def hello(name):
    print("Hello, " + name)
def hello2(name = "Bob"):
    print("Hello, ", name)

print()
#Exercise 5
def swap(lst):
    i = len(lst)
    one = lst[0]
    lst[0] = lst[i-1]
    lst[i-1] = one
    print(lst)
lst = [0, 3, 8, 4, 5]
swap(lst)

hello = "hello"
for c in hello:
    print(c)

course = "Platform computing"
course[start:end]
plat = course[0 : 8] #[: 8] default start at 0
comp = course[9:] # default end at 9
print(plat)
print(comp)


