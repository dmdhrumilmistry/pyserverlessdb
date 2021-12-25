import os
import json


class DB:
    '''
    DB class
    Create a database DB object to store information locally.
    '''
    def __init__(self, file_name:str, indent:int=4) -> None:
        '''
        Create a db at specified location, if it already exists then load data i
        param: file_name
        param: indent
        returns: None
        '''
        self.file_name = file_name
        self.__db_data = dict()
        self.__indent = indent

        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as f:
                self.__db_data = json.loads(f.read())
        else:
            with open(self.file_name, 'a+') as f:
                f.write(json.dumps(dict()))


    def __repr__(self) -> str:
        return f"DB object : {self.file_name}"


    def create_table(self, table_name:str):
        '''
        creates a empty table inside the database
        '''
        if type(table_name) != str:
            raise ValueError("table name should be str.")
        self.__db_data[table_name] = dict()


    def dump_data(self):
        '''
        dumps data into file
        '''
        try:
            with open(self.file_name, 'w+') as f:
                f.write(json.dumps(self.__db_data, indent=self.__indent))
        except Exception as e:
            raise Exception(e)
