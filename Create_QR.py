import qrcode

image = qrcode.make('https://mail.google.com/mail/u/0/#inbox')

image.save('qrcode.png')