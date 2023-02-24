import configparser
import os
config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + '/configurations/config.ini')


class ReadConfig:

    @staticmethod
    def get_base_url():
        return config.get('commonInfo', 'base_url')

    @staticmethod
    def get_inventory_page_url():
        return config.get('commonInfo', 'inventory_page_url')

    @staticmethod
    def get_standard_user():
        return config.get('commonInfo', 'standard_user')

    @staticmethod
    def get_locked_out_user():
        return config.get('commonInfo', 'locked_out_user')

    @staticmethod
    def get_problem_user():
        return config.get('commonInfo', 'problem_user')

    @staticmethod
    def performance_glitch_user():
        return config.get('commonInfo', 'performance_glitch_user')

    @staticmethod
    def invalid_user():
        return config.get('commonInfo', 'invalid_user')

    @staticmethod
    def get_valid_password():
        return config.get('commonInfo', 'valid_password')

    @staticmethod
    def get_invalid_password():
        return config.get('commonInfo', 'invalid_password')
