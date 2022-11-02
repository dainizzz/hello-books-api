from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    @classmethod
    def from_dict(cls, book_data):
        return Book(title=book_data["title"],
                    description=book_data["description"])

    def to_dict(self):
        book_as_dict = {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }
        return book_as_dict