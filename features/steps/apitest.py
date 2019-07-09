from behave import *

from bin.apicalls import *


@given(u'I set base URL to "{base_url}"')
def set_base_url(context, base_url):
    if base_url.startswith("context"):
        context.base_url = context.settings['base_url']
        logger.info("Setting Base url : {}".format(context.base_url))


@when(u'I make a "{api_type}" request to "{url_path}"')
def request_call(context, api_type, url_path):
    url = context.base_url + url_path
    context.resp = fetch_api_response(api_type, url)


@then(u'the response status code should equal "{exp_status_code}"')
def status_code_check(context, exp_status_code):
    assert context.resp.status_code == int(exp_status_code)
    logger.info("Response code received : {}".format(context.resp.status_code))

@then(u'the response status message should equal "{msg}"')
def status_msg_check(context, msg):
    assert context.resp.reason == msg, "Invalid message received - {}".format(context.resp.reason)
