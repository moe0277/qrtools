#!/usr/bin/env python
import qrgenerator
import cgi
import cgitb
cgitb.enable()

html1="""<!DOCTYPE html>
<html>
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-E71J0ZQ2N2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-E71J0ZQ2N2');
</script>
<title>QR Code Generator: WiFi Format</title>
</head>
<body>
<div align="center"> 
<img src="http://qrtools.elcaro.io/wifi.svg" alt="Wifi Logo" style="width:150px;height:125px;">
<form action="/cgi-bin/qrwifi.py" method="get">
<table>
    <tbody>
    <tr><td>SSID:</td><td><input type="text" name="ssid"></input></td></tr>
    <tr><td>Password:</td><td><input type="text" name="password"></input></td></tr>
    <tr><td colspan=2 align='right'><input type="submit"></input></td></tr>
    </tbody>
</table>
</form>
</div>
</body>
</html>
"""

html2="""<!DOCTYPE html>
<html>
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-E71J0ZQ2N2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-E71J0ZQ2N2');
</script>
<title>QR Code Generator: WiFi Format</title>
</head>
<body>
<div align="center">
<img src="http://qrtools.elcaro.io/wifi.svg" alt="Wifi Logo" style="width:150px;height:125px;">
<p>ssid: %s</p>
<p>password: %s</p>
<div>%s</div>
</div>
</body>
</html>
"""

print ("Content-type:text/html\r\n\r\n")

def main(): 

    form = cgi.FieldStorage()
    if "ssid" not in form or "password" not in form:
        print (html1)
    else:
        qrcode = qrgenerator.getWifiQrCode(form["ssid"].value, form["password"].value)
        qrcodeinline = qrgenerator.getQrCodeInline(qrcode, 'black')
        print (html2 % (form["ssid"].value, form["password"].value, qrcodeinline))

main()
