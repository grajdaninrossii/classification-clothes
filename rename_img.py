from PIL import Image
import os

# size = (540 * 1.2, 720 * 1.2)
# saved = "test_img.jpg"
# img = Image.open("1163.jpg")
# img.thumbnail(size)
# img.save(saved)
# img.show()

from_dir = "../shops_stuff"
to_dir = "../shops_stuff_del_jpeg"
# повторный запуск mkdir с тем же именем вызывает FileExistsError,
# вместо этого запустите:
if not os.path.isdir(to_dir):
    os.mkdir(to_dir)

for img in os.listdir(from_dir):
    if img[-4:] == "jpeg":
        saved = to_dir + "/" + img[:-5] + ".jpg"
    else:
        saved = to_dir + "/" + img[:-4] + ".jpg"
    img = Image.open(from_dir +"/" + img)

    imgRGB = img.convert('RGB')
    # img.thumbnail(img.size)

    imgRGB.save(saved)
        # break
    # img.show()


https://drive.google.com/drive/folders/1k0DN_43Jgl1YxA8_ehkK_tOisMwekBoG?usp=sharing