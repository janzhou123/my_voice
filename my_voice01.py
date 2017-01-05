#-*- coding: utf-8 -*-
import wave
import urllib, urllib2, pycurl
import base64
import json
import os


## get access token by api key & secret key

def get_token():
    apiKey = "WEiOuW65sztplZMoxXQgHyGV"
    secretKey = "707a647122a4d2e1d8bbcde317151e71"

    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;

    res = urllib2.urlopen(auth_url)
    json_data = res.read()
    return json.loads(json_data)['access_token']


def dump_res(buf):
    print buf


## post audio to server
def use_cloud(token):
    # f = 'D:\\PycharmProjects\\my_voice\\123.wav'
    # fp = wave.open('123.wav', 'rb')
    # nf = fp.getnframes()
    # f_len = nf * 2
    # audio_data = fp.readframes(nf)
    # fp = open('test.pcm', 'rb')
    # # nf = fp.getnframes()
    # f_len = fp.tell()
    # audio_data = fp.read(f_len)

    VOICE_RATE = 8000
    WAVE_FILE = '123.wav'
    USER_ID = 'duvoice'
    WAVE_TYPE = 'wav'

    f = open(WAVE_FILE,'r')
    speech = base64.b64encode(f.read())
    size = os.path.getsize(WAVE_FILE)

    cuid = "fe80:e5bb:8a3f:a804:6fa%12"  # my xiaomi phone MAC
    srv_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + token
    http_header = [
        'Content-Type: audio/wav; rate=8000',
        'Content-Length: %d' % size
    ]

    c = pycurl.Curl()
    c.setopt(pycurl.URL, str(srv_url))  # curl doesn't support unicode
    # c.setopt(c.RETURNTRANSFER, 1)
    c.setopt(c.HTTPHEADER, http_header)  # must be list, not dict
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 30)
    c.setopt(c.TIMEOUT, 30)
    c.setopt(c.WRITEFUNCTION, dump_res)

    c.setopt(c.SPEECH, speech)
    c.setopt(c.LEN, size)
    c.perform()  # pycurl.perform() has no return val


if __name__ == "__main__":
    token = get_token()
    use_cloud(token)