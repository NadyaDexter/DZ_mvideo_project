import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains


class Product_page(Base):

    url = "https://www.mvideo.ru/"

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g
        self.action = ActionChains(driver_g)
        self.move = ActionChains(driver_g)

    # Locators

    color_pink = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-pdp/mvid-pdp-general/div/mvid-general-details/section/div[2]/div[3]/div[1]/div/div[1]/mvid-multi-sku/div/div/mvid-carousel/div[1]/div/div/a[6]/div/div"
    gamepad_name = "//h1[@class='title']"
    gamepad_price = "//span[@class='price__main-value']"
    gamepad_to_cart = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-pdp/mvid-pdp-general/div/mvid-general-details/section/div[2]/div[3]/div[2]/mvideoru-product-details-card[1]/div/mvid-preorder-v2-wrapper/mvideoru-cart-button/button"
    go_to_cart_button = "//button[@class='cart-button mv-main-button--large mv-main-button--primary mv-button mv-main-button mv-main-button--outline']"


    # Getters

    def get_color_pink(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.color_pink)))

    def get_gamepad_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.gamepad_name)))

    def get_gamepad_price(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.gamepad_price)))

    def get_gamepad_to_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.gamepad_to_cart)))

    def get_go_to_cart_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_button)))


    # Actions

    def chose_color_pink(self):
        self.get_color_pink().click()
        print("Выбрали цвет: Розовый")

    def click_gamepad_to_cart(self):
        self.get_gamepad_to_cart().click()
        print("Добавили товар в корзину")

    def click_go_to_cart_button(self):
        self.get_go_to_cart_button().click()
        print("Нажали кнопку Перейти в корзину")


    # Methods

    def gamepad_page(self):
        self.chose_color_pink()
        self.var_as_text(self.get_gamepad_name())
        self.var_as_text(self.get_gamepad_price())
        self.navigate_to(0, 100)
        self.click_gamepad_to_cart()
        time.sleep(1)

    def put_gamepad_to_cart(self):
        self.click_go_to_cart_button()
        self.get_current_url()
        self.assert_url('https://www.mvideo.ru/cart')












