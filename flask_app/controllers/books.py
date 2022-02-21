from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.book import Book


@app.route('/books')
def rend_books():
    x = Book.get_books()
    return render_template('books.html', all_books = x)


@app.route('/add_book', methods=['POST'])
def add_book():
    data = {
        'tittle': request.form['book'],
        'num_of_pages': request.form['pages']
    }
    Book.add_book(data)
    return redirect('/books')
