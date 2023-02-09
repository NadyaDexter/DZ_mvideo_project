import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains


class Cart_page(Base):


    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g
        self.action = ActionChains(driver_g)

    # Locators

    delete_single = "//span[@class='cart-item-actions__title']"
    cart_game_name = "/html/body/mvid-root/div/ng-component/mvid-layout/div/main/div/div/div[1]/mvid-cart-list/div/ul/li/mvid-cart-item/div/div/div[2]/div[1]/div/div/h3/a"
    cart_game_price = "/html/body/mvid-root/div/ng-component/mvid-layout/div/main/div/div/div[1]/mvid-cart-list/div/ul/li/mvid-cart-item/div/div/div[2]/div[2]/mvid-cart-item-price/div/mvid-price/div/span"
    final_price = "/html/body/mvid-root/div/ng-component/mvid-layout/div/main/div/div/div[2]/div/mvid-cart-total/div/div[1]/div[3]/p[2]"
    empty_cart = "//h1[@class='cart-empty__title']"


    # Getters

    def get_delete_single(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_single)))

    def get_cart_game_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_game_name)))

    def get_cart_game_price(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_game_price)))

    def get_final_price(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.final_price)))

    def get_empty_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.empty_cart)))


    # Actions

    def click_get_delete_single(self):
        self.get_delete_single().click()
        print("Нажали на кнопку Удалить")


    # Methods
    def cart_assert_and_delete(self):
        self.assert_text(self.get_cart_game_name(), "PS4 игра Sony NieR: Automata - Game of the YoRHa Edition")
        self.assert_text(self.get_cart_game_price(), "3 199 ₽")
        self.assert_valuables(self.get_cart_game_price(), self.get_final_price())
        self.click_get_delete_single()
        time.sleep(1)
        self.assert_word(self.get_empty_cart(), "Корзина пуста")
        self.get_screenshot()










