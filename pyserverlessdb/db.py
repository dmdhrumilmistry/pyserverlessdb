from typing import Any


import copy
import datetime
import json
import os


class DB:
    '''
    DB class
    Create a database DB object to store information locally.

    for interactive console use:
        python3 -m pyserverlessdb
    '''
    def __init__(self, file_name:str=os.path.join(os.getcwd(), f'db-{datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S")}'), indent:int=4) -> None:
        '''
        description:
            Creates a pysdb database at specified location.

        parameters:
            file_name (str): location of the db along with its name. default name will be current_location/db-date-time example->/home/user/db_locations/db-date-time.pysdb
            indent (int): json file indentation. default value is 4

        returns: 
            type: None
        '''
        extension = ".pysdb"
        if not file_name.endswith(extension):
            file_name += extension

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
            raise ValueError("table_name should be str.")
        if table_name not in self.__db_data.keys():
            self.__db_data[table_name] = list()
            return True
        return False



    def delete_table(self, table_name:str) -> bool:
        '''
        description:
            deletes table from the db

        parameters:
            table_name (str): name of the table

        returns:
            bool: returns True if operation is successful, else False

        Exception:
            ValueError: if table_name is not a str
        '''
        if type(table_name) != str:
            raise ValueError("table_name should be str.")
        if table_name in self.__db_data.keys():
            del self.__db_data[table_name]
            return True
        
        return False


    def get_table_names(self) -> list:
        '''
        description:
            get table names in a db as a list.

        parameters:
            None
        
        returns:
            list: table names
        '''
        return list(self.__db_data.keys())
    

    def add_in_table(self, table_name:str, obj:Any) -> bool:
        '''
        description:
            add object to the table of table_name
        
        parameters: 
            table_name (str): name of the table
            obj (Any): object to be inserted in the table
        
        returns:
            bool: True if object is inserted successfully, 
                  False if table not found or data already exists.
        '''
        try:
            if type(obj) is dict:
                data = obj
            else:
                data = obj.__dict__
            if data not in self.__db_data[table_name]:
                self.__db_data[table_name].append(data)
                return True
            return False
        except KeyError:
            return False


    def update_in_table(self, table_name:str, index:int, obj:Any) -> bool:
        '''
        description:
            update value of a table entry using index. 

        parameters:
            table_name (str): name of the table
        
        returns:
            bool: True if operation was successful.
                  False if table name if not found in db, or Index is invalid.
        '''
        try:
            # extract data from obj
            if type(obj) is dict:
                data = obj
            else:
                data = obj.__dict__

            # assign data to db table index
            if table_name in self.get_table_names():
                self.__db_data[table_name][index] = data
                return True
            return False

        except IndexError:
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
            dumps data into the file. DB file are updated while dumping data.

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

        
    def get_db_copy(self) -> dict:
        '''
        description:
            returns a deep copy of the current db.

        parameters:
            None

        returns:
            dict: copy of db
        '''
        return copy.deepcopy(self.__db_data)
