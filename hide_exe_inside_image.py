
with open('main_image.jpg', 'ab') as f, open("procexp.exe", 'rb') as e:
    f.write(e.read())