def test_delete_group(app):
    app.session.login('admin', 'secret')
    app.group.delete_first()
    app.session.logout()
