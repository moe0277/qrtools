#!/usr/bin/env python
#
import segno
from segno import helpers

def getMeCard(lastname, firstname, email, phone, url=""):
    mecard = helpers.make_mecard_data(name=lastname+", "+firstname, email=email, phone=phone)
    return mecard

def getQrCode(mecard):
    return segno.make(mecard, error='H')
   
def getQrCodeInline(qrcode, dark='red'):
    return qrcode.svg_inline(dark=dark, scale=4)

def getWifiQrCode(ssid, password):
    return helpers.make_wifi(ssid=ssid, password=password, security="wpa2")

if __name__ == "__main__":
    mc = getMeCard("Doe", "Moe", "moe.doe@oracle.com", "555-1212", "http://www.linkedin.com/in/moedoe01")

    wc = getWifiQrCode("sky", "airdoggz")
    print(wc)
