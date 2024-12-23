# https://hoboxr.github.io/Chrisamas/Merry-Christmas/

import qrcode

# 将 GitHub Pages 或 Coding Pages 的 URL 填入
url = "https://merrychrismas.yyhobo.xin/content/index.html/"

# 生成二维码
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# 创建二维码图像
img = qr.make_image(fill="black", back_color="white")

# 保存二维码图像
img.save("详情页.png")