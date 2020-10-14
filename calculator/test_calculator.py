import time
import calculator.test_helper.TestObject as to
import calculator.test_helper.TestFunction as tf
import calculator.test_helper.TestExtractor as te
import calculator.test_helper.TestHelper as th
import calculator.coordinates as co


def test_calculator_add():
    first = '100'
    second = '100'
    op = '+'

    first_number = th.convert_to_list(first)
    second_number = th.convert_to_list(second)

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
    print('You entered {} {} {}'.format(first, op, second))
    print('The expected Answer is: {}'.format(expected_value))

    # Close browser
    driver.close()


def test_calculator_subtract():
    first = '10'
    second = '9999'
    op = '-'

    first_number = th.convert_to_list(first)
    second_number = th.convert_to_list(second)

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
    print('You entered {} {} {}'.format(first, op, second))
    print('The expected Answer is: {}'.format(expected_value))

    # Close browser
    driver.close()


def test_calculator_multiply():
    first = '700'
    second = '30'
    op = '*'

    first_number = th.convert_to_list(first)
    second_number = th.convert_to_list(second)

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
    print('You entered {} {} {}'.format(first, op, second))
    print('The expected Answer is: {}'.format(expected_value))

    # Close browser
    driver.close()


def test_calculator_divide():
    first = '1500'
    second = '122'
    op = '/'

    first_number = th.convert_to_list(first)
    second_number = th.convert_to_list(second)

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
    print('You entered {} {} {}'.format(first, op, second))
    print('The expected Answer is: {}'.format(expected_value))

    # Close browser
    driver.close()


def test_calculator_negative():
    first = '9999999999'
    second = '1000'
    op = '-'

    first_number = th.convert_to_list(first)
    check_first_number = th.validate_number(first_number)
    error = 'Number is supposed to be invalid'
    assert not check_first_number, error

    second_number = th.convert_to_list(second)
    check_second_number = th.validate_number(second_number)
    error = 'Number is supposed to be valid'
    assert check_second_number, error

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

    error = 'Value shouldnt be the same'
    assert expected_value != actual_value, error
    print('You entered {} {} {}'.format(first, op, second))
    print('The Expected Answer is: {}'.format(expected_value))
    print('The Actual Answer is: {}'.format(actual_value))

    # Close browser
    driver.close()


def test_calculator_max_boundary():
    first = '222222222'
    second = '777777777'
    op = '+'

    first_number = th.convert_to_list(first)
    second_number = th.convert_to_list(second)

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
    print('You entered {} {} {}'.format(first, op, second))
    print('The expected Answer is: {}'.format(expected_value))

    # Close browser
    driver.close()


def test_calculator_min_boundary():
    first = '1'
    second = '1'
    op = '-'

    first_number = th.convert_to_list(first)
    second_number = th.convert_to_list(second)

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
    print('You entered {} {} {}'.format(first, op, second))
    print('The expected Answer is: {}'.format(expected_value))

    # Close browser
    driver.close()
