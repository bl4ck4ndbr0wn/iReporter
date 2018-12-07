from instance.db import Model
import pdb


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

    def serialize(self):
        return dict(id=self.id,
                    user_id=self.user_id,
                    record_type=self.record_type,
                    location=self.location,
                    status=self.status,
                    comment=self.comment
                    )

    def find_all_by_user_id(self, user_id):
        """
        Fetch all incident records by user_id.
        :param user_id:
        :return: Incidents
        """
        query = f"SELECT * FROM incident WHERE user_id={user_id}"
        self.query(query)
        incidents = self.fetch_all()
        self.save()

        if incidents:
            return [self.map_incidents(incident) for incident in incidents]
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
        self.cursor.execute("""
                INSERT INTO incident (user_id, recordtype,location, status, comment) 
                VALUES(%s, %s, %s, %s, %s);""", (self.user_id, self.record_type, self.location, self.status, self.comment))
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
        self.cursor.execute("""
                        UPDATE incident SET location = %s 
                        WHERE id = %s;""",
                            (location, self.id))
        self.save()

    def update_comment(self, comment):
        """
        Update incident comment

        :param comment:
        :return: Incident
        """
        self.cursor.execute("""
                                UPDATE incident SET comment = %s 
                                WHERE id = %s;""",
                            (comment, self.id))
        self.save()

    def update_status(self, status):
        """
        Update incident status

        :param status:
        :return: Incident
        """
        self.cursor.execute("""
                                UPDATE incident SET status = %s 
                                WHERE id = %s;""",
                            (status, self.id))
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
        self.id = data[0]
        self.user_id = data[1],
        self.record_type = data[2],
        self.location = data[3],
        self.status = data[4],
        self.comment = data[5]

        return self
