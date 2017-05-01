# -*- coding: utf-8 -*-


def test_login(app):
    app.session.login("administrator", "python")
    assert app.session.is_logged_in_as("administrator")
