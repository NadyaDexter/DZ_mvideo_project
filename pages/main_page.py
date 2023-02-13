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
        self.move = ActionChains(driver_g)

    # Locators

    catalog_button = "//button[@class='button button--with-icon ng-star-inserted']"
    games_and_soft = "//a[@href='https://www.mvideo.ru/igry-i-razvlecheniya']"
    games_ps4 = "//a[@title='Игры для PlayStation 4']"
    age_filter_18 = "//a[@href='/playstation-4327/ps4-igry-4331/f/category=igry-dlya-playstation-4-ps4-4343/tolko-v-nalichii=da/vozrastnoe-ogranichenie=18']"
    language_filter_eng = "//a[@href='/playstation-4327/ps4-igry-4331/f/category=igry-dlya-playstation-4-ps4-4343/tolko-v-nalichii=da/vozrastnoe-ogranichenie=18/yazyk=angliiskii']"
    game_to_cart = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/div[2]/mvid-product-list/mvid-plp-product-cards-layout/div/mvid-product-cards-row/div[4]/mvid-plp-product-checkout[3]/div/mvid-preorder-v2-wrapper/div/mvid-plp-checkout-tooltip/mvid-plp-cart-button/mvid-button/button"
    to_cart = "//a[@href='https://www.mvideo.ru/cart']"
    game_name = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/div[2]/mvid-product-list/mvid-plp-product-cards-layout/div/mvid-product-cards-row/div[4]/div[14]/mvid-plp-product-title/div/a"
    game_price = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/div[2]/mvid-product-list/mvid-plp-product-cards-layout/div/mvid-product-cards-row/div[4]/div[16]/mvid-plp-price-block/div/mvid-price/div/span"
    search_field = "//input[@id='1']"
    search_button = "//div[@class='search-icon-wrap ng-star-inserted']"
    all_filters_button = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-srp/mvid-product-list-block/mvid-filters-list/div/div[2]/mvid-button/button"
    category_filters = "/html/body/mvid-root/mvid-modals-container/div[1]/mvid-modal/div/div/div/div/mvid-filters-list/div/div[1]/div[2]/div[1]/mvid-accordion[1]/div/div/label"
    brand_filters = "/html/body/mvid-root/mvid-modals-container/div[1]/mvid-modal/div/div/div/div/mvid-filters-list/div/div[1]/div[2]/div[2]/mvid-accordion/div/div/label"
    price_filters = "/html/body/mvid-root/mvid-modals-container/div[1]/mvid-modal/div/div/div/div/mvid-filters-list/div/div[1]/div[2]/div[3]/mvid-accordion[1]/div/div/label"
    ps5_gamepad_filter ="/html/body/mvid-root/mvid-modals-container/div[1]/mvid-modal/div/div/div/div/mvid-filters-list/div/div[1]/div[2]/div[1]/mvid-accordion[1]/div/div/div/mvid-filter-checkbox-list/form/div/div[1]/mvid-checkbox"
    brand_ps5_filter = "/html/body/mvid-root/mvid-modals-container/div[1]/mvid-modal/div/div/div/div/mvid-filters-list/div/div[1]/div[2]/div[2]/mvid-accordion/div/div/div/mvid-filter-checkbox-list/form/div/div[1]/mvid-checkbox"
    brand_rainbo_filter = "/html/body/mvid-root/mvid-modals-container/div[1]/mvid-modal/div/div/div/div/mvid-filters-list/div/div[1]/div[2]/div[2]/mvid-accordion/div/div/div/mvid-filter-checkbox-list/form/div/div[3]/mvid-checkbox/div"
    brand_sony_filter = "/html/body/mvid-root/mvid-modals-container/div[1]/mvid-modal/div/div/div/div/mvid-filters-list/div/div[1]/div[2]/div[2]/mvid-accordion/div/div/div/mvid-filter-checkbox-list/form/div/div[2]/mvid-checkbox"
    price_slider = "/html/body/mvid-root/mvid-modals-container/div[1]/mvid-modal/div/div/div/div/mvid-filters-list/div/div[1]/div[2]/div[3]/mvid-accordion[1]/div/div/div/mvid-price-facet/div/div/mvid-slider/div/div/button[1]/div"
    show_button = "/html/body/mvid-root/mvid-modals-container/div[1]/mvid-modal/div/div/div/div/mvid-filters-list/div/div[4]/mvid-button/button/span"
    gamepad = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-srp/mvid-product-list-block/div[2]/mvid-product-list/mvid-plp-product-cards-layout/div/mvid-product-cards-row/div/div[2]/mvid-plp-product-title/div"


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

    def get_game_to_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.game_to_cart)))

    def get_to_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.to_cart)))

    def get_game_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.game_name)))

    def get_game_price(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.game_price)))

    def get_search_field(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field)))

    def get_search_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))

    def get_all_filters_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.all_filters_button)))

    def get_category_filters(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_filters)))

    def get_brand_filters(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_filters)))

    def get_price_filters(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_filters)))

    def get_ps5_gamepad_filter(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.ps5_gamepad_filter)))

    def get_brand_ps5_filter(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_ps5_filter)))

    def get_brand_sony_filter(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_sony_filter)))

    def get_brand_rainbo_filter(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_rainbo_filter)))

    def get_price_slider(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_slider)))

    def get_show_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_button)))

    def get_gamepad(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.gamepad)))


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

    def click_get_age_filter_18(self):
        self.get_age_filter_18().click()
        print("Выбрали фильтр 18+")

    def click_get_language_filter_eng(self):
        self.get_language_filter_eng().click()
        print("Выбрали фильтр Язык: английский")

    def click_get_game_to_cart(self):
        self.get_game_to_cart().click()
        print("Добавили игру в корзину")

    def click_to_cart(self):
        self.get_to_cart().click()
        print("Перешли в корзину")

    def input_search_field(self):
        self.get_search_field().send_keys("геймпад ps5")
        print("Ввели текст в строку поиска")

    def click_search_button(self):
        self.get_search_button().click()
        print("Нажали кнопку Поиск(лупа)")

    def click_all_filters_button(self):
        self.get_all_filters_button().click()
        print("Нажали кнопку Все фильтры")

    def click_category_filters(self):
        self.get_category_filters().click()
        print("Раскрыли вкладку фильтров Категории")

    def click_ps5_gamepad_filter(self):
        self.get_ps5_gamepad_filter().click()
        print("Выбрали фильтр Категория: Геймпад PS5")

    def click_brand_filters(self):
        self.get_brand_filters().click()
        print("Раскрыли вкладку фильтров Бренды")

    def click_brand_ps5_filter(self):
        self.get_brand_ps5_filter().click()

    def click_brand_sony_filter(self):
        self.get_brand_sony_filter().click()

    def click_brand_rainbo_filter(self):
        self.get_brand_rainbo_filter().click()
        print("Выбрали фильтры Бренд: PlayStation 5, Sony, PlayStation 5 Rainbo")

    def click_price_filters(self):
        self.get_price_filters().click()
        print("Раскрыли вкладку фильтров Цена")

    def slide_price_slider(self):
        self.move.click_and_hold(self.get_price_slider()).move_by_offset(100, 0).release().perform()
        print("Прокрутили слайдер Цена вправо")

    def click_show_button(self):
        self.get_show_button().click()
        print("Нажали кнопку Показать товары")

    def click_gamepad_page(self):
        self.get_gamepad().click()
        print("Перешли на страницу товара")


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
        self.navigate_to(0,1350)
        time.sleep(1)
        self.click_get_age_filter_18()
        time.sleep(1)
        self.click_get_language_filter_eng()
        time.sleep(1)

    def put_game_to_cart(self):
        self.var_as_text(self.get_game_name())
        self.var_as_text(self.get_game_price())
        self.click_get_game_to_cart()
        time.sleep(1)
        self.click_to_cart()
        time.sleep(2)
        self.get_current_url()
        self.assert_url('https://www.mvideo.ru/cart')

    def search_by_field(self):
        self.driver_g.get(self.url)
        self.driver_g.maximize_window()
        self.get_current_url()
        self.input_search_field()
        self.click_search_button()
        time.sleep(1)
        self.navigate_to(0, 800)
        time.sleep(1)
        self.click_all_filters_button()
        self.click_category_filters()
        time.sleep(1)
        self.click_ps5_gamepad_filter()
        time.sleep(1)
        self.click_brand_filters()
        time.sleep(1)
        self.click_brand_ps5_filter()
        self.click_brand_sony_filter()
        self.click_brand_rainbo_filter()
        time.sleep(1)
        self.click_price_filters()
        time.sleep(1)
        self.slide_price_slider()
        time.sleep(1)
        self.click_show_button()
        time.sleep(2)
        self.click_gamepad_page()













