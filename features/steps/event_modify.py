from behave import *

@given(u'Exists a registered organizer "usero" with password "password" with 1 event')
def step_impl(context):
    from ArtProject.models import Organizer, Event
    from django.contrib.auth.models import User
    from datetime import datetime
    user = User.objects.create_user(username="usero", email='user@example.com',\
    password="password")
    organizer = Organizer(dni=14567, user=user, first_name="J", last_name="L", phone_number="66",\
    role="Organizer", afiliation_CIF="111")
    event = Event(name="KH", created_by=organizer, ini_date=datetime.today(),\
     end_date=datetime.today(), type="Painting")
    organizer.save()
    event.save()

@then(u'I log in as an organizer')
def step_impl(context):
    context.browser.visit(context.get_url('login'))
    context.browser.fill('usernamelogin', "usero")
    context.browser.fill('passwordlogin', "password")
    form = context.browser.find_by_tag('form').first
    form.find_by_name('login').first.click()
    assert context.browser.url == context.get_url('currentevents')

@then(u'I go to my events detail page')
def step_impl(context):
    context.browser.visit(context.get_url('yourevents'))
    assert context.browser.url == context.get_url('yourevents')


@given(u'an event')
def step_impl(context):
    from ArtProject.models import Event
    count = 1
    result = Event.objects.count()
    assert count == result


@when(u'I click on the button "modify" of the event')
def step_impl(context):
    context.browser.find_by_name('modify').first.click()


@then(u'I get redirected to modify event page')
def step_impl(context):
    from ArtProject.models import Event
    event = Event.objects.get()
    assert context.browser.url == context.get_url('/modify/event/' + str(event.pk))


@then(u'I change it\'s name to')
def step_impl(context):
    context.browser.fill('name', "KingdomHearts")
    context.browser.find_by_name('modify').first.click()


@then(u'I got redirected to my events page')
def step_impl(context):
    assert context.browser.url == context.get_url('yourevents')


@then(u'I check the event\'s name has been modified')
def step_impl(context):
    from ArtProject.models import Event
    event = Event.objects.get()
    assert event.name == "KingdomHearts"
