from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.author import Author
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

@app.route('/addbook/<int:num>', methods= ['POST', 'GET'])
def add_new(num):
    data ={
        'Author_id': num,
        'book_id': request.form['book_id']
    }
    Book.add_favorite(data)
    return redirect(f'/profile/{num}')

@app.route('/bookpage/<int:num>')
def book_page(num):
    data = {'id': num}
    x = Book.get_specific(data)
    y = Author.get_by_id(data)
    z = Author.unfavorited_authors(data)
    return render_template('bookprofile.html', the_book = x, faves = y, un_faves = z, book = num )

@app.route('/addfbook/<int:num>', methods = ['POST'])
def added(num):
    data ={
        'Author_id': request.form['author_id'],
        'book_id': num
    }
    x = Book.add_favorite(data)
    return redirect(f'/bookpage/{num}')