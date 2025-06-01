def task1(): # The idea to devide code by functions was discovered with the use of AI
    a = "Hello, Python World!"
    print(a)  

def task2():
    var1, var2 = map(int, input().split())
    print(f"Sum: {var1+var2}")
    print(f"-operation: {var1-var2}")
    print(f"product: {var1*var2}")
    print(f"Quotient: {var1/var2}")

def task3():
    strain_1 = input()
    strain_2 = input()
    print(strain_1+strain_2, len(strain_1+strain_2))

def task4():
    x = int(input("Enter ur number to check if it is divisible by 2: "))
    if x%2==0:
        print("congrats! It is EVEN")
    else:
        print("Nah, bro. It is an ODD number")
def task5():
    for i in range (1,11):
        print(i)
def task6():
    num = int(input("Enter the nuumber: "))
    if num >0:
        print("Number is positive!")
    elif num<0:
        print("Number is negative")
    else:
        print("The number is equal to my IQ, it is exactly 0!")
def task7():
    for i in range(1,11):
        if i%2==0:
            print(i)
def task8():
    n = int(input("Enter n to count sum til n: "))
    sum = 0
    for i in range(1,n):
        sum += i
    print(sum)
def task9():
     for i in range(10, 0, -1):
         print(i)
def task10():
    for i in range(1,11):
        if i == 5:
            continue
        if i == 7:
            break
        print(i)
task10()


