from flask_app.config.mysqlconnection import connectToMySQL


class Author:
    def __init__(self, data):
        self.id =data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


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
    def get_specific(cls, num1):
        query = f"SELECT * FROM authors WHERE id = {num1}"
        return connectToMySQL('booksauthors').query_db(query)