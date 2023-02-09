import datetime
from datetime import timedelta


class Base():

    def __init__(self, driver_g):
        self.driver_g = driver_g

    """Method Get current URL"""

    def get_current_url(self):
        get_url = self.driver_g.current_url
        print("Current URL " + get_url)

    """Method save variable as text"""

    def var_as_text(self, vari):
        value_variables = vari.text
        print(value_variables)

    """Method assert word on page"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Key Word CORRECT: " + value_word)

    """Method assert text"""

    def assert_text(self, var1, var2):
        value_var1 = var1.text
        assert value_var1 == var2
        print("Variable " + value_var1 + " CORRECT")

    """Method assert two variables"""

    def assert_valuables(self, vari1, vari2):
        value_vari1 = vari1.text
        value_vari2 = vari2.text
        assert value_vari1 == value_vari2
        print("Variable " + value_vari1 + " CORRECT")

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = (datetime.datetime.utcnow() + timedelta(hours=+3)).strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver_g.save_screenshot('C:\\Users\\NadyaDexter\\PycharmProjects\\mvideo_project\\screenshots\\' + name_screenshot)

    """Method assert URL"""

    def assert_url(self, result):
        get_url = self.driver_g.current_url
        assert get_url == result
        print("Key URL CORRECT")
