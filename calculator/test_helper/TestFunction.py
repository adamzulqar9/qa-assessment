from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.common.by as by
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as ec
import calculator.config as config


def click_pos(driver, coordinates):
    """
    Click on specified position on browser
    :param driver:
    :param coordinates:
    :return:
    """
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(driver.find_element_by_tag_name('body'), 0, 0)
    # wait_for_clickable_element(driver)
    actions.move_by_offset(coordinates[0], coordinates[1]).click().perform()


def wait_for_clickable_element(driver):
    """
    Waits for specified element to become clickable
    :param driver: driver obj
    :return: None
    """
    delay = 5
    try:
        ui.WebDriverWait(driver, delay).until(ec.element_to_be_clickable((by.By.XPATH, config.canvas_xpath)))
    except TimeoutError:
        print('Error: Element not click-able after {} seconds'.format(delay))
