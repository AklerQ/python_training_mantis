from model.project import Project
from generator.project import random_string


def test_add_project(app):
    old_projects = app.project.get_project_list()
    project = Project(name=random_string("Name ", 22), description=random_string("Description ", 140))
    app.project.create(project)
    new_projects = app.project.get_project_list()
    old_projects.append(Project.clear(project))
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)



