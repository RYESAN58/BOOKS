from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__(self, data):
        self.id =data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []


    @classmethod
    def add_author(cls, data):
        query = 'INSERT INTO `booksauthors`.`authors` (`name`) VALUES (%(name)s);'
        print(query)
        return connectToMySQL('booksauthors').query_db( query, data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors"
        which = connectToMySQL('booksauthors').query_db(query)
        writers = []

        for i in which:
            writers.append(cls(i))
        return writers


    @classmethod
    def get_specific(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s"
        return connectToMySQL('booksauthors').query_db(query, data)


    @classmethod
    def unfavorited_authors(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        authors = []
        results = connectToMySQL('booksauthors').query_db(query,data)
        for row in results:
            authors.append(cls(row))
        return authors


    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        print(query)
        results = connectToMySQL('booksauthors').query_db(query,data)

        # Creates instance of author object from row one
        author = cls(results[0])
        # append all book objects to the instances favorites list.
        for row in results:
            # if there are no favorites
            if row['books.id'] == None:
                break
            # common column names come back with specific tables attached
            data = {
                "id": row['books.id'],
                "tittle": row['tittle'],
                "num_of_pages": row['num_of_pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            print(data)
            author.favorite_books.append(book.Book(data))
        return author