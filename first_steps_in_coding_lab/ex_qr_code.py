import pyqrcode
import png
from pyqrcode import QRCode

address = "https://cryptobent.com"
url = pyqrcode.create(address)
url.png("cryptobent.png", scale=8)