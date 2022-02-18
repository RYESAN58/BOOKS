from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def index():
    x = Author.get_all()
    return render_template('index.html', all_authors = x)


@app.route('/add', methods=['POST', 'GET'])
def add():
    data = {'name': request.form['author_name']}
    Author.add_author(data)
    return redirect('/')


@app.route('/profile/<int:num>')
def profile_page(num):
    x = Author.get_specific(num)
    y = Book.get_books()
    print(x)
    return render_template('profile.html', user = x, all_books = y)
