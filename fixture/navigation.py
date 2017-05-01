# -*- coding: utf-8 -*-
class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not ((len(wd.find_elements_by_link_text("Управление проектами")) > 0)
                and (len(wd.find_elements_by_link_text("Оставаться в системе")) > 0)):
            wd.get(self.app.base_url)
