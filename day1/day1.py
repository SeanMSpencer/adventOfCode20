from day1_data import input_data
from itertools import combinations

# ----- PART 1 -----


def search_sum_manual(data):
    """
    search_sum takes a list of numeric data and returns two values that sum to target_sum and returns the product of those values.
    """

    # value the two numbers need to sum too
    target_sum = 2020

    for i, n in enumerate(data[:-1]):
        # take each value of the list and find the compliment value
        complement = target_sum - n

        # check if the complement is in the list, search i+1 slice to cut down on computation load
        if (complement in data[i+1:]):
            number = n
            product = number * complement
            print("This is the manual solution:")
            print("A Solution has been identified: {} and {}".format(
                number, complement))
            print("The product of these values is: {}".format(product))
            break
    else:
        print("No Solution has been found.")


def search_sum_iter(data):
    """
    This function takes a list of numerical data and returns the pair of values in the list that sum to the target value and the subsequent product of that pair.
    """
    target_sum = 2020

    combination_list = combinations(data, 2)

    for pairs in combination_list:
        if sum(pairs) == target_sum:
            solution = pairs[0] * pairs[1]
            print("This is the itertools solution:")
            print("A solution has been identified: {}".format(pairs))
            print("The product of these values is: {}".format(solution))

# ----- PART 2 -----


def search_prod_iter(data):
    """
    This function finds a tuple of 3 values that sum to the target value and returns their product.
    """
    target_sum = 2020

    combination_list = combinations(data, 3)

    for pairs in combination_list:
        if sum(pairs) == target_sum:
            solution = pairs[0] * pairs[1] * pairs[2]
            print("This is the itertools triple solution:")
            print("A solution has been identified: {}".format(pairs))
            print("The product of these values is: {}".format(solution))


# search_sum_manual(input_data)
# search_sum_iter(input_data)

search_prod_iter(input_data)
