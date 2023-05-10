import qrcode

qr_data = 'https://naver.com'
qr_img = qrcode.make(qr_data)

save_path = 'QR생성기.png'
qr_img.save(save_path)