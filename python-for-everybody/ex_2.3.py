# print("Hello World!")


hrs = input("Enter Hours:")
h = float(hrs)
rate = input("enter Rate:")
r = float(rate)
if (h) <= 40:
    print("Pay:", h * r)
elif (h) > 40:
    print(40 * r + (h - 40) * 1.5 * r)
