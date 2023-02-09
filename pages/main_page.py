import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains


class Main_page(Base):

    url = "https://www.mvideo.ru/"

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g
        self.action = ActionChains(driver_g)

    # Locators

    catalog_button = "//button[@class='button button--with-icon ng-star-inserted']"
    games_and_soft = "//a[@href='https://www.mvideo.ru/igry-i-razvlecheniya']"
    games_ps4 = "//a[@title='Игры для PlayStation 4']"
    age_filter_18 = "//a[@href='/playstation-4327/ps4-igry-4331/f/category=igry-dlya-playstation-4-ps4-4343/tolko-v-nalichii=da/vozrastnoe-ogranichenie=18']"
    language_filter_eng = "//a[@href='/playstation-4327/ps4-igry-4331/f/category=igry-dlya-playstation-4-ps4-4343/tolko-v-nalichii=da/vozrastnoe-ogranichenie=18/yazyk=angliiskii']"
    nier_game_to_cart = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/div[2]/mvid-product-list/mvid-plp-product-cards-layout/div/mvid-product-cards-row/div[2]/mvid-plp-product-checkout[1]/div/mvid-preorder-v2-wrapper/div/mvid-plp-checkout-tooltip/mvid-plp-cart-button/mvid-button/button"
    to_cart = "//a[@href='https://www.mvideo.ru/cart']"
    game_name = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/div[2]/mvid-product-list/mvid-plp-product-cards-layout/div/mvid-product-cards-row/div[2]/div[2]/mvid-plp-product-title/div/a"
    game_price = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/div[2]/mvid-product-list/mvid-plp-product-cards-layout/div/mvid-product-cards-row/div[2]/div[4]/mvid-plp-price-block/div/mvid-price/div/span"


    # Getters

    def get_catalog_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_games_and_soft(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.games_and_soft)))

    def get_games_ps4(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.games_ps4)))

    def get_age_filter_18(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.age_filter_18)))

    def get_language_filter_eng(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.language_filter_eng)))

    def get_nier_game_to_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.nier_game_to_cart)))

    def get_to_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.to_cart)))

    def get_game_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.game_name)))

    def get_game_price(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.game_price)))


    # Actions


    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Нажали на Каталог")

    def navigate_games_and_soft(self):
        self.action.move_to_element(self.get_games_and_soft()).perform()
        print("Навели на Игры и Софт")

    def click_games_ps4(self):
        self.get_games_ps4().click()
        print("Выбрали Игры для PlayStation 4")

    def navigate_to(self, x, y):
        self.driver_g.execute_script("window.scrollTo(" + str(x) + ", " + str(y)+")")

    def click_get_age_filter_18(self):
        self.get_age_filter_18().click()
        print("Выбрали фильтр 18+")

    def click_get_language_filter_eng(self):
        self.get_language_filter_eng().click()
        print("Выбрали фильтр Язык: английский")

    def click_get_nier_game_to_cart(self):
        self.get_nier_game_to_cart().click()
        print("Добавили игру в корзину")

    def click_to_cart(self):
        self.get_to_cart().click()
        print("Перешли в корзину")


    # Methods

    def catalog_select(self):
        self.driver_g.get(self.url)
        self.driver_g.maximize_window()
        self.get_current_url()
        self.click_catalog_button()
        time.sleep(1)
        self.navigate_games_and_soft()
        time.sleep(1)
        self.click_games_ps4()

    def filters_select(self):
        self.navigate_to(0,1400)
        time.sleep(1)
        self.click_get_age_filter_18()
        time.sleep(1)
        self.click_get_language_filter_eng()
        self.navigate_to(0, 650)
        time.sleep(1)

    def game_to_cart(self):
        self.var_as_text(self.get_game_name())
        self.var_as_text(self.get_game_price())
        self.click_get_nier_game_to_cart()
        time.sleep(1)
        self.click_to_cart()
        time.sleep(2)
        self.get_current_url()
        self.assert_url('https://www.mvideo.ru/cart')









