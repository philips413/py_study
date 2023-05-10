import qrcode

file_path = r'qr코드모임.txt'
with open(file_path, 'rt', encoding='UTF8') as f :
    read_lines = f.readlines()
    for line in read_lines:
        line = line.split()
        print(line)

        qr_data = line
        qr_img = qrcode.make(qr_data)

        save_path = '111.png'
        qr_img.save(save_path)