from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Database():
    def __init__(self):
        self.book = self.Book

    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String, unique=True, nullable=False)
        author = db.Column(db.String, unique=False, nullable=False)
        rating = db.Column(db.Float, unique=False, nullable=False)

    def get_all_books(self):
        return db.session.query(self.Book)

    def get_single_book_by_id(self,id):
        return self.Book.query.filter_by(id=id).first()

    def add_new_book(self, book_data):
        new_book = self.book(name=book_data['name'], author=book_data['author'], rating=book_data['rating'])
        db.session.add(new_book)
        db.session.commit()

    def modify_book(self, data):
        book = self.get_single_book_by_id(data["id"])
        book.name = data['name']
        book.author = data['author']
        book.rating = data['rating']
        db.session.commit()

    def delete_book(self, id):
        db.session.delete(self.get_single_book_by_id(id))
        db.session.commit()





