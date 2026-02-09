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

    @staticmethod
    def get_firstname():
        return config.get("add_employee","firstname")

    @staticmethod
    def get_middle_name():
        return config.get("add_employee", "middle_name")


    @staticmethod
    def get_lastname():
        return config.get("add_employee", "lastname")

    @staticmethod
    def get_image():
        return config.get("add_employee", "image")

    # @staticmethod
    # def get_new_username():
    #     return config.get("New_User","new_username")
    #
    # @staticmethod
    # def get_new_password():
    #     return config.get("New_User", "new_password")
    #
    # @staticmethod
    # def get_confirm_password():
    #     return config.get("New_User", "confirm_password")
    #
    # @staticmethod
    # def get_employee_name():
    #     return config.get("New_User", "employee_name")
