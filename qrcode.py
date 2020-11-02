import qrcode
code = input('Enter the link or text:')
img=qrcode.make(code)
img.save('qrcode_test.png')