import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.details_page import Details_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from base.base_class import Base
from pages.product_page import Product_page


def test_2_buy_gamepad(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver_g = webdriver.Chrome(executable_path='C:\\Users\\NadyaDexter\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)

    print("Start Test 2")

    by_search = Main_page(driver_g)
    by_search.search_by_field()
    time.sleep(3)

    gp = Product_page(driver_g)
    gp.gamepad_page()

    # Сохраняем в переменные название и цену товара
    a1 = Product_page(driver_g)
    n1 = (a1.get_gamepad_name()).text
    p1 = (a1.get_gamepad_price()).text

    tc = Product_page(driver_g)
    tc.put_gamepad_to_cart()
    time.sleep(1)

    # Сохраняем в переменные название и цену товара в корзине
    a2 = Cart_page(driver_g)
    n2 = (a2.get_cart_name()).text
    p2 = (a2.get_cart_price()).text

    # Сравниваем значения переменных названий и цен товара
    ass_n = Base(driver_g)
    ass_n.assert_text(n1, n2)
    ass_p = Base(driver_g)
    ass_p.assert_text(p1, p2)

    prc = Cart_page(driver_g)
    prc.cart_assert()
    time.sleep(1)

    ss = Details_page(driver_g)
    ss.shop_scroll()
    time.sleep(1)

    # Сохраняем в переменную адрес магазина
    al = Details_page(driver_g)
    l1 = (al.get_shop_location()).text

    sc = Details_page(driver_g)
    sc.shop_chose()
    time.sleep(1)

    # Сравниваем итоговую цену
    a3 = Details_page(driver_g)
    p3 = (a3.get_purchase_price()).text
    ass_p2 = Base(driver_g)
    ass_p2.assert_text(p2, p3)

    # Сравниваем итоговый адрес с выбранным
    al2 = Details_page(driver_g)
    l2 = (al2.get_purchase_location()).text
    ass_al = Base(driver_g)
    ass_al.assert_text(l1, l2)

    steps = Details_page(driver_g)
    steps.steps_and_cancel()

    da = Cart_page(driver_g)
    da.cart_delete_all()

    print("Test 2 Finished")
    time.sleep(3)
    driver_g.quit()



