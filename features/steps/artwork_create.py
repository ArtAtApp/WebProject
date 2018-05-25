from behave import *

@given(u'Exists a registered artist "user" with password "password" and role "Artist"')
def step_impl(context):
    from ArtProject.models import Artist
    from django.contrib.auth.models import User
    user = User.objects.create_user(username='user', email='user@example.com',\
    password='password')
    artist = Artist(dni=1, user=user, first_name='J', last_name='L', phone_number='66',\
    role='artist', bank_account='111')
    artist.save()

@then(u'I log in')
def step_impl(context):
    context.browser.visit(context.get_url('login'))
    context.browser.fill('usernamelogin', 'user')
    context.browser.fill('passwordlogin', 'password')
    form = context.browser.find_by_tag('form').first
    form.find_by_name('login').first.click()
    assert context.browser.url == context.get_url('currentevents')


@then(u'I go to the create artwork page')
def step_impl(context):
    context.browser.visit(context.get_url('create_artwork'))
    assert context.browser.url == context.get_url('create_artwork')

@when(u'I post artwork')
def step_impl(context):
    form = context.browser.find_by_tag('form').first
    context.browser.fill('name', 'KH')
    context.browser.fill('price', 10)
    context.browser.attach_file('image', '/home/rdc2/Escritorio/graph.png')
    context.browser.select('artwork_type', 'Painting')
    form.find_by_name('button').first.click()

@then(u'I\'m viewing the details page for artworks by "user"')
def step_impl(context):
    context.browser.visit(context.get_url('/your/artworks'))
    assert context.browser.url == context.get_url('/your/artworks')

@then(u'There are 1 artworks')
def step_impl(context):
    from ArtProject.models import Artwork
    count = 1
    result = Artwork.objects.count()
    print str(result) + '    NAANANNAAN'
    assert count == result
