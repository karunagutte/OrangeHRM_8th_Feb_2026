import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod  #no need to create object
    def get_username():
        return config.get("Login","username")

    @staticmethod
    def get_password():
        return config.get("Login","password")

    @staticmethod
    def get_login_url():
        return config.get("urls","login_url")