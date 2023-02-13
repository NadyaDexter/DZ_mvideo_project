import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains


class Details_page(Base):


    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g
        self.action = ActionChains(driver_g)

    # Locators

    chose_shop_button = "//button[@class='button button--light button--full-size ng-star-inserted']"
    shop_list_button = "/html/body/mvid-root/mvid-modals-container/div[1]/mvid-modal/div/div/div/div/mvid-pickup-selector-modal/div/div[1]/div[3]/mvid-tabs/div/ul/li[2]/button"
    shop_location = "/html/body/mvid-root/mvid-modals-container/div[1]/mvid-modal/div/div/div/div/mvid-pickup-selector-modal/div/div[2]/div[1]/mvid-pickup-list/div/table/div/tr[9]/td[1]/p"
    next_button = "//button[@class='payment-button mv-main-button--primary mv-main-button--medium mv-button mv-main-button ng-star-inserted']"
    here_button = "/html/body/mvid-root/mvid-modals-container/div[1]/mvid-modal/div/div/div/div/mvid-pickup-selector-modal/div/div[2]/div[2]/mvid-pickup-info-store/div[2]/div/mvid-button/button"
    email_field = "//input[@id='mvideo-form-field-input-3']"
    name_field = "//input[@id='mvideo-form-field-input-1']"
    phone_field = "//input[@id='mvideo-form-field-input-2']"
    purchase_price = "/html/body/mvid-root/div/ng-component/ng-component/mvid-layout/div/main/div/div/div[2]/div/div/mvid-checkout-total/section/div[1]/div[3]/p[2]"
    purchase_location = "/html/body/mvid-root/div/ng-component/ng-component/mvid-layout/div/main/div/div/div[1]/div[1]/mvid-checkout-handover-details/div/div/div[2]/div/span"
    back_step_1 = "//button[@class='secondary-header__back-button ng-star-inserted']"


    # Getters

    def get_chose_shop_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.chose_shop_button)))

    def get_shop_list_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.shop_list_button)))

    def get_shop_location(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.shop_location)))

    def get_next_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.next_button)))

    def get_here_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.here_button)))

    def get_name_field(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_field)))

    def get_phone_field(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_field)))

    def get_email_field(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_purchase_price(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.purchase_price)))

    def get_purchase_location(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.purchase_location)))

    def get_back_step_1(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.back_step_1)))


    # Actions


    def click_chose_shop_button(self):
        self.get_chose_shop_button().click()
        print("Нажали на кнопку Выбрать магазин")

    def click_shop_list_button(self):
        self.get_shop_list_button().click()
        print("Нажали на кнопку Список")

    def scroll_shop_location(self):
        self.action.move_to_element(self.get_shop_location()).perform()
        print("Проскролили список до нужного адреса")

    def click_shop_location(self):
        self.get_shop_location().click()
        print("Выбрали нужный адрес")

    def click_here_button(self):
        self.get_here_button().click()
        print("Нажали на Заберу отсюда")

    def click_next_button(self):
        self.get_next_button().click()
        print("Нажали на кнопку Далее")

    def input_name_field(self):
        self.get_name_field().send_keys("Кирюха Казума")
        print("Ввели имя")

    def input_phone_field(self):
        self.get_phone_field().send_keys("0000000000")
        print("Ввели номер телефона")

    def input_email_field(self):
        self.get_email_field().send_keys("dragon_of_dojima@rggmail.com")
        print("Ввели email")

    def click_back_step_1(self):
        self.get_back_step_1().click()
        print("Нажали Вернуться на шаг назад")


    # Methods


    def shop_scroll(self):
        self.navigate_to(0, 400)
        time.sleep(1)
        self.click_chose_shop_button()
        time.sleep(1)
        self.click_shop_list_button()
        time.sleep(1)
        self.scroll_shop_location()
        time.sleep(1)

    def shop_chose(self):
        self.click_shop_location()
        time.sleep(1)
        self.click_here_button()
        time.sleep(1)
        self.click_next_button()

    def steps_and_cancel(self):
        self.navigate_to(0, 800)
        time.sleep(1)
        self.input_name_field()
        time.sleep(0.5)
        self.input_phone_field()
        time.sleep(0.5)
        self.input_email_field()
        time.sleep(0.5)
        self.navigate_to(0, 0)
        time.sleep(1)
        self.click_back_step_1()
        self.get_current_url()
        self.assert_url("https://www.mvideo.ru/purchase/step1")
        time.sleep(1)
        self.click_back_step_1()
        time.sleep(1)














