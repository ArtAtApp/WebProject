from behave import *

@given(u'Exists an artist "user1" with password "password" and role "Organizer"')
def step_impl(context):
    from django.contrib.auth.models import User
    user = User.objects.create_user(username="user1", email='user@example.com',\
    password="password")
    # artist = Artist(dni=478, user=user, first_name="J", last_name="O", phone_number="666",\
    # role="Organizer", bank_account="111")

@given(u'I\'m loged as user "user1" with password "password"')
def step_impl(context):
    context.browser.visit(context.get_url('127.0.0.1:8000/create/event'))
    # assert context.browser.url == context.get_url('createevent')

@when(u'I post events')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.config.server_url + '/create/event')
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
    form.find_by_css('button.btn-success').first.click()

@then(u'I\'m viewing the details page for events by "user1"')
def step_impl(context):
    context.browser.visit(context.get_url('/your/events'))

@then(u'There are 1 events')
def step_impl(context):
    from ArtProject.models import Event
    count = 1
    result = Event.objects.count()
    print str(result) + "    NAANANNAAN"
    assert count == result
