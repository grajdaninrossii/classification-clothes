from itertools import count
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import pandas as pd

import re



server_url = "/"

def fill_category(cursor):
    query = """INSERT INTO category (NAME) VALUES (%s)"""
    cursor.execute(query, (["test"]))

def fill_articles(cursor):
    fill_category(cursor)
    arts = [
        (
            "Громкое возвращение нулевых, актуальные босоножки на платформах, безупречные трикотажные костюмы и самый модный тигровый принт",
            server_url + "arts/newTrends.html",
            "20 главных трендов весны и лета 2022: самый полный гид",
            server_url + "arts/images/moda-nulevyh-zanizhennaja-talija-plamennyj-privet-iz-nulevyh--9.jpg",
            1
        ),
         (
            "Что такое мода и стиль, чем эти понятия отличаются — именно об этом наша сегодняшняя статья.",
            server_url + "arts/WhatIsFashion.html",
            "Мода или стиль — что выбрать?",
            server_url + "arts/images/belye-tufli-16.jpg",
            1
        ),
         (
            "Нет такого дизайнера, кто бы ни разу не цитировал своих предшественников. Переложить хорошо забытое старое на новый лад – излюбленный прием и Джереми Скотта, и Карла Лагерфельда, и Николя Жескьера...",
            server_url + "arts/GuideFashionableEras.html",
            "Гид по модным эпохам?",
            server_url + "arts/images/moda20vek.jpg",
            1
        ),
         (
            "Включите фантазию, наберитесь немного смелости, учтите следующие советы и подберите свой собственный стиль.",
            server_url + "arts/FindYourStyle.html",
            "10 советов, как найти свой собственный стиль",
            server_url + "arts/images/yourStyle.jpg",
            1
        ),
         (
            "Даже если мы не знаем четкого определения, все же можем практически не задумываясь сказать, кто такие «харизматичные личности», какие качества им присущи.",
            server_url + "arts/FemaleСharisma.html",
            "Женская харизма",
            server_url + "arts/images/715527724-charlize-theron-deixa-gorjeta-generosa-1024x576.jpg",
            1
        ),
         (
            "Сегодня поговорим о сравнительно новом явлении в русскоязычном модном пространстве - о фэмили лук (Family look)...",
            server_url + "arts/FamilyStyle.html",
            "Фэмили лук: как стильно одеваться паре и семье? Идеи 2022/2023",
            server_url + "arts/images/family-look.jpg",
            1
        ),
        ]
    query = """INSERT INTO article (DESCRIPTION, URL, TITLE, IMAGE_URL, CATEGORY_ID) VALUES (%s, %s, %s, %s, %s)"""
    for q in arts:
        cursor.execute(query, q)

def fill_quote(cursor):
    quotes = [
        ("Для того, чтобы быть незаменимой, нужно быть разной.", "Коко Шанель"),
        ("Мода не просто делает женщин красивыми, она дает им уверенность в себе.", "Ив Сен-Лоран"),
        ("Чистые, сильные эмоции. Это не о дизайне. Это о чувствах.", "Альбер Эльбаз"),
        ("Когда вы слышите, что дизайнеры жалуются на проблемы своей профессии, скажите: Не увлекаетесь, это всего лишь платья.", "Карл Лагерфельд"),
        ("Мода - это не о лейблах. И не о брендах. Это о чем-то еще, что происходит внутри нас.", "Ральф Лорен"),
        ("Мы никогда не должны путать элегантность со снобизмом.", "Ив Сен-Лоран"),
        ("Девочки одеваются не для мальчиков. Они одеваются для себя и, конечно, друг для друга. Если бы девочки одевались для мальчиков, они бы так и ходили все время голыми.", "Бетси Джонсон"),
        ("Женское платье должно быть сродни колючей проволоке: делать свое дело, не портя пейзаж.", "Софи Лорен"),
        ("Стиль – это простой способ говорить о сложных вещах.", "Жан Кокто"),
        ("Дайте девушке правильные туфли, и она сможет покорить мир.", "Мерилин Монро")
    ]
    query = """INSERT INTO quotes (VALUE, AUTHOR) VALUES (%s, %s)"""
    for q in quotes:
        cursor.execute(query, q)


def fill_gender(cursor):
    # roles = ["Men", "Women", "Children"]
    gender = list(stuff['gender'].unique())
    query = """INSERT INTO gender (GENDER_NAME) VALUES (%s)"""
    for r in gender:
        cursor.execute(query, tuple([r]))

def fill_version(cursor):
    version = ("0.0.1", "0.0.1")
    new_version = ("0.0.2", "0.0.2")
    current_version = ("0.0.3", "0.0.3")
    query = """INSERT INTO app_versions (ACTUAL_VERSION_NUMBER, MIN_ACTUAL_VERSION_NUMBER) VALUES (%s, %s)"""
    cursor.execute(query, version)
    cursor.execute(query, new_version)
    cursor.execute(query, current_version)

def fill_stuff(cursor):
    # Добавляем наши шмотки
    insert_stuff_query = """ INSERT INTO shop_stuff (ID, PRODUCT_DISPLAY_NAME, GENDER_ID,
                             ARTICLE_TYPE,MASTER_CATEGORY, BASE_COLOR, SEASON, USAGE,
                             IMAGE_URL, STORE_LINK)
                             VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    # ,productDisplayName,gender,masterCategory,articleType,baseColor,season,usage,imageUrl,urlSource
    for _, row in stuff.iterrows():
        stf = row.tolist()
        # print(stf)
        if stf[2] == "Women":
            stf[2] = 2
        elif stf[2] == "Children":
            stf[2] = 3
        else:
            stf[2] = 1
        stf = tuple(stf)
        cursor.execute(insert_stuff_query, stf)

def fill_roles(cursor):
    roles = ["ROLE_USER", "ROLE_MODERATOR", "ROLE_ADMIN"]
    query = """INSERT INTO roles (NAME) VALUES (%s)"""
    for r in roles:
        cursor.execute(query, tuple([r]))

def fill_style_user(cursor):
    phases = [
        "Городской стиляга 🦾",
        "Классик 🥸",
        "Неформат 🎃",
        "Межстильный 👽",
        "На спорте 🧘🏻",
        "На веселе 🥳",
        "Яркий 🤩"
    ]
    query = """INSERT INTO style_user (NAME) VALUES (%s)"""
    for r in phases:
        cursor.execute(query, tuple([r]))

def master_category():
    global stuff
    count = 0
    for id, row in stuff.iterrows():
        pattern = 'поло'

        if pattern in row['masterCategory'].lower():
            stuff['masterCategory'][id] = "Футболка"

        # row['masterCategory' == pattern]['masterCategory'] = row['masterCategory' == pattern]['productDisplayName'].split(" ")[0]
        # pattern = 'Лонгслив'
        # if pattern == row['masterCategory']:
        #     # count += 1
        #     stuff['masterCategory'][id] = 'Лонгслив'

    #     stuff['masterCategory'][id] = row['productDisplayName'].split(" ")[0]
    # print(count)
        # print(_)

    print("masterCategory: ", pd.unique(stuff['masterCategory']).size)
    # print()
    count =0
    for key, x in stuff['masterCategory'].value_counts(dropna=False).items():

        if x > 50:
            count+=1
            print(key, x)
        # print(key, x)

    print(count)
    # print("baseColor: ", stuff['masterCategory'=='']['season'].value_counts(dropna=False))




#     count = 0
#     stuff['season'] = stuff['season'].fillna('-')
#     for key, x in stuff.iterrows():

#         if x['season'] == '-':
#             for k, v in stuff_master_categofy.items():
#                 if k == x['masterCategory']:
#                     stuff['season'][key] = v

#                     count+=1

#         if x['season'] == '-' or x['season'] == 'Для мальчиков':
#             stuff['season'][key] = 'демисезон'

#     print(count)



# --------------------------Начало ---------------------------
stuff = pd.read_csv("./data.csv", delimiter=",")
print(stuff['articleType'].head())

# master_category()


# master_category()



# del stuff['Unnamed: 0']
# stuff.to_csv("./data.csv", sep=",")

# print("masterCategory: ", stuff['masterCategory'].value_counts(dropna=False)[stuff['masterCategory'].value_counts(dropna=False) > 50].size)
# del stuff['year']
# del stuff['subCategory']

# stuff['masterCategory'] = stuff




# print(len(pd.unique(stuff["subCategory"])))

# urls_img = list()

# for id in stuff['id']:
#     urls_img.append("/" + str(id) + ".jpg")

# stuff['image_url'] = urls_img
# print(stuff.iloc[0].tolist())
# print(pd.unique(stuff["gender"]))


# Добавление нашей красоты в бд
try:
    # Поключение к нашей TrueStyle бд
    connection = psycopg2.connect(user="truestyleman",
                                  password = "megaProject",
                                  host="localhost",
                                  port="5432",
                                  database="truestyle")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()

    # Чекним инфу о бд
    print("Инфа о сервере PostgreSQL")
    # record = cursor.fetchone()
    # print("Вы подключены к - ", record, "\n")
    fill_version(cursor)
    print("Версии добавлены")
    fill_quote(cursor)
    print("Цитаты загружены")
    fill_gender(cursor)
    print("Гендер загружен")
    fill_stuff(cursor)
    print("Вещи загружены")
    fill_roles(cursor)
    print("Роли загружены")
    fill_articles(cursor)
    print("Статьи загружены")
    fill_style_user(cursor)
    print("Фразы загружены")



except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")