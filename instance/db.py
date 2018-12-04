import os
import psycopg2
from flask import current_app


class Model:
    def __init__(self):
        """
        use our connection values to establish a connection
        create a psycopg2 cursor that can execute queries
        """
        self.db_host = current_app.config['DB_HOST']
        self.db_username = current_app.config['DB_USERNAME']
        self.db_password = current_app.config['DB_PASSWORD']
        self.db_name = current_app.config['DB_NAME']

        self.connect = psycopg2.connect(
            host=self.db_host,
            user=self.db_username,
            password=self.db_password,
            database=self.db_name,
        )
        self.cursor = self.connect.cursor()

    def create_table_user(self):
        """
        Create a users table
        :return:
        """
        create_user_query = """CREATE TABLE IF NOT EXISTS "users"(
                                id serial not null primary key,
                                username  varchar not null,
                                password  varchar not null,
                                firstname varchar not null,
                                lastname varchar not null,
                                othernames varchar,
                                email varchar not null,
                                phonenumber numeric
                                )"""

        self.query(create_user_query)
        self.save()

    def create_table_incident(self):
        """
        Create a incident table
        :return:
        """
        create_incident_query = """CREATE TABLE IF NOT EXISTS "incident"(
                                      id serial not null primary key,
                                      user_id  integer not null references "users",
                                      recordtype varchar not null,
                                      location varchar,
                                      status varchar not null,
                                      comment varchar not null
                                    )"""

        self.query(create_incident_query)
        self.save()

    def drop_tables(self):
        """
        Drop created tables
        :return: True
        """
        self.drop("incident")
        self.drop("users")
        self.close_session()

    def query(self, query):
        """
        Execute query.
        :param query:
        :return: True
        """
        self.cursor.execute(query)

    def save(self):
        """
        Make the changes to the database persistent
        :return: Success
        """
        self.connect.commit()

    def fetch_all(self):
        """
        Query the db and Fetch all rows in a table

        :return: rows
        """
        return self.cursor.fetchall()

    def fetch_one(self):
        """
        Query the db and Fetch First row in the table

        :return: row
        """
        return self.cursor.fetchone()

    def drop(self, name):
        """
        Drop table by name

        :param name: table_name
        :return:
        """
        self.query("DROP TABLE IF EXISTS " + name)
        self.save()

    def close_session(self):
        """
        Close database connection
        :return: true
        """
        self.cursor.close()
        self.connect.close()


