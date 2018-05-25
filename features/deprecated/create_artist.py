from behave import *


use_step_matcher("parse")

# @given(u'I want to create a new user "new_artist" with password "123pass"')
# def step_impl(context):
#     context.browser.visit(context.get_url('/accounts/signup'))
#     context.browser.fill('username', "new_artist")
#     context.browser.fill('password', "123pass")

@when(u'I fill the fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill the fields')

@when(u'I click on create user:')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on create user:')

@then(u'I get redirected to my homepage')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I get redirected to my homepage')
