from behave import *


@given(u'Exists a registered artist "artiste" with password "password" with 1 artwork')
def step_impl(context):
    from ArtProject.models import Artist, Artwork
    from django.contrib.auth.models import User
    from datetime import datetime
    user = User.objects.create_user(username="artiste", email='user@example.com',\
    password="password")
    artist = Artist(dni=14567, user=user, first_name="J", last_name="L", phone_number="66",\
    role="Artist", bank_account="111")
    artwork = Artwork(name="KH", artist=artist, price=10, image="/artwork/41022.png", \
    state=1, art_type="Painting")
    artist.save()
    artwork.save()

@then(u'I log in as an artist')
def step_impl(context):
    context.browser.visit(context.get_url('login'))
    context.browser.fill('usernamelogin', "artiste")
    context.browser.fill('passwordlogin', "password")
    form = context.browser.find_by_tag('form').first
    form.find_by_name('login').first.click()

@when(u'I\'m in the current events page')
def step_impl(context):
    assert context.browser.url == context.get_url('currentevents')

@when(u'there\'s 1 event')
def step_impl(context):
    from ArtProject.models import Organizer, Event
    from django.contrib.auth.models import User
    import datetime

    ini_date = datetime.date(2017, 4, 1)
    end_date = datetime.date(2019, 6, 1)

    user = User.objects.create_user(username="orga", email='user@example.com',\
    password="password")
    organizer = Organizer(dni=14567, user=user, first_name="J", last_name="L", phone_number="66",\
    role="Organizer", afiliation_CIF="111")
    event = Event(name="Kingdom Hearts", created_by=organizer, ini_date=ini_date,\
     end_date=end_date, type="Painting")
    organizer.save()
    event.save()
    assert Event.objects.count() == 1


@when(u'I enter in')
def step_impl(context):
    from ArtProject.models import Event
    event = Event.objects.get()
    context.browser.visit(context.get_url('/visit/event/' + str(event.pk)))
    assert context.browser.url == context.get_url('/visit/event/' + str(event.pk))


@when(u'there are not any artworks')
def step_impl(context):
    from ArtProject.models import Event
    event = Event.objects.get()
    assert str(event.artwork) == "ArtProject.Artwork.None"


@then(u'I go back to current events')
def step_impl(context):
    context.browser.visit(context.get_url('currentevents'))
    assert context.browser.url == context.get_url('currentevents')


@then(u'I select add artwork to an event')
def step_impl(context):
    from ArtProject.models import Event
    event = Event.objects.get()
    context.browser.visit(context.get_url('/add/artwork/' + str(event.pk)))
    assert context.browser.url == context.get_url('/add/artwork/' + str(event.pk))


@then(u'I select one of my artworks of the same type as the event')
def step_impl(context):
    from ArtProject.models import Artwork
    artwork = Artwork.objects.get()
    context.browser.select('artwork', artwork.artwork_id)
    form = context.browser.find_by_tag('form').first
    form.find_by_name('add').first.click()
    assert context.browser.url == context.get_url('currentevents')


@then(u'There are 1 artworks in the event')
def step_impl(context):
    from ArtProject.models import Event
    event = Event.objects.get()
    print (event.artwork)
    assert str(event.artwork) == "ArtProject.Artwork.None"
