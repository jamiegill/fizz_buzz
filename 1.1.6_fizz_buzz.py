# Fizz Buzz application
# Every number divisible by 3 should be labeled 'Fizz'
# Every number divisible by 5 should be labeled 'Buzz'
# Every number divisible by 3 AND 5 should be labeled 'Fizz Buzz'
n = 100
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