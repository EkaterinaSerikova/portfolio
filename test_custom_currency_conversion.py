from e2e.utilities.capture_logs import GeneralLogs
from e2e.src.back_end_automation import jsons, endpoints
from e2e.src.back_end_automation.base_requests import ApiMethods
from pytest import mark

# random inputs
from e2e import settings
from e2e.utilities.random_inputs import random_phone, random_fake_email

# shortcuts
from e2e.tests.shortcuts.create_new_user import CreateNewUser
from e2e.tests.shortcuts.common_actions import CommonActions

# pages
from e2e.src.front_end_automation.pages.common_elements import CommonElements
from e2e.src.front_end_automation.pages.login_page import LoginPage
from e2e.src.front_end_automation.pages.top_bar_page import TopBarPage
from e2e.src.front_end_automation.pages.client_page import ClientPage, AccountPage
from e2e.src.front_end_automation.pages.backoffice_page import (BackofficeSidebarButtons, DepositsPage, DashboardsPage,
                                                                WithdrawalsPage)

# steps
from e2e.tests.steps.preliminary_steps.preliminary_steps import PreliminarySteps
from e2e.tests.steps.trading_accounts.trading_accounts import TradingAccounts
from e2e.tests.steps.platforms.setup_platforms import SetupPlatforms

# payments
from e2e.tests.steps.trading_accounts.payments import Payments


def test_custom_currency_conversion(session, drv, app_config):
    # instantiate logs
    log = GeneralLogs("test_custom_currency_conversion")

    preliminary_steps = PreliminarySteps(session)
    payments = Payments(session, log)
    page = CommonElements(drv)
    login_page = LoginPage(drv)
    client_page = ClientPage(drv)
    top_bar_page = TopBarPage(drv)
    common_actions = CommonActions(page, login_page, top_bar_page)
    backoffice_page = BackofficeSidebarButtons(drv)
    dashboards_page = DashboardsPage(drv)
    deposits_page = DepositsPage(drv)
    account_page = AccountPage(drv)
    withdrawals_page = WithdrawalsPage(drv)
    setup_platforms = SetupPlatforms(drv, app_config, session, log)

    # send request to convert USD to EUR
    log.add_step("send request to convert USD to EUR")
    jsons.CUSTOM_CURRENCY_CONVERSION["currencyFrom"] = "USD"
    jsons.CUSTOM_CURRENCY_CONVERSION["currencyTo"] = "USD"
    jsons.CUSTOM_CURRENCY_CONVERSION["rateFrom"] = 0.92
    jsons.CUSTOM_CURRENCY_CONVERSION["rateTo"] = 1.09
    session.post(endpoints.CUSTOM_CURRENCY_CONVERSION, json=jsons.CUSTOM_CURRENCY_CONVERSION)

    # send request to convert USD to JPY
    log.add_step("send request to convert USD to JPY")
    jsons.CUSTOM_CURRENCY_CONVERSION["currencyFrom"] = "USD"
    jsons.CUSTOM_CURRENCY_CONVERSION["currencyTo"] = "JPY"
    jsons.CUSTOM_CURRENCY_CONVERSION["rateFrom"] = 131.31
    jsons.CUSTOM_CURRENCY_CONVERSION["rateTo"] = 0.0076
    session.post(endpoints.CUSTOM_CURRENCY_CONVERSION, json=jsons.CUSTOM_CURRENCY_CONVERSION)

    agreement_title = settings.RANDOM_STRING
    log.add_step(f"created an agreement {agreement_title}")
    preliminary_steps.create_agreement(agreement_title)

    # create payment system
    payments.create_payment_system(title=settings.RANDOM_STRING + " payment system", deposit_commission_amount=0)

    # get new payment system id
    new_payment_system_id = payments.get_payment_system_id_by_title(title=settings.RANDOM_STRING + " payment system")
    log.add_step(f"created payment system with id {new_payment_system_id}")

    # create payment method
    new_payment_method_id = payments.create_payment_method(
        payment_method_title=settings.RANDOM_STRING + " payment method", payment_system_id=new_payment_system_id)
    log.add_step(f"created payment method with id {new_payment_method_id}")

    # new user creds
    user_phone_number = "+996502" + random_phone(phone_length=6)
    user_email = random_fake_email()

    # create new user
    create_new_user = CreateNewUser(session, user_email, user_phone_number)
    create_new_user.create_new_user()

    log.add_step(f"create new user with email: {user_email}")
    log.add_step(f"and phone: {user_phone_number}")

    # update creds for user session
    jsons.AUTH_PAYLOAD["emailOrPhone"] = user_email

    # instantiate user session
    user_session = ApiMethods(app_config.url)
    user_session.get_authorized(jsons.AUTH_PAYLOAD)

    trading_accounts = TradingAccounts(log=log, page=page, session=session, user_session=user_session,
                                       common_actions=common_actions, client_page=client_page,
                                       backoffice_page=backoffice_page, dashboards_page=dashboards_page,
                                       deposits_page=deposits_page, account_page=account_page,
                                       withdrawals_page=withdrawals_page)

    # Setup Servers, Groups, Types
    setup_platforms.configure_servers_groups_types_for_mt4()

    # create real mt4 account
    real_mt4_account_id, real_mt4_account_number = trading_accounts.create_real_account_with_api(account_type='4')
    log.add_step(f"created a mt4 real account with number {real_mt4_account_number}, and id {real_mt4_account_id}")

    # login as new user
    common_actions.login_as_user(user_email)
    log.add_step(f"login as {user_email}")

    # deposit 1000 USD to account
    first_deposit_id = trading_accounts.deposit_to_real_account(account_number=real_mt4_account_number, value="1000")
    log.add_step(f"deposit 1000 USD to {real_mt4_account_number}, payment id: {first_deposit_id}")

    # execute deposit
    session.post(endpoints.EXECUTE_DEPOSIT % first_deposit_id)

    # make withdrawal
    withdrawal_id = trading_accounts.make_withdrawal_with_api(account_number=real_mt4_account_number,
                                                                        value="920",
                                                                        payment_method_id=new_payment_method_id)
    # confirm withdrawal
    session.post(endpoints.CONFIRM_WITHDRAWAL % withdrawal_id)

    # execute withdrawal
    session.post(endpoints.EXECUTE_WITHDRAWAL % withdrawal_id)

