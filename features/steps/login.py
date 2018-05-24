from behave import *

import operator


use_step_matcher("parse")

@given(u'Exists a user "default_artist" with password "123pass"')
def step_impl(context):
    from django.contrib.auth.models import User
    User.objects.create_user(username="user", email='user@example.com', password="password")

@given(u'I login as user "user" with password "password"')
def step_impl(context):
    context.browser.visit(context.get_url('/accounts/login'))
    context.browser.fill('usernamelogin', "user")
    context.browser.fill('passwordlogin', "password")

@when(u'I log in')
def step_impl(context):
    form = context.browser.find_by_tag('form').first
    form.find_by_name('login').first.click()

@then(u'I get redirected to the homepage')
def step_impl(context):
    assert context.browser.url == context.get_url('/current/events/')
