import logging


class log_generator_class:
    @staticmethod
    def log_gen_method():
        log_file=logging.FileHandler(".\\Logs\\OrangeHRM.log")
        log_format=logging.Formatter('%(asctime)s - %(name)s -%(funcName)s- %(lineno)d - %(levelname)s - %(message)s')
        log_file.setFormatter(log_format)
        logger=logging.getLogger()
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger
