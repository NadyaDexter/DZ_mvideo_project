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
    cart_name = "//a[@class='cart-item__name ng-star-inserted']"
    cart_price = "//span[@class='price__main-value']"
    final_price = "/html/body/mvid-root/div/ng-component/mvid-layout/div/main/div/div/div[2]/div/mvid-cart-total/div/div[1]/div[3]/p[2]"
    empty_cart = "//h1[@class='cart-empty__title']"
    check_in_button = "//button[@class='cart-total__button-total ng-tns-c301-1 mv-main-button--large mv-main-button--primary mv-button mv-main-button']"
    skip_button = "//button[@class='login-form__button login-form__button--skip mv-main-button--secondary mv-main-button--medium mv-button mv-main-button ng-star-inserted']"
    del_all = "//a[@class='cart-list__delete-selected-button mv-link-button--default mv-button mv-link-button ng-star-inserted']"


    # Getters

    def get_delete_single(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_single)))

    def get_cart_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_name)))

    def get_cart_price(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_price)))

    def get_final_price(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.final_price)))

    def get_empty_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.empty_cart)))

    def get_check_in_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_in_button)))

    def get_skip_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.skip_button)))

    def get_del_all(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.del_all)))


    # Actions

    def click_delete_single(self):
        self.get_delete_single().click()
        print("Нажали на кнопку Удалить")

    def click_check_in_button(self):
        self.get_check_in_button().click()
        print("Нажали на кнопку Перейти к оформлению")

    def click_skip_button(self):
        self.get_skip_button().click()
        print("Нажали на кнопку Пропустить (ввод номера телефона)")

    def click_del_all(self):
        self.get_del_all().click()
        print("Нажали Удалить выбранные")


    # Methods

    def cart_assert_and_delete(self):
        self.assert_values(self.get_cart_price(), self.get_final_price())
        self.click_delete_single()
        time.sleep(1)
        self.assert_word(self.get_empty_cart(), "Корзина пуста")
        self.get_screenshot()

    def cart_assert(self):
        self.assert_values(self.get_cart_price(), self.get_final_price())
        time.sleep(1)
        self.click_check_in_button()
        time.sleep(1)
        self.click_skip_button()

    def cart_delete_all(self):
        self.click_del_all()
        self.assert_word(self.get_empty_cart(), "Корзина пуста")
        self.get_screenshot()













