#! /usr/bin/env python
#coding=utf-8

import requests
import strings
import json
import socket
import pickle

def GetIP():
    localIP = requests.get("http://ip.dnsexit.com/index.php")
    return localIP.text.strip()

def GetLocation():
    ip = GetIP()
    url = "http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip="+ip
    r = requests.get(url)
    return r.json()
    
def City_Code():
    with open('mydata.pickle', 'rb') as mysavedata:
        d = pickle.load(mysavedata)
    mysavedata.close()
    return d

weather_url = "http://www.weather.com.cn/adat/cityinfo/101021200.html"

 

if __name__ == '__main__':
    local = GetLocation()
    print 'You are in', local['country'], local['city']
    

    city = City_Code()
    
    print city[u'北京']
    
    
    #city_list2 = provinceNumber[local['city']]
    
    #city = requests.get(weather_url)
    #print city.text    