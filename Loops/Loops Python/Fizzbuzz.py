# Jackson Clark, FizzBuzz Python

x = 0
for x in range(51):
    i = x%3
    e = x%5
    if i+e==0:
        print("FizzBuzz")
    elif i==0:
        print("Fizz")
    elif e==0:
        print("Buzz")
    else:
        print(x)
    
