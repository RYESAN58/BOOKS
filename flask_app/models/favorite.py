from flask_app.config.mysqlconnection import connectToMySQL
class Favorite:
    def __init__(self, data):
        self.Author_id =data['Author_id']
        self.book_id = data['book_id']
        self.favorites = []