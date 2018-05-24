from behave import *


use_step_matcher("parse")

@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    # context.browser.visit(context.get_url('/accounts/login'))
    # context.browser.find_by_value('New box').click()
    pass
