import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_card_button(browser):
    browser.get(link)
    but = browser.find_elements_by_id("add_to_basket_form")
    assert but, "корзина не найдена"
       
    
    
    