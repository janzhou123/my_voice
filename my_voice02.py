#-*- coding: utf-8 -*-
import wave
import urllib, urllib2, pycurl
import base64
import json
import os
import requests
def get_voice():
    Api_Key = "WEiOuW65sztplZMoxXQgHyGV"
    Secrect_Key = "707a647122a4d2e1d8bbcde317151e71"
    url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id='+Api_Key+'&client_secret='+Secrect_Key
    res = urllib2.urlopen(url).read()
    data = json.loads(res)
    token = data['access_token']    #获取的token
    print 'token获取成功：'+`token`
    cuid = "fe80:e5bb:8a3f:a804:6fa%12"
    srv_url = 'http://vop.baidu.com/server_api'
              # //+ '?cuid=' + cuid + '&token=' + token


    VOICE_RATE = 8000
    # WAVE_FILE = '123.wav'
    WAVE_FILE = 'test.pcm'
    USER_ID = 'duvoice'
    # WAVE_TYPE = 'wav'
    WAVE_TYPE = 'pcm'
    #其它参数可参考sdk文档

    f = open(WAVE_FILE,'r')
    speech = base64.b64encode(f.read()).replace('\n', '')
    size = os.path.getsize(WAVE_FILE)
    # update = json.dumps({'format':WAVE_TYPE,'rate':VOICE_RATE,'channel':1,'cuid':cuid,'token':token,'speech':speech,'len':size})
    # print update
    # r = urllib2.urlopen(srv_url,update)
    # # print  r
    #
    # t = r.read()
    # result = json.loads(t)
    # # print  json
    # print result

    # ===============================================================
    data = {'format':WAVE_TYPE,'rate':VOICE_RATE,'channel':1,'cuid':cuid,'token':token,'speech':speech,'len':size}
    # print data
    # print json.dumps(data)
    r = requests.post(srv_url, json=data, headers={'Content-Type': 'application/json'})
    # r = requests.post(srv_url, data=data)
    print r.text
    # print r.content



    # if result['err_msg']=='success.':
    #     word = result['result'][0].encode('utf-8')
    #     if word!='':
    #         if word[len(word)-3:len(word)]=='，':
    #             print word[0:len(word)-3]
    #             return word[0:len(word)-3]
    #         else:
    #             print word
    #             return word
    #     else:
    #         print "音频文件不存在或格式错误"
    #         return ''
    # else:
    #     print "错误"

if __name__ == "__main__":
    get_voice()