import logging

import requests

logger = logging.getLogger('APITest')


def timeit(f):
    def wrapper(*args, **kwargs):
        logger.info("Calling API: {}".format(args[1]))
        resp = f(*args, **kwargs)
        logger.info("Time taken for the call: {}s".format(round(resp.elapsed.total_seconds(), 3)))
        return resp

    return wrapper


@timeit
def fetch_api_response(api_type, url, *args, **kwargs):
    if api_type == "POST":
        response = requests.post(url, data=kwargs.get('data', None), headers=kwargs.get('headers', None), verify=True)

    elif api_type == "GET":
        response = requests.get(url, headers=kwargs.get("headers", None))

    elif api_type == "PUT":
        response = requests.put(url, data=kwargs.get('data', None), headers=kwargs.get('headers', None), verify=True)

    elif api_type == "DELETE":
        response = requests.delete(url, data=kwargs.get('data', None), headers=kwargs.get('headers', None), verify=True)
    else:
        logger.error("Invalid API type call requested")
        raise TypeError("Invalid API type call requested")

    return response
