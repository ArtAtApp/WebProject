from behave import *

import operator


use_step_matcher("parse")

@given(u'Exists a user "user" with password "password"')
def step_impl(context):
    from ArtProject.models import Artist
    from django.contrib.auth.models import User
    user = User.objects.create_user(username="user", email='user@example.com',\
    password="password")
    artist = Artist(dni=1, user=user, first_name="J", last_name="L", phone_number="66",\
    role="Artist", bank_account="111")
    artist.save()

@given(u'I am in the login page')
def step_impl(context):
    context.browser.visit(context.get_url('login'))
    assert context.browser.url == context.get_url('login')

@given(u'I login as user "user" with password "password"')
def step_impl(context):
    context.browser.fill('usernamelogin', "user")
    context.browser.fill('passwordlogin', "password")

@when(u'I log in')
def step_impl(context):
    form = context.browser.find_by_tag('form').first
    form.find_by_name('login').first.click()

@then(u'I get redirected to the homepage')
def step_impl(context):
    assert context.browser.url == context.get_url('currentevents')
