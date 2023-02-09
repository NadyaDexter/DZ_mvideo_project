import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import Main_page
from pages.cart_page import Cart_page


def test_1_buy_game(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver_g = webdriver.Chrome(executable_path='C:\\Users\\NadyaDexter\\PycharmProjects\\resource\chromedriver.exe', chrome_options=options)

    print("Start Test 1")

    catalog_game = Main_page(driver_g)
    catalog_game.catalog_select()
    time.sleep(2)

    filters = Main_page(driver_g)
    filters.filters_select()
    time.sleep(3)

    select_game = Main_page(driver_g)
    select_game.game_to_cart()

    crt1 = Cart_page(driver_g)
    crt1.cart_assert_and_delete()

    print("Test 1 Finished")
    time.sleep(3)
    driver_g.quit()



