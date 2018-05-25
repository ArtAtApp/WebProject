# from behave import *
#
# import operator
#
#
# use_step_matcher("parse")
#
# @given(u'Exists a user "user" with password "password" f')
# def step_impl(context):
#     from django.contrib.auth.models import User
#     User.objects.create_user(username="user", email='user@example.com',\
#     password="password")
#
# @given(u'I am in the login page f')
# def step_impl(context):
#     context.browser.visit(context.get_url('/accounts/login'))
#
# @given(u'Given I login as user "user" with password "piss word" which is incorrect f')
# def step_impl(context):
#     context.browser.fill('usernamelogin', "user")
#     context.browser.fill('passwordlogin', "piss word")
#
# @when(u'I log in')
# def step_impl(context):
#     form = context.browser.find_by_tag('form').first
#     form.find_by_name('login').first.click()
#
# @then(u'I get redirected to the homepage f')
# def step_impl(context):
#     assert context.browser.url == context.get_url('/accounts/login')
