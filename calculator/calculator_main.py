import time
import calculator.test_helper.TestObject as to
import calculator.test_helper.TestFunction as tf
import calculator.test_helper.TestExtractor as te
import calculator.test_helper.TestHelper as th
import calculator.coordinates as co


def main():
    first = str(input("Please enter first number: "))
    first_number = th.convert_to_list(first)
    check_first_number = th.validate_number(first_number)
    if not check_first_number:
        exit(1)
    second = str(input("Please enter second number: "))
    second_number = th.convert_to_list(second)
    check_second_number = th.validate_number(second_number)
    if not check_second_number:
        exit(1)
    op = str(input("Please enter operator type (e.g. add, subtract, multiply, divide): "))

    value = th.calculate(first, second, op)
    expected_value = th.pre_process(value)
    expected_value = th.prepare_expected_value(expected_value, op)

    driver = to.TestObject()
    driver = driver.start()

    # Click first number
    for number in first_number:
        tf.click_pos(driver, co.num[number])

    # Click arithmetic operator
    tf.click_pos(driver, co.operator[op])

    # Click second number
    for number in second_number:
        tf.click_pos(driver, co.num[number])

    # Click equal
    tf.click_pos(driver, co.equal)

    time.sleep(1)
    actual_value = te.extract_value()

    assert expected_value == actual_value, th.error_msg(expected_value, actual_value)
    print('The expected Answer is: {}'.format(expected_value))


if __name__ == '__main__':
    main()
