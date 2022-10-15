from random import randint


def calc_groups_size1(n_customers: int) -> dict[int, int]:
    """Function counts the number of customers in each group if the ID
    numbering is continuous and starts from 0.

    :param n_customers: numbers of customers.
    :return: conatians groups as keys and number of clients as values.
    """

    result = {}

    for id_ in range(n_customers):
        group = _sum_digits(id_)
        if group in result.keys():
            result[group] += 1
        else:
            result[group] = 1

    return result


def calc_groups_size2(n_customers: int, n_first_id: int) -> dict[int, int]:
    """Function counts the number of customers in each group if the ID
    numbering is continuous and starts from random number.

    :param n_customers: numbers of customers.
    :param n_first_id: first digit in the sequence.
    :return: conatians groups as keys and number of clients as values.
    """

    result = {}

    for id_part in range(n_customers):
        id_ = _add_digit_to_left(n_first_id, id_part)
        group = _sum_digits(id_)
        if group in result.keys():
            result[group] += 1
        else:
            result[group] = 1

    return result


def _sum_digits(number: int) -> int:
    """Function calculates the sum of the digits of a number."""

    result = 0
    while number:
        result += number % 10
        number //= 10
    return result


def _add_digit_to_left(digit: int, number: int) -> int:
    """Function adds digit to the left side of the input number.

    :param digit: single digit.
    :param number: number to modify.
    :return: modified number.
    """

    dozens = 1
    while dozens <= number:
        dozens *= 10
    return dozens*digit + number


def main():
    # Test cases.
    print('Grouping functions tast cases.\n')
    for i in range(1, 11):
        print(f'Case number - {i}.')
        print('-'*50)

        n_customers1 = randint(0, 9999999)
        groups1 = calc_groups_size1(n_customers1)
        print(f'First grouping method: n_customers - {n_customers1}')
        print('Group number   |   customers count.')
        for key, value in groups1.items():
            print(f'{key}         :   {value}')
        print()

        n_customers2 = randint(0, 999999)
        n_first_id = randint(0, 9)
        groups2 = calc_groups_size2(n_customers2, n_first_id)
        print(f'Second grouping method: n_customers - {n_customers2}, '
              f'n_first_id - {n_first_id}.')
        print('Group number   |   customers count.')
        for key, value in groups2.items():
            print(f'{key}         :   {value}')
        print()


if __name__ == '__main__':
    main()

