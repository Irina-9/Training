from model.contact import Contact

def test_edit_contact_fname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="New first name"))
    app.session.logout()

def test_edit_contact_mname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(middlename="New middle name"))
    app.session.logout()

def test_edit_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(address="New address"))
    app.session.logout()

def test_edit_contact_hphone(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(home="111111111"))
    app.session.logout()