class calculator:
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.button_0 = '//*[text()="0"]'
        self.button_1 = '//*[text()="1"]'
        self.button_2 = '//*[text()="2"]'
        self.button_3 = '//*[text()="3"]'
        self.button_4 = '//*[text()="4"]'
        self.button_5 = '//*[text()="5"]'
        self.button_6 = '//*[text()="6"]'
        self.button_7 = '//*[text()="7"]'
        self.button_8 = '//*[text()="8"]'
        self.button_9 = '//*[text()="9"]'
        self.button_plus_minus = '//*[text()="+/-"]'
        self.button_AC = '//*[text()="AC"]'
        self.button_percent = '//*[text()="%"]'
        self.button_equate = '//*[text()="="]'
        self.button_plus = '//*[text()="+"]'
        self.button_minus = '//*[text()="-"]'
        self.button_multiplication = '//*[text()="x"]'
        self.button_division = '//*[text()="÷"]'
        self.result_component = '//*[@class="component-display"]'