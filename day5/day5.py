from day5_data import day5_data_input as data_input
import re

# Question: What is the highest seat ID in the list
# Seat ID = row number * 8 + column number

# Solution: The binary representation of the combined seat and column numbers give the unique seat ID. For example
# for seat BFFFBBFRRR -> 1000110111 -> 567 which is the seat ID. With component values 1000110 -> row: 70 and 111 -> col: 7.
# Map all characters to a binary and compute values.

seat_match = {
    "B": 1,
    "F": 0,
    "L": 0,
    "R": 1
}


def max_seat_id(data_list: list, dict_input: dict):

    # Part 1: Find the maximum seat ID.
    seats = data_list
    converted_list = []
    for seat in seats:
        x = [dict_input[i] for i in seat]
        x = int("".join(map(str, x)), 2)
        converted_list.append(x)
    max_id = max(converted_list)
    print(f"The maximum seat ID is: {max_id} ")

    # Part 2: Find my seat by looking for the missing seat ID
    converted_list = sorted(converted_list)
    missing_num = set(
        range(converted_list[0], converted_list[-1]+1)).difference(converted_list)
    print(f"My seat ID is: {missing_num} ")


max_seat_id(data_input, seat_match)
