import time
link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_goods_has_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    button1 = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert button1, 'Нет кнопки добавления товара'