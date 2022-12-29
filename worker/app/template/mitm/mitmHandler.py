from mitmproxy import http,ctx,dns
from mitmproxy.net.http.http1 import assemble

import os
REPORT_URL = os.environ.get('REPORT_URL') +'/log'
if not REPORT_URL:
    raise BaseException("No REPORT_URL found")


import requests as r


def response(flow: http.HTTPFlow) -> None:
    if flow.response.headers.get("content-type", "").startswith("image"):
        return
    data = {
        'type':'mitm-http',
        'data': {
            'host': flow.request.pretty_host,
            'method':flow.request.method,
            'path':flow.request.path,
            'url':flow.request.url,
            'req_raw':assemble.assemble_request(flow.request).decode('utf8','ignore'),
            'res_raw':assemble.assemble_response(flow.response).decode('utf8','ignore'),
            'status_code':flow.response.status_code,
            'scheme':flow.request.scheme,
        }
    }
    ctx.log.info(
        r.post(REPORT_URL,
            json = data
        ).text
    )
                

def dns_response(flow: dns.DNSFlow):
    data = {
        'type':'mitm-dns',
        'data': {
            'req': flow.dns_request.text,
            'res':flow.dns_response.text,
        }
    }
    ctx.log.info(
        r.post(REPORT_URL,
            json = data
        ).text
    )