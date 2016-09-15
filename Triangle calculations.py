def is_triangle(a, b, c):
    if a > b + c:
        print("NO")
    if b > a + c:
        print("NO")
    if c > a + b:
        print("NO")
    else:
        print("Yes")


is_triangle(input("Enter a number: \n"), input("Enter a number: \n"), input("Enter a number: \n"))
