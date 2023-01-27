from fileinput import filename
from itertools import count
from PIL import Image
import os
import pandas as pd
from tqdm import tqdm


from_dir = "../shops_stuff"
to_dir = "./shops_stuff_for_learn"

df = pd.read_csv("./data.csv", delimiter=",")

# print(os.listdir(to_dir))

# print(len(os.listdir(to_dir + "_гг/val")))
print(df['articleType'].unique())

# os.exit(0)

# for x in os.listdir(to_dir + "_гг/train"):
#     if x not in os.listdir(to_dir + "_гг/val"):
#         print("dsfl" + x)

# urls_img = list()

# for id in df['id']:
#     urls_img.append("/" + str(id) + ".jpg")
# df['imageUrl'] = urls_img

new_df = df[['articleType','imageUrl']]
# new_df = df


# new_df.to_csv("./styles.csv", sep=",")



valid_class = new_df['articleType'].value_counts(dropna=False)
# print(valid_class)

# for key, value in valid_class.items():
#     if (value < 50) or (key == 'Мяч' or key == 'Костюм' or key == 'Комплект'):
#         #  or key == 'Лиф' or key == 'Трусы' or key == 'Сорочка' or key == 'Лонгслив')
#         del class_item[key]
#     else:
#         class_item[key] = value

# print(sorted(class_item.items(), reverse=True, key=lambda x: x[1]))


# new_class_items = dict()
# for k in new_df['articleType'].unique():
#     # print(k)
#     try:
#        new_df['articleType'][k == new_df['articleType']] = class_item[k]
#        new_class_items[k] = 0
#     except:
#         new_df = new_df[new_df['articleType'] != k]

print(new_df)

# print(class_item)
# print(len(class_item))

# print(class_item)
# print(len(class_item))

# for k in class_item.keys():
#     print(k)

new_df = new_df.sample(frac=1)

class_item = ['Бейсболка']
class_item_dict = dict()
for k in class_item:
    class_item_dict[k] = 0

if not os.path.isdir(to_dir):
    os.mkdir(to_dir)

for _, file_name in tqdm(enumerate(new_df.iterrows())):

    file_name = file_name[1]
    # to_path = to_dir + "/" + file_name['masterCategory']

    to_path = to_dir

    if file_name['articleType'] not in class_item:
        continue

    try:
        img = Image.open(from_dir + file_name['imageUrl'])

        class_item_dict[file_name['articleType']] += 1
        if file_name['articleType'] == 'Рюкзак' or file_name['articleType'] == 'Мешок' or file_name['articleType'] == 'Тайтсы' or file_name['articleType'] == 'Леггинсы':
            if class_item_dict[file_name['articleType']] > 150:
                continue
        if file_name['articleType'] == 'Футболка' or file_name['articleType'] == 'Топ':
            if class_item_dict[file_name['articleType']] > 175:
                continue
        if class_item_dict[file_name['articleType']] > 300:
            continue
        if class_item_dict[file_name['articleType']] % 6 == 0:
            to_path += '/val'
        else:
            to_path += '/train'

        if not os.path.isdir(to_path):
            os.mkdir(to_path)

        to_path += "/" + file_name['articleType']

        if not os.path.isdir(to_path):
            os.mkdir(to_path)

        saved = to_path + file_name['imageUrl']
        img.save(saved)
    except:
        img = 0
        continue

# if not os.path.isdir(to_dir):
#     os.mkdir(to_dir)

# for img in os.listdir(from_dir):
#     if img[-4:] == "jpeg":
#         saved = to_dir + "/" + img[:-5]
#     else:
#         saved = to_dir + "/" + img[:-4]
#     img = Image.open(from_dir +"/" + img)
#     # img.thumbnail(img.size)

#     img.save(saved)


# for class_name in tqdm(class_names):
#     count = 0
#     for i, file_name in enumerate(img_class_dir.items()):
#         if class_name == file_name[1] and file_name[0]!=39401 and file_name[0]!=39403 and file_name[0]!=21617:
#             if count % 6 != 0:
#                 dest_dir = os.path.join(work_dir+train_dir, class_name)
#             else:
#                 dest_dir = os.path.join(work_dir+val_dir, class_name)
#             count += 1
#             if (count > 300):
#                  break
#             shutil.copy(os.path.join(data_dir, str(file_name[0])+'.jpg'), os.path.join(dest_dir, str(file_name[0])+'.jpg'))