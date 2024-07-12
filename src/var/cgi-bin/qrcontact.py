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
<title>QR Code Generator: MeCard Format</title>
</head>
<body>
<div align="center"> 
<img src="http://qrtools.elcaro.io/logo.jpg" alt="Oracle Logo">
<form action="/cgi-bin/qrcontact.py" method="get">
<table>
    <tbody>
    <tr><td>Last Name:</td><td><input type="text" name="lastname"></input></td></tr>
    <tr><td>First Name:</td><td><input type="text" name="firstname"></input></td></tr>
    <tr><td>E-mail:</td><td><input type="text" name="email"></input><td/></tr>
    <tr><td>Phone:</td><td><input type="text" name="phone"></input><td/></tr>
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
<title>QR Code Generator: MeCard Format</title>
</head>
<body>
<div align="center">
<img src="http://qrtools.elcaro.io/logo.jpg" alt="Oracle Logo" style="width:150px;height:125px;">
<p>Name: %s</p>
<p>Email: %s</p>
<p>Phone: %s</p>
<div>%s</div>
</div>
</body>
</html>
"""

print ("Content-type:text/html\r\n\r\n")

def main(): 

    form = cgi.FieldStorage()
    if "lastname" not in form or "firstname" not in form or "email" not in form or "phone" not in form:
        print (html1)
    else:
        mecard = qrgenerator.getMeCard(form["lastname"].value, form["firstname"].value, form["email"].value, form["phone"].value)
        qrcode = qrgenerator.getQrCode(mecard)
        qrcodeinline = qrgenerator.getQrCodeInline(qrcode)
        print (html2 % (form["firstname"].value+" "+form["lastname"].value, form["email"].value, form["phone"].value, qrcodeinline))

main()
