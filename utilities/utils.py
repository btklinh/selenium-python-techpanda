from random import randint

class random_email:
    def __init__(self):
        pass

    def create_random_email(self):
        value = randint(10,999)
        email = "linhbui_" + str(value) + "@gmail.com"
        return email
