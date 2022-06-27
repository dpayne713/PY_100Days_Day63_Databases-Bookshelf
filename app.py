from flask import Flask, render_template, request, redirect
from database import Database, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///book-database.db"
db.init_app(app)
database = Database()

@app.route('/')
def home():
    all_books = database.get_all_books()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method =="GET":
        return render_template('add.html')

    if request.method == "POST":
        book_data = request.form.to_dict()
        database.add_new_book(book_data)
        return redirect('/')

@app.route('/update/<id>', methods=["GET", "POST"])
def update(id):
    if request.method == "GET":
        book_data = database.get_single_book_by_id(id)
        return render_template('modal.html', book_data=book_data)
    if request.method == "POST":
        form_data = request.form.to_dict()
        form_data['id'] = id
        database.modify_book(form_data)
        return redirect('/')


@app.route("/delete/<id>")
def delete(id):
    database.delete_book(id)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)




















# STRAIGHT SQLITE COMMANDS #
# db=sqlite3.connect("dp-books-database.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating INTEGER NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1,'Harry Potter', 'J.K.Rowling', 5)")
# db.commit()