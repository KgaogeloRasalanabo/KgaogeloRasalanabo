# get seven unique random numbers from 1 through 50. display six lucky numbers and last number as bonus
import random


def number_generator(six_numbers):
    i = 0
    for num in six_numbers:
        if i < len(six_numbers):
            print(six_numbers[i], end=", ")
            i += 1


if __name__ == "__main__":
    # seven unique random numbers from 1 through 50
    seven_numbers = random.sample(range(1, 51), 7)

    # six numbers
    print("LUCKY NUMBERS: ", end=" ")
    number_generator(seven_numbers[0:6])

    # bonus number
    print('\n'"BONUS: ", seven_numbers[6])
