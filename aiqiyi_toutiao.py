#!/usr/bin/env python
# !coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
import hashlib
import random

def cmd5x(str):
    vf = hashlib.new('md5', str + '3sj8xof48xof4tk9f4tk9ypgk9ypg5ul').hexdigest()
    return vf


def getPcVf(str):
    vf = hashlib.new('md5', str + 'u6fnp3eok0dpftcq9qbr4n9svk8tqh7u').hexdigest()
    return vf


def getPcIbt(str):
    vf = hashlib.new('md5', str + 't6hrq6k0n6n6k6qdh6tje6wpb62v7654').hexdigest()
    return vf


def split_param(param):
    res = ""
    for k,v in param.items():
        res+= k+"="+str(v)+"&"
    return res

#纳豆播放页面的vf算法
def get_vf(tvid,vid,t):
    a = tvid
    b = vid
    c = {
        "uid":"",
        "cupid":"",
        "platForm":"h5",
        "qyid":"",
        "agenttype":"13",
        "type":"mp4",
        "nolimit":"",
        "k_ft1":"8",
        "rate":"2",
        "sgti":"13_12e9e055c713deba092399c62d8cb2b2_1489561211612",
        "qdv":"1",
        "qdx":"n",
        "qdy":"x",
        "qds":"0",
        "__jsT":"sgve",
        "t":t,
        "src":"02020031010000000000",
        "callback":"tmtsCallback"
    }
    print split_param(c)
    src = "/jp/tmts/" + a + "/" + b + "/?" + split_param(c)
    vf =  cmd5x(src)
    return src,vf




if __name__ == '__main__':
    tvid = "12476488409"
    vid = "12476488409"
    host = "http://cache.m.iqiyi.com"
    head = "/jp/tmts/%s/%s/"%(tvid,vid)
    src,vf = get_vf(tvid, vid, int(time.time())*1000)
    print host + src + '&vf=' + vf
