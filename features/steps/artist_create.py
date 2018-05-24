from behave import *

import operator


use_step_matcher("parse")

@when(u'I fill all the fields correctly')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill all the fields correctly')

@then(u'the user is created successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user is created successfully')
