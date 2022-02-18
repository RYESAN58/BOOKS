from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self, data):
        self.id =data['id']
        self.tittle = data['tittle']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_books(cls):
        query = "SELECT * FROM books"
        which = connectToMySQL('booksauthors').query_db(query)
        novels = []

        for i in which:
            novels.append(cls(i))
        return novels