def bigestNumber(numbers):
    # variable None can also be used intead 0. "None is also a flag value, is just usede at the biggining of the loop."
    lg_number = numbers[0]

    for num in numbers:
        if num < lg_number:
            lg_number = num
    return lg_number


# To call the funtion
print(bigestNumber([374, 3647, 65748, 647546, 2, 4, 857]))
