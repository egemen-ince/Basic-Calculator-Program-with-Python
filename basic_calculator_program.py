print("""****************
CALCULATOR PROGRAM

1. Addition process

2. Extraction process

3. Multiplication process

4. Division process

****************""")


a = int(input("First number:  "))
b = int(input("Second number:  "))


işlem = input("Select transaction type: ")


if işlem == "1":
    print("{} + {} = {}".format(a,b,a+b))
elif işlem == "2":
    print("{} - {} = {}".format(a,b,a-b))
elif işlem == "3":
    print("{} * {} = {}".format(a,b,a*b))
elif işlem == "4":
    print("{} / {} = {}".format(a,b,a/b))
else:
    print("Invalid operation.")