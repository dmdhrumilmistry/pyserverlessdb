from pyserverlessdb.db import DB

import datetime
import os
import tempfile
import tracemalloc
import unittest


class DBTests(unittest.TestCase):
    def test_db_creation(self):
        file_name = os.path.join(tempfile.gettempdir(), f'testdb-{datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S")}.pysdb')
        db_conn = DB(file_name)
        self.assertEqual(str(db_conn), f"DB object : {file_name}", "Should return DB object")
        os.remove(file_name)


if __name__ == "__main__":
    tracemalloc.start()
    unittest.main()
    tracemalloc.stop()
