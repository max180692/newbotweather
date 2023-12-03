

class RegisterUser:
    
    def __init__(self):
        self.name = None
        self.id = None
        self.city = None

    def set_user_info(self,name,id):
        self.name = name
        self.id = id

    def get_info_user(self):
        return {'name':self.name,'id':self.id,'city':self.city}

    def set_my_city(self,city):
        self.city = city