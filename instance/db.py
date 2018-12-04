import os
import psycopg2

db_url = os.getenv("DATABASE_URL")


class Model:
    def __init__(self):
        """
        use our connection values to establish a connection
        create a psycopg2 cursor that can execute queries
        """
        self.connect = psycopg2.connect(db_url)
        self.cursor = self.connect.cursor()

    def init_app(self, app):
        self.connect = psycopg2.connect(app.config.get('DATABASE_URL'))

    def create_table_user(self):
        """
        Create a users table
        :return:
        """
        create_user_query = """CREATE TABLE IF NOT EXISTS "Users"(
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
        create_incident_query = """CREATE TABLE IF NOT EXISTS "Incident"(
                                      id serial not null primary key,
                                      user_id  integer not null references "Users",
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
        self.drop("Users")
        self.drop("Incident")
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
        self.query(f"DROP TABLE IF EXISTS {name} CASCADE")

    def close_session(self):
        """
        Close database connection
        :return: true
        """
        self.cursor.close()
        self.connect.close()


