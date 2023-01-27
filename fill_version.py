import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import pandas as pd



def create_version_table(cursor):
    versions = {"zero":("0.0.0", "0.0.0"), "alpha_test":("0.0.1", "0.0.1")}

    query_create = """CREATE SEQUENCE IF NOT EXISTS public.app_versions_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1
    OWNED BY article.id_article;

ALTER SEQUENCE public.app_versions_id_seq
    OWNER TO truestyleman;

    CREATE TABLE IF NOT EXISTS public.app_versions
(
    id bigint NOT NULL DEFAULT nextval('app_versions_id_seq'::regclass),
    actual_version_number character varying(255) COLLATE pg_catalog."default",
    min_actual_version_number character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT app_versions_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.app_versions
    OWNER to truestyleman;"""

    cursor.execute(query_create)
    query_insert = """INSERT INTO app_versions (ACTUAL_VERSION_NUMBER, MIN_ACTUAL_VERSION_NUMBER) VALUES (%s, %s)"""
    for v in versions.values():
        cursor.execute(query_insert, v)


def main():

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

        create_version_table(cursor)
        connection.commit()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

if __name__ == "__main__":
    main()