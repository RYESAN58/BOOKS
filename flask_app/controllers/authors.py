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
    data = {
        'id': num
    }
    x = Author.get_specific(data)
    y = Author.get_by_id(data)
    print('THHIS IS Y ------>', y)
    z = Book.unfavorited_books(data)
    return render_template('profile.html', user = x, all_faves = y, unfaves = z, )
