from e2e import settings


class CommonActions:
    def __init__(self, page, login_page, top_bar_page):
        self.page = page
        self.login_page = login_page
        self.top_bar_page = top_bar_page

    # login as admin
    def login_as_admin(self):
        self.login_page.email_field.input_text(settings.ADMIN_EMAIL)
        self.login_page.password_field.input_text(settings.PASSWORD)
        self.page.submit_button.click()

    # logout
    def logout(self):
        self.top_bar_page.expand_profile_button.click()
        self.top_bar_page.sign_out_button.click()

    def login_as_user(self, email):
        # return to sign in page
        self.login_page.sign_in_button.click()

        # input new user email
        self.login_page.email_field.input_text(email)

        # input new user password
        self.login_page.password_field.input_text(settings.PASSWORD)

        # login
        self.page.submit_button.click()

    # switch to admin interface
    def switch_to_admin_interface(self):
        self.top_bar_page.interface_switch.click()
        self.top_bar_page.select_admin_interface.click()

    # switch to backoffice interface
    def switch_to_backoffice_interface(self):
        self.top_bar_page.interface_switch.click()
        self.top_bar_page.select_backoffice_interface.click()

    # switch to client interface
    def switch_to_client_interface(self):
        self.top_bar_page.interface_switch.click()
        self.top_bar_page.select_client_interface.click()

