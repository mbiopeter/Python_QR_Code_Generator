# Install all the libraies needed: qrcode, Image
# ceate a function that collect a text and convert it into a qr code
# Save the qr code as an image
# call the function

import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,

    )
    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill = "black", back_color = "white")
    img.save("youtube.png")

generate_qrcode("https://www.youtube.com/channel/UCnmwh432bC8Rx704mjyB_Lw")