import logging
from mitmproxy import http
from mitmproxy.http import Headers

def request(flow: http.HTTPFlow):
    if "SEC" in flow.request.headers:
        logging.info("SEC TOKEN RECOVERED: " + flow.request.headers["SEC"])
