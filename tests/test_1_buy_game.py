import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from base.base_class import Base


def test_1_buy_game(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver_g = webdriver.Chrome(executable_path='C:\\Users\\NadyaDexter\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)

    print("Start Test 1")

    catalog_game = Main_page(driver_g)
    catalog_game.catalog_select()
    time.sleep(2)

    filters = Main_page(driver_g)
    filters.filters_select()
    time.sleep(3)

    # Сохраняем в переменные название и цену товара
    a1 = Main_page(driver_g)
    n1 = (a1.get_game_name()).text
    p1 = (a1.get_game_price()).text

    select_game = Main_page(driver_g)
    select_game.put_game_to_cart()

    # Сохраняем в переменные название и цену товара в корзине
    a2 = Cart_page(driver_g)
    n2 = (a2.get_cart_name()).text
    p2 = (a2.get_cart_price()).text

    # Сравниваем значения переменных названий и цен товара
    ass_n = Base(driver_g)
    ass_n.assert_text(n1, n2)
    ass_p = Base(driver_g)
    ass_p.assert_text(p1, p2)

    crt1 = Cart_page(driver_g)
    crt1.cart_assert_and_delete()

    print("Test 1 Finished")
    time.sleep(3)
    driver_g.quit()



