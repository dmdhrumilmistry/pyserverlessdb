from pyserverlessdb.__main__ import select_db
from pyserverlessdb.db import DB

import copy
import datetime
import os
import shutil
import tempfile
import tracemalloc
import unittest


class TestClass:
    def __init__(self, name:str="TestCase", is_testing:int=True) -> None:  
        self.name = name
        self.is_testing = is_testing


class DBTests(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.temp_dir = os.path.join(tempfile.gettempdir(), 'pyserverlessdb_tests')
        if not os.path.exists(self.temp_dir):
            os.mkdir(self.temp_dir)
        self.file_name = os.path.join(self.temp_dir, f'testdb-{datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S")}.pysdb')
        self.table_name = "TestTable"
        self.db = DB(self.file_name)


    def test_creation(self):
        self.assertEqual(str(self.db), self.file_name, "Should return file_name as str")


    def test_table_creation(self):
        self.assertEqual(self.db.create_table(self.table_name), True, "Received unexpected value while creating table")
        with self.assertRaises(ValueError, msg="Did not received Value Error while creating table with invalid argument type"):
            self.db.create_table(self.table_name.encode())

    
    def test_add_in_table(self):
        self.assertEqual(self.db.add_in_table(self.table_name, TestClass()), False, "Expected return value to be False durin adding obj to table when table is not present")
        self.db.create_table(self.table_name)
        self.assertEqual(self.db.add_in_table(self.table_name, TestClass()), True, "Expected return value to be True after adding obj in table")
    

    def test_get_table(self):
        self.db.create_table(self.table_name)
        self.assertEqual(type(self.db.get_table(self.table_name)), list, "Expected Type list while retrieving table")


    def test_get_table_names(self):
        self.db.create_table(self.table_name)
        self.assertEqual(type(self.db.get_table_names()), list, "Expected Type list while retrieving table names")
        
    
    def test_delete_table(self):
        self.db.create_table(self.table_name)
        self.assertEqual(self.db.delete_table(self.table_name), True, "Expected True after deleting table")
        self.assertEqual(self.db.delete_table(self.table_name), False, "Expected False while deleting a deleted table")
        with self.assertRaises(ValueError, msg="Did not received Value Error while deleting a table with invalid argument type"):
            self.db.create_table(self.table_name.encode())


    def test_get_db_copy(self):
        self.db.create_table(self.table_name)
        self.assertEqual(type(self.db.get_db_copy()), dict, "Expected db as a dictionary")

    def test_update_in_table(self):
        obj = TestClass()
        new_obj = TestClass("NewObj")
        self.db.create_table(self.table_name)
        self.db.add_in_table(self.table_name, obj)
        table = copy.deepcopy(self.db.get_table(self.table_name))
        self.assertEqual(self.db.update_in_table(self.table_name, 0, new_obj), True, "Table cannot be updated with new obj")
        new_table = self.db.get_table(self.table_name)
        self.assertNotEqual(table, new_table, "Table entry is not being updated")




    def test_dump_data(self):
        self.assertEqual(self.db.dump_data(), True)

    
    def test_remove_tested_files(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)



if __name__ == "__main__":
    tracemalloc.start()
    unittest.main()
    tracemalloc.stop()
