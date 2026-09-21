class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator("[data-test='title']")

    def get_title_text(self):
        return self.title.inner_text()