#! /usr/bin/env python3

import urllib.parse
import urllib.request

url = 'http://vps.beta.ule.com/feedback/doFeedback!doFeedback.do'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {
'content' : 'fsfdfsfsasfda'
}

cookie = "vpsService_villageNo=98335433; token=0j82coBbTyWTopfUa3y9wj%2Fzf0WnOWS0"
header={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding":"utf-8",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Host":"ule.com",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Referer":"",
    "Cookie":cookie,
    "Connection":"keep-alive"
    }


data = urllib.parse.urlencode(values).encode(encoding='UTF8')
req = urllib.request.Request(url, data,header)
#req.add_header('User-Agent',user_agent)
response = urllib.request.urlopen(req)
the_page = response.read()

print(the_page.decode("utf8"))
