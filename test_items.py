link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_presence_button_add_basket(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket") 
    assert button.is_displayed(), "Basket button is not visible"
