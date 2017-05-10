from model.project import Project
import re


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def create(self, project):
        wd = self.app.wd
        self.app.navigation.open_project_page()
        wd.find_element_by_xpath('//input[@value="создать новый проект"]').click()
        self.fill_project_fields(project)
        wd.find_element_by_xpath('//input[@value="Добавить проект"]').click()
        wd.find_element_by_xpath('//a[contains(text(),"Продолжить")]').click()
        self.project_cache = None

    def fill_project_fields(self, project):
        self.change_field_value('project-name', project.name)
        self.change_field_value('project-description', project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(field_name).click()
            wd.find_element_by_id(field_name).clear()
            wd.find_element_by_id(field_name).send_keys(text)

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.app.navigation.open_project_page()
            self.project_cache = []
            l = len(wd.find_elements_by_xpath('//table/tbody/tr/td[1]/a'))
            for i in range(l):
                index = i + 1
                element = wd.find_element_by_xpath('//table/tbody/tr['+str(index)+']/td[1]/a')
                name = element.text
                href = element.get_attribute("href")
                id = int(re.search("\d+$", href).group(0))
                description = wd.find_element_by_xpath('//table/tbody/tr['+str(index)+']/td[5]').text
                self.project_cache.append(Project(id=id, name=name, description=description))
        return list(self.project_cache)

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.app.navigation.open_project_page()
        wd.find_element_by_xpath('//a[@href="manage_proj_edit_page.php?project_id='+str(id)+'"]').click()
        wd.find_element_by_xpath('//input[@value="Удалить проект"]').click()
        wd.find_element_by_xpath('//input[@value="Удалить проект"]').click()
        self.project_cache = None
