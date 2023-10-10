""" Print the sum of all the numbers from 1-15 """
def sum_of_range(with_built_in):
    # With built in methods (using range, and sum)
    if with_built_in:
        print(sum(range(1,16)))

    # Without built in methods
    else:
        x = 1
        x_sum = 0
        while x < 16:
            x_sum += x
            x += 1
        print(x_sum)
# sum_of_range(True)
# sum_of_range(False)



""" Use a for loop to count from 1-100. For every number that is odd print “FIZZ” for every number that is even print “BUZZ” """
def fizz_buzz(with_built_in):
    # With built in methods (using range)
    if with_built_in:
        for x in range(1,101):
            print("BUZZ") if x % 2 == 0 else print("FIZZ")  

    # Without built in methods
    else:
        i = 1
        x_li = [None] * 100
        for x in x_li:
            print("BUZZ") if i % 2 == 0 else print("FIZZ")
            i += 1
# fizz_buzz(True)
# fizz_buzz(False)


""" Create a list variable with 5 numbers and find the minimum, maximum and average of all those numbers. Then print them out. """
def min_max_average(with_built_in):
    sample_li = [2,7,3,1,9]
    # With built in methods (min, max, sum, len)
    if with_built_in:
        print(f"Min: {min(sample_li)} Max: {max(sample_li)} Average: {sum(sample_li)/len(sample_li)}")

    # Without built in methods
    else:
        x_min = None
        x_max = None
        x_sum = 0
        x_len = 0
        for x in sample_li:
            if x_min == None:
                x_min = x
                x_max = x
            if x < x_min:
                x_min = x
            if x > x_max:
                x_max = x
            x_sum += x
            x_len += 1
        print(f"Min: {x_min} Max: {x_max} Average: {x_sum/x_len}")
# min_max_average(True)
# min_max_average(False)