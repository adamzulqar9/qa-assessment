# Silly Calculator
**- How it works?**

Program will take inputs from user, opens a browser and key in the inputs from the user into the calculator. After calculation is done, it will display the answer to the user

Run using: `python3 calculator_main.py`

--------

**- Testing calculator functions**

Program will run a series of tests on the online calculator. It will input predefined numbers and operators and test it against an expected answer. After all tests has been executed, a report will be generated and displayed to user via a HTML reporting page

Run test using: `pytest -k calculator --html=report.html`

--------

**- Tools Used:**

1. Selenium webdriver: Used to open browser, perform actions on online calculator
2. pyautogui: Used to capture image on the ROI (region of interest)
3. cv2, numpy: Used to pre-process image captured
4. pytesseract: Used to perform extraction of data from the captured image into string
5. pytest: Used as test framework and for test reporting
