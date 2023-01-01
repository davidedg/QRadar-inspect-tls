import logging

from mitmproxy.utils import strutils
from mitmproxy import tcp
import re

class WCollectTokensIntercept:
    def __init__(self):
        self.WCOLLECT_TOKEN_REGEX = r"(\$(\{?[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}\}?))"
        self.WCOLLECT_re = re.compile(self.WCOLLECT_TOKEN_REGEX, re.ASCII + re.IGNORECASE)

    async def tcp_message(self, flow: tcp.TCPFlow):
        message = flow.messages[-1]
        if not message.from_client: return
        if (len(message.content) < 60): return

        r = self.WCOLLECT_re.search(strutils.bytes_to_escaped_str(message.content))
        if not r: return

        t = r.group(2)
        if t: logging.info("WCOLLECT TOKEN RECOVERED: " + t)


addons = [WCollectTokensIntercept()]
