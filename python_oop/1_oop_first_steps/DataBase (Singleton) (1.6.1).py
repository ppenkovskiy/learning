class DataBase:
    # Singleton - you can create only one instance of this class.
    # __instance - link to the instance of the class
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        return f"Connecting to DB: {self.user}, {self.psw}, {self.port}."

    def close(self):
        print('Closing connection to DB.')

    def read(self):
        return 'Data from DB.'

    def write(self):
        print(f'Writing to DB {data}.')

db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '12345', 81)  # new data will be overwritten to the same object.
print(id(db)==id(db2))
print(db.connect())
print(db2.connect())