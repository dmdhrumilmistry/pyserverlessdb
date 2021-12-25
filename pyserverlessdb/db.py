from typing import Any


import datetime
import json
import os


class DB:
    '''
    DB class
    Create a database DB object to store information locally.
    '''
    def __init__(self, file_name:str=os.path.join(os.getcwd(), f'db-{datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S")}'), indent:int=4) -> None:
        '''
        description:
            Creates a pysdb database at specified location.

        parameters:
            file_name (str): location of the db along with its name. default name will be current_location/db-date-time example->/home/user/db_locations/mydb.pysdb
            indent (int): json file indentation. default value is 4

        returns: 
            type: None
        '''
        if not file_name.endswith(".pysdb"):
            file_name += ".pysdb"

        self.__file_name = file_name
        self.__db_data = dict()
        self.__indent = indent

        if os.path.exists(self.__file_name):
            with open(self.__file_name, 'r') as f:
                self.__db_data = json.loads(f.read())
        else:
            with open(self.__file_name, 'a+') as f:
                f.write(json.dumps(dict()))


    def __repr__(self) -> str:
        return str(self.__file_name)


    def create_table(self, table_name:str) -> bool:
        '''
        description:
            creates a empty table inside the database.
            On success returns True.
            raises Value error is table name is not a string.

        parameters:
            table_name (str): name of the table
        
        returns:
            bool: returns True if operation is successful
        
        Exception:
            ValueError: if table_name is not a str
        '''
        if type(table_name) != str:
            raise ValueError("table name should be str.")
        self.__db_data[table_name] = list()
        return True

    
    def add_in_table(self, table_name:str, obj:Any)->bool:
        '''
        description:
            add object to the table of table_name
        
        parameters: 
            table_name (str): name of the table
            obj (Any): object to be inserted in the table
        
        returns:
            bool:   True if object is inserted successfully,
                    False if table not found.
        '''
        try:
            self.__db_data[table_name].append(obj.__dict__)
            return True
        except KeyError:
            return False


    def get_table(self, table_name:str):
        '''
        description:
            Get Table Entries as a list of dictionaries

        parameters:
            table_name (str): name of the table
        
        returns:
            list[dict]: list of table enteries in dictionary format
            or
            None: if table_name is invalid or does not exists
        '''
        table_content = self.__db_data.get(table_name, None)
        if table_name is not None:
            return table_content
        else:
            return None



    def dump_data(self):
        '''
        description:
            dumps data into the file.

        parameters:
            None

        returns:
            bool: True if operation is successful.
        
        Exception:
            Exception: if any occurs
        '''
        try:
            with open(self.__file_name, 'w+') as f:
                f.write(json.dumps(self.__db_data, indent=self.__indent))
            return True
        except Exception as e:
            raise Exception(e)
