# Record array
records_table = []


class Incident:
    id = 1

    def __init__(self, record_type=None, comment=None, location=None,
                 status=None, images=None, videos=None):
        self.id = Incident.id
        self.record_type = record_type  # [red-flag, intervention]
        self.location = location  # Lat Long coordinates
        # [draft, under investigation, resolved, rejected]
        self.status = status
        self.images = images
        self.videos = videos
        self.comment = comment

        Incident.id += 1

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

    @staticmethod
    def find_by_id(record_id):
        """
        Find a record by their id

        :param record_id: record_id
        :type record_id: int
        :return: record item
        """
        for record in records_table:
            if record.id == record_id:
                return record
        return None

    def save_to_db(self):
        records_table.append(self)

    @staticmethod
    def get_all():
        return records_table

    def delete_from_db(self):
        """
        Find record and delete it.

        :return: None
        """
        records_table.remove(self.find_by_id(self.id))


