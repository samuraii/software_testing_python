def test_delete_contacts(app):
    app.contact.delete()
    app.accept_alert()
