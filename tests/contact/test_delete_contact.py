def test_delete_contacts(app):
    app.session.login('admin', 'secret')
    app.contact.delete()
    app.accept_alert()
    app.session.logout()