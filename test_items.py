import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestProductPage:

    def test_presence_button_add_to_basket(self, browser):
        browser.get(link)
        time.sleep(30)
        assert browser.find_element_by_css_selector("button.btn-add-to-basket")
