from behave import *

organizer = None

@given(u'Exists an organizer "user1" with password "password" and role "Organizer"')
def step_impl(context):
    from ArtProject.models import Organizer
    from django.contrib.auth.models import User
    user = User.objects.create_user(username="user1", email='user@example.com',\
    password="password")
    organizer = Organizer(dni=14567, user=user, first_name="J", last_name="L", phone_number="66",\
    role="Organizer", afiliation_CIF="111")
    organizer.save()

@then(u'I do the login')
def step_impl(context):
    context.browser.visit(context.get_url('login'))
    context.browser.fill('usernamelogin', "user1")
    context.browser.fill('passwordlogin', "password")
    form = context.browser.find_by_tag('form').first
    form.find_by_name('login').first.click()

@given(u'I\'m logged as user "user1" with password "password"')
def step_impl(context):
    context.browser.visit(context.get_url('createevent'))
    assert context.browser.url == context.get_url('createevent')

@when(u'I post events')
def step_impl(context):
    from datetime import datetime
    from datetime import date
    dt = str(datetime.today())
    context.browser.fill('name', "KH")
    context.browser.fill('ini_date', dt)
    context.browser.fill('end_date', dt)
    context.browser.select('type', "Painting")
    form = context.browser.find_by_tag('form').first
    form.find_by_id('button').first.click()

@then(u'I get redirected to create event')
def step_impl(context):
    assert context.browser.url == context.get_url('createevent')
