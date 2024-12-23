def bigestNumber(numbers):
    # variable None can also be used intead 0. "None is also a flag value, is just usede at the biggining of the loop."
    lg_number = numbers[0]

    for num in numbers:
        if num < lg_number:
            lg_number = num
    return lg_number


# To call the funtion
print(bigestNumber([374, 3647, 65748, 647546, 2, 4, 857]))

tot = 0
for i in [5, 4, 3, 2, 1]:
    tot = tot + 1
print(tot)

zork = 0
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
print('After', zork)

if smallest is None:
    smallest = value
