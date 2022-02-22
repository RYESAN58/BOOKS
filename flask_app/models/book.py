from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    def __init__(self, data):
        self.id =data['id']
        self.tittle = data['tittle']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.best_books = []


    @classmethod
    def get_books(cls):
        query = "SELECT * FROM books"
        which = connectToMySQL('booksauthors').query_db(query)
        novels = []

        for i in which:
            novels.append(cls(i))
        return novels


    @classmethod
    def add_book(cls, data):
        query = 'INSERT INTO `booksauthors`.`books` (`tittle`, `num_of_pages`) VALUES (%(tittle)s, %(num_of_pages)s);'
        print(query)
        return connectToMySQL('booksauthors').query_db( query, data)

    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
        results = connectToMySQL('booksauthors').query_db(query,data)
        books = []
        for row in results:
            books.append(cls(row))
        print(books)
        return books

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL('booksauthors').query_db(query,data)

        book = cls(results[0])

        for row in results:
            if row['authors.id'] == None:
                break
            data = {
                "id": row['authors.id'],
                "name": row['name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            book.best_books.append(author.Author(data))
        return book