from instance.db import Model


class Incident(Model):

    def __init__(self, title=None, record_type=None, comment=None, user_id=None,
                 location=None, status="draft", images=None, videos=None):
        super().__init__()
        self.id = None
        self.user_id = user_id
        self.title = title
        self.record_type = record_type  # [red-flag, intervention]
        self.location = location  # Lat Long coordinates
        # [draft, under investigation, resolved, rejected]
        self.status = status
        self.images = images
        self.videos = videos
        self.comment = comment

    def __repr__(self):
        return f'{self.comment} incident in incident Model.'

    def serialize(self):
        return {"id": self.id,
                "user_id": self.user_id,
                "record_type": self.record_type,
                "title": self.title,
                "comment": self.comment,
                "location": self.location,
                "status": self.status,
                "image_path": self.images,
                "video_path": self.videos}

    def find_all_by_user_id(self, user_id):
        """
        Fetch all incident records by user_id.
        :param user_id:
        :return: Incidents
        """
        query = f"""SELECT * FROM incident WHERE user_id={user_id}"""
        self.query(query)
        incidents = self.fetch_all()
        self.save()

        if incidents:
            print(incidents)
            return incidents
        return None

    def find_by_id(self, record_id):
        """
        Find a record by their id

        :param record_id: record_id
        :type record_id: int
        :return: record item
        """
        query = f"SELECT * FROM incident WHERE id={record_id}"
        self.query(query)
        incidents = self.fetch_one()
        self.save()

        if incidents:
            return self.map_incidents(incidents)
        return None

    def save_to_db(self):
        self.cursor.execute("""INSERT INTO incident (user_id, title, recordtype,
                                location, status, comment) VALUES(%s, %s, %s,
                                 %s, %s, %s);""", (self.user_id,
                                                   self.title,
                                                   self.record_type,
                                                   self.location,
                                                   self.status,
                                                   self.comment,))
        self.save()
        self.close_session()

    def get_all(self):
        self.query("SELECT * FROM incident")
        incidents = self.fetch_all()
        self.save()

        if incidents:
            return incidents
        return None

    def update_location(self, location):
        """
        Update incident location
        :param location:
        :return: incident
        """
        self.cursor.execute("""UPDATE incident SET location = %s WHERE id = %s;""", (location, self.id,))
        self.save()

    def update_comment(self, comment):
        """
        Update incident comment

        :param comment:
        :return: Incident
        """
        self.cursor.execute("""UPDATE incident SET comment = %s 
                                WHERE id = %s;""",
                            (comment, self.id,))
        self.save()

    def update_status(self, status):
        """
        Update incident status

        :param status:
        :return: Incident
        """
        self.cursor.execute("""UPDATE incident SET status = %s 
                                WHERE id = %s;""",
                            (status, self.id,))
        self.save()

    def delete_from_db(self):
        """
        Find record and delete it.

        :return: None
        """
        self.cursor.execute("""DELETE FROM incident WHERE id = %s;""",
                            (self.id,))
        self.save()

    def map_incidents(self, data):
        """
        Update
        :return:
        """
        print(data)
        self.id = data[0]
        self.user_id = data[1],
        self.title = data[2]
        self.record_type = data[3],
        self.location = data[4],
        self.status = data[5],
        self.comment = data[6]

        return self
