import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

url = 'https://faslala.github.io/curriculovitae/'
text = 'Exemplo de texto no qrCode.'

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data(url)
qr.add_data(text)
qr.make(fit=True)

image_qrcode = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), color_mask=RadialGradiantColorMask())
image_qrcode.save('curriculo_Faslala.png')
image_qrcode.save('text.png')