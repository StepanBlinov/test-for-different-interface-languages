import time

#ссылка на которой корзина присутствует, тест должен пройти без ошибки:
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#ссылка на которой корзины нет, тест должен упасть:
#link = "http://selenium1py.pythonanywhere.com/"

def test_basket_search(browser):
    browser.get(link)
    # поставил таймер на 10 сек, что бы можно было понять, что язык ссответстует заданному параметру
    time.sleep(10)
    basket = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    #проверям что найденных корзин больше 0
    assert len(basket) > 0,"Корзина на странице не найдена!"