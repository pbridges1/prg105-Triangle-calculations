def is_triangle(a, b, c):
    if a > b + c:
        print("NO")
    elif b > a + c:
        print("NO")
    elif c > a + b:
        print("NO")
    else:
        print("Yes")


is_triangle(input("Enter a number: \n"), input("Enter a number: \n"), input("Enter a number: \n"))
