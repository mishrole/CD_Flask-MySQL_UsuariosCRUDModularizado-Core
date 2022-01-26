from users_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_cr').query_db(query)
        users = []

        if results:
            for user in results:
                users.append(cls(user))
        
        return users
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(firstname)s, %(lastname)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('users_cr').query_db(query, data)
    
    @classmethod
    def findById(cls, data):
        query = "SELECT * FROM users WHERE id like %(userId)s limit 1"
        results = connectToMySQL('users_cr').query_db(query, data)
        user = {}

        for user in results:
            user = cls(user)

        return user
    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(firstname)s, last_name = %(lastname)s, email = %(email)s, updated_at = NOW() WHERE id like %(userId)s;"
        return connectToMySQL('users_cr').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id like %(userId)s"
        return connectToMySQL('users_cr').query_db(query, data)