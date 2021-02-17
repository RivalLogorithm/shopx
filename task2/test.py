from pages.main_page import MainPage

def test_auth(browser):
    avito_auth_page = MainPage(browser,'https://www.avito.ru/#login?authsrc=h')
    avito_auth_page.open()
    avito_auth_page.enter_login_and_pass('','')
    avito_auth_page.click_submit_button()
    profile = avito_auth_page.is_login_in()
    assert profile, str

def test_is_phone_empty(browser):
    avito_items_page = MainPage(browser, 'https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1')
    avito_items_page.open()
    avito_items_page.get_item(0)
    avito_items_page.select_new_tab()
    avito_items_page.click_delivery_button()
    phone = avito_items_page.get_phone_field()
    assert phone == ''
