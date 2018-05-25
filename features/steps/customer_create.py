from behave import *

@given(u'I am in the sign up page')
def step_impl(context):
    context.browser.visit(context.get_url('signup'))
    assert context.browser.url == context.get_url('signup')

@when(u'I\'ll fill all the fields correctly')
def step_impl(context):
    context.browser.select('role', "Customer")
    context.browser.fill('usernamesignup', "user")
    context.browser.fill('passwordsignup', "password")
    context.browser.fill('emailsignup', "def@def.com")
    context.browser.fill('dnisignup', "48004800C")
    context.browser.fill('firstnamesignup', "Goldsberg")
    context.browser.fill('lastnamesignup', "Shekelstein")
    context.browser.fill('phonenumbersignup', "657282716")
    context.browser.fill('bank_account_signup', "785632")
    form = context.browser.find_by_tag('form').first
    form.find_by_name('signup').first.click()

@then(u'my user is created successfully')
def step_impl(context):
    assert context.browser.url == context.get_url('currentevents')
