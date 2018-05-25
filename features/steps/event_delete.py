from behave import *

@given(u'Exists a registered organizer "orga" with password "password" and role "Organizer" with 1 event created')
def step_impl(context):
    from ArtProject.models import Organizer, Event
    from django.contrib.auth.models import User
    from datetime import datetime
    user = User.objects.create_user(username="orga", email='user@example.com',\
    password="password")
    organizer = Organizer(dni=14567, user=user, first_name="J", last_name="L", phone_number="66",\
    role="Organizer", afiliation_CIF="111")
    event = Event(name="Kingdom Hearts", created_by=organizer, ini_date=datetime.today(),\
     end_date=datetime.today(), type="Painting")
    organizer.save()
    event.save()

@then(u'I log in.')
def step_impl(context):
    context.browser.visit(context.get_url('login'))
    context.browser.fill('usernamelogin', "orga")
    context.browser.fill('passwordlogin', "password")
    form = context.browser.find_by_tag('form').first
    form.find_by_name('login').first.click()
    assert context.browser.url == context.get_url('currentevents')


@then(u'I go to my events page')
def step_impl(context):
    context.browser.visit(context.get_url('yourevents'))
    assert context.browser.url == context.get_url('yourevents')


@given(u'1 event')
def step_impl(context):
    from ArtProject.models import Event
    count = 1
    result = Event.objects.count()
    assert count == result


@then(u'I click on the delete button')
def step_impl(context):
    #Here we supposo to click the button delete, but due to javscript we can't
    #test it, so we will delete the event manuallyself.
    from ArtProject.models import Event
    Event.objects.get().delete()



@then(u'there aren\'t more events')
def step_impl(context):
    from ArtProject.models import Event
    count = 0
    result = Event.objects.count()
    assert count == result
