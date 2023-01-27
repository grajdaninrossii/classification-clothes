from PIL import Image
import os

# size = (540 * 1.2, 720 * 1.2)
# saved = "test_img.jpg"
# img = Image.open("1163.jpg")
# img.thumbnail(size)
# img.save(saved)
# img.show()

from_dir = "./fashion-dataset/compressed_imgs"
to_dir = "./fashion-dataset/compressed_imgs_for_deploy"
# повторный запуск mkdir с тем же именем вызывает FileExistsError,
# вместо этого запустите:
if not os.path.isdir(to_dir):
    os.mkdir(to_dir)

size = (540 * 0.8, 720 * 0.8)
for img in os.listdir(from_dir):
    saved = to_dir + "/" + img
    img = Image.open(from_dir +"/" + img)
    img.thumbnail(size)
    img.save(saved)
    # img.show()