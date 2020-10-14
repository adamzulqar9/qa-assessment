
def error_msg(expected, actual):
    """
    Assertion error message
    :param expected: expected value
    :param actual: actual value
    :return: error message with expected and actual value
    """
    return "FAIL!\nExpected: {}\nActual: {}\n".format(expected, actual)


def list_to_string(list_of_number):
    """
    Joins list to form a string
    :param list_of_number: number list
    :return:
    """
    string = ""
    return string.join(list_of_number)


def prepare_expected_value(number, op):
    """
    Prepares expected value to be used for assertion, adding "space" to conform to calculator output format
    :param number: input number
    :param op: input operator
    :return: processed expected value in str
    """
    # FIXME: workaround
    if op == 'divide' or op == '/':
        return number
    else:
        number = convert_to_list(number)
        expected_value = []
        number = number[::-1]
        for iterate, value in enumerate(number):
            if iterate % 3 == 0 and iterate != 0:
                expected_value.insert(iterate, '{} '.format(value))
            else:
                expected_value.insert(iterate, value)

        expected_value = expected_value[::-1]
        # TODO: implement
        # if len(expected_value) > 9:
        # raise NotImplementedError

        return list_to_string(expected_value)


def pre_process(number):
    """
    Converts number into either integer or float
    :param number: input number
    :return: converted number in str format
    """
    try:
        number = int(number)
    except (TypeError, ValueError):
        number = round(float(number), 6)
        return str(number)
    else:
        return str(number)


def calculate(first, second, op):
    """
    Performs calculation based on user input number and operator
    :param first: user input first number
    :param second: user input second number
    :param op: user input operator
    :return: calculated value in string
    """
    first = int(first)
    second = int(second)
    if op == 'add' or op == '+':
        value = first + second
        return str(value)
    elif op == 'subtract' or op == '-':
        value = first - second
        return str(value)
    elif op == 'multiply' or op == '*':
        value = first * second
        return str(value)
    elif op == 'divide' or op == '/':
        value = first / second
        return str(value)
    else:
        print('Invalid arithmetic operator, accepted operators are: + - * /')
        exit(1)


def convert_to_list(number):
    """
    Convert input numbers to list
    :param number: input number
    :return: list
    """
    number_list = list(number)
    return number_list


def check_valid_number(number_list):
    """
    Verifies that entered number is a digit
    :param number_list: list of number
    :return: True or False
    """
    for number in number_list:
        if not number.isdigit():
            return False
        else:
            pass
    return True


def validate_number(number):
    """
    Validates that the input numbers are within the max range and is valid
    :param number: list of numbers
    :return: True or False
    """
    if len(number) > 9 or not check_valid_number(number):
        number = list_to_string(number)
        print('You entered invalid number, please enter maximum of 9 valid integer digits\nYou entered {}'.format(
            number))
        return False
    else:
        return True
