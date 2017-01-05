# Fizz Buzz application
# Every number divisible by 3 should be labeled 'Fizz'
# Every number divisible by 5 should be labeled 'Buzz'
# Every number divisible by 3 AND 5 should be labeled 'Fizz Buzz'
import sys

print("The name of this script is {}".format(sys.argv[0]))
print("User supplied {} arguments at runtime".format(len(sys.argv)))


if len(sys.argv) == 2:
    n = int(sys.argv[1])
else:
    while True:
        try:
            n = int(input("enter a counter value > "))
            break
        except ValueError:
            print("Please enter in a number instead")
        
counter = 0
while counter < n:
    counter += 1
    fizz = counter / 3
    buzz = counter / 5
    fizz_buzz = counter / 3 /5
    if fizz_buzz == int(fizz_buzz):
        print('fizz_buzz')
    elif  fizz == int(fizz):
        print('fizz')
    elif buzz == int(buzz):
        print('buzz')
    else:
        print(counter)