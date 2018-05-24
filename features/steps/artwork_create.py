from behave import *

artist = None

@given(u'Exists an artist "user" with password "password" and role "Artist"')
def step_impl(context):
    context.browser.visit(context.get_url('/create/artwork'))


@when(u'I post artwork')
def step_impl(context):
    # context.browser.visit(context.get_url('/create/artwork'))
    #context.browser.select('role', 'Artist')
    form = context.browser.find_by_tag('form').first
    for row in context.table:
        for heading in row.headings:
            if heading == "name":
                context.browser.fill('name', "KH")
            elif heading == "price":
                context.browser.fill('price', 10)
            elif heading == "image":
                context.browser.fill('image', "/artworks/udl.png")
    context.browser.fill('art_type', "Painting")
    form.find_by_css('button.btn-success').first.click()
    # form.find_by_name('button').first.click()

@then(u'I\'m viewing the details page for artworks by "user"')
def step_impl(context):
    context.browser.visit(context.get_url('/your/artworks'))
    # assert context.browser.url == context.get_url('/your/artworks')

@then(u'There are 1 artworks')
def step_impl(context):
    from ArtProject.models import Artwork
    count = 1
    result = Artwork.objects.count()
    print str(result) + "    NAANANNAAN"
    assert count == result
