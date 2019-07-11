import json

import jpath
from behave import *

from utils.apicalls import *


@given(u'I set base URL to "{base_url}"')
def set_base_url(context, base_url):
    if base_url.startswith("context"):
        context.base_url = context.settings['base_url']
        logger.info("Base url set to : {}".format(context.base_url))


@when(u'I make a "{api_type}" request to "{url_path}"')
def request_call(context, api_type, url_path):
    url = context.base_url + url_path
    context.resp = fetch_api_response(api_type, url)


@when(u'I make a "{api_type}" request to "{url_path}" with {params}')
def request_call_params(context, api_type, url_path, params):
    url = context.base_url + url_path
    params = json.loads(json.dumps(params))
    logger.info("Sending request with params : {}".format(params))
    context.resp = fetch_api_response(api_type, url, params=params)


@then(u'the response status code should equal "{exp_status_code}"')
def status_code_check(context, exp_status_code):
    assert context.resp.status_code == int(exp_status_code), "Unexpected return code :{}".format(
        context.resp.status_code)
    logger.info("Response code received : {}".format(context.resp.status_code))


@then(u'the response status message should equal "{msg}"')
def status_msg_check(context, msg):
    assert context.resp.reason == msg, "Invalid message received - {}".format(context.resp.reason)


@then(u'value at jsonpath "{json_path}" in response should be "{exp_value}"')
def step_impl(context, json_path, exp_value):
    data = context.resp.json()
    logger.debug(data)
    actual_value = jpath.get(json_path, data)
    logger.debug("Actual value from response: {}".format(actual_value))
    assert str(actual_value) == str(exp_value), "Mismatch found Exp value :{}, Actual value: {}".format(exp_value,
                                                                                                        actual_value)
    logger.info("Pattern \"{}\" found in response".format(exp_value))


@then(u'value at jsonpath "{json_path}" in response should contain "{exp_value}"')
def step_impl(context, json_path, exp_value):
    data = context.resp.json()
    logger.debug(data)
    actual_value = jpath.get(json_path, data)
    logger.debug("Actual value from response: {}".format(actual_value))
    assert exp_value in actual_value, "Pattern not found in response Pattern :{}, Actual value: {}".format(exp_value,
                                                                                                           actual_value)
    logger.info("Pattern \"{}\" found in response".format(exp_value))
