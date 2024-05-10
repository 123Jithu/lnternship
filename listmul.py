def list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

my_list = [7, 8, 4, 5]
print("Multipy:", list(my_list))
