
import qrcode

url = 'https://github.com/jeferson-mendes'

qr = qrcode.QRCode(
    version=1,
    box_size=4,
    border=5
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.show()
