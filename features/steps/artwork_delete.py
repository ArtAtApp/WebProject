from behave import *

@given(u'Exists a registered organizer "user" with password "password" with 1 artwork created')
def step_impl(context):
    from ArtProject.models import Artist, Artwork
    from django.contrib.auth.models import User
    from datetime import datetime
    user = User.objects.create_user(username="user", email='user@example.com',\
    password="password")
    artist = Artist(dni=14567, user=user, first_name="J", last_name="L", phone_number="66",\
    role="Artist", bank_account="111")
    artwork = Artwork(name="KH", artist=artist, price=10, image="/artwork/41022.png", \
    state=1, art_type="Painting")
    artist.save()
    artwork.save()

@then(u'I log in as an artist.')
def step_impl(context):
    context.browser.visit(context.get_url('login'))
    context.browser.fill('usernamelogin', "user")
    context.browser.fill('passwordlogin', "password")
    form = context.browser.find_by_tag('form').first
    form.find_by_name('login').first.click()
    assert context.browser.url == context.get_url('currentevents')

@then(u'I go to my artwork page')
def step_impl(context):
    context.browser.visit(context.get_url('yourartworks'))
    assert context.browser.url == context.get_url('yourartworks')

@given(u'1 artwork')
def step_impl(context):
    from ArtProject.models import Artwork
    count = 1
    result = Artwork.objects.count()
    assert count == result

@then(u'I click on the delete button of the artwork')
def step_impl(context):
    context.browser.find_by_name('delete').first.click()

@then(u'there aren\'t more artwork')
def step_impl(context):
    from ArtProject.models import Artwork
    count = 0
    result = Artwork.objects.count()
    assert count == result
