#-*- coding: utf-8 -*-

import base64, requests
d = open('D:\\PycharmProjects\\my_voice\\234.wav', 'rb').read()
# d = open('D:\\PycharmProjects\\my_voice\\123.pcm', 'rb').read()
data = {
    # "format": "pcm",
    "format": "wav",
    "rate": 16000,
    "channel": 1,
    "token": "24.9e2b89db72fe262284a6a783e9daefd2.2592000.1486194211.282335-9165197",
    "cuid": "fe80:e5bb:8a3f:a804:6fa%12",
    "len": len(d),
    "speech": base64.encodestring(d).replace('\n', '')
}
result = requests.post('http://vop.baidu.com/server_api', json=data, headers={'Content-Type': 'application/json'})
# print result.text
data_result = result.json()
# print data_result
print data_result['err_msg']
if data_result['err_msg']=='success.':
    print "语音结果：" + data_result['result'][0].encode('utf-8')
else:
    print data_result



