link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_presence_button_add_basket(browser):
    browser.get(link)
    number_button = len (browser.find_elements_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket") )
    assert number_button, "Not button add basket"