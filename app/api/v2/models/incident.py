from instance.db import Model


class Incident(Model):

    def __init__(self, record_type=None, comment=None, user_id=None,  location=None,
                 status=None, images=None, videos=None):
        super().__init__()
        self.id = None
        self.user_id = user_id
        self.record_type = record_type  # [red-flag, intervention]
        self.location = location  # Lat Long coordinates
        # [draft, under investigation, resolved, rejected]
        self.status = status
        self.images = images
        self.videos = videos
        self.comment = comment

    def __repr__(self):
        return f'{self.comment} incident in incident Model.'

    def json(self):
        return {"id": self.id,
                "record_type": self.record_type,
                "location": self.location,
                "status": self.status,
                "comment": self.comment,
                "images": self.images,
                "videos": self.videos
                }

    def find_by_id(self, record_id):
        """
        Find a record by their id

        :param record_id: record_id
        :type record_id: int
        :return: record item
        """
        query = f"SELECT * FROM incident WHERE id={record_id}"
        self.query(query)
        incident = self.fetch_one()

        if incident:
            return incident
        return None

    def save_to_db(self):
        self.cursor.execute("""
                INSERT INTO incident (user_id, recordtype,location, status, comment) 
                VALUES(%s, %s, %s, %s, %s);""", (self.user_id, self.record_type, self.location, self.status, self.comment))
        self.save()

    @staticmethod
    def get_all():
        pass

    def update_location(self, location):
        """
        Update incident location
        :param location:
        :return: incident
        """
        pass

    def update_comment(self, comment):
        """
        Update incident comment

        :param comment:
        :return: Incident
        """
        pass

    def delete_from_db(self):
        """
        Find record and delete it.

        :return: None
        """
        pass
