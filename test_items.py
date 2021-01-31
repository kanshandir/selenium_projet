
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_is_element_present(browser):
    browser.get(link)
    assert len(browser.find_elements_by_id("add_to_basket_form")) > 0, "no add to basket button"
