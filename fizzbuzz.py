def fizzbuzz(num):
    array = list(range(1, num+1))
    for index in range(len(array)):
        if array[index] % 15 == 0:
            array[index] = "Fizzbuzz"
        elif array[index] % 3 == 0:
            array[index] = "Fizz"
        elif array[index] % 5 == 0:
            array[index] = "Buzz"
    return array


# define FIZZBUZZ function, takes NUM as argument
# create an empty ARRAY of length NUM
# fill ARRAY with range of NUM
# loop through the ARRAY
# if current_num is a multiple of 3, replace with fizz
# if current_num is a multiple of 5, replace with buzz
# if current_num is a multiple of both, replace with fizzbuzz
# return ARRAY