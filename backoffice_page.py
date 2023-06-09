from selenium.webdriver.common.by import By
from e2e.src.front_end_automation.base.base_element import BaseElement as Be
from e2e.src.front_end_automation.base.base_page import BasePage as Bp
from e2e.src.front_end_automation.base.locator import Locator

class PartnershipPage(Bp):
    @property
    def saved_reports_button(self):
        return Be(driver=self.driver, locator=Locator(by=By.XPATH, value="//*[text()='Saved reports']"))

    def saved_report_status_by_index(self, index):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value=f".SavedReportsTable .rt-tr-group:nth-child({index}) .rt-td:nth-child(3)"))


class DepositsPage(Bp):
    def entry_in_deposits_table_by_id(self, payment_id):
        return Be(driver=self.driver, locator=Locator(by=By.XPATH, value=f"//div[@class='rt-tbody']/div[@class='rt-tr-group']//span[text()='{payment_id}']/ancestor::div[@role='row']"))

    def entry_in_deposits_table_by_index(self, index):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value=f".rt-tbody .rt-tr-group:nth-child({index})"))

    @property
    def mark_as_failed_button(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value=".PaymentPage__buttons-inner .DefaultButton:nth-child(2)"))

    @property
    def type_manually_button(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value=".BasicModal__inner .RejectDepositForm__btns .DefaultButton:nth-child(3)"))

    @property
    def send_button(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value=".RejectDepositForm .RejectDepositForm__btns .DefaultButton:nth-child(1)"))

    @property
    def failed_status(self):
        return Be(driver=self.driver, locator=Locator(by=By.XPATH, value="//*[contains(text(), 'Failed')]"))

    @property
    def amount_icon(self):
        return Be(driver=self.driver, locator=Locator(by=By.ID, value="actionsEditValue"))

    @property
    def amount_field(self):
        return Be(driver=self.driver, locator=Locator(by=By.ID, value="amount"))

    @property
    def comment_field(self):
        return Be(driver=self.driver, locator=Locator(by=By.ID, value="comment"))

    @property
    def save_button(self):
        return Be(driver=self.driver, locator=Locator(by=By.XPATH, value="//*[text()='Save']/ancestor::button"))

    @property
    def execute_button(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value=".PaymentPage__buttons-inner .DefaultButton:nth-child(1)"))

    @property
    def deposited_status(self):
        return Be(driver=self.driver, locator=Locator(by=By.XPATH, value="//*[contains(text(), 'Deposited')]"))

    @property
    def reject_proof_of_payment_button(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value=".UserDocument__buttons-inner .DefaultButton__error"))

    @property
    def type_manually_proof_of_payment_rejection_message_button(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value=".RejectDocumentForm__btns .noBorder"))

    @property
    def verify_proof_of_payment_button(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value=".UserDocument__inner .DefaultButton__success"))

    @property
    def payments_button(self):
        return Be(driver=self.driver, locator=Locator(by=By.XPATH, value="//*[text()='Payments']"))

    def find_row_by_sum(self, deposit):
        return Be(driver=self.driver, locator=Locator(by=By.XPATH, value=f"//*[text()={deposit}]"))

