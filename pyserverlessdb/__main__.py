from pyserverlessdb.db import DB


import json
import textwrap


BANNER = textwrap.dedent('''
+==============================================+
| ╔═╗┬ ┬╔═╗┌─┐┬─┐┬  ┬┌─┐┬─┐┬  ┌─┐┌─┐┌─┐╔╦╗╔╗   |
| ╠═╝└┬┘╚═╗├┤ ├┬┘└┐┌┘├┤ ├┬┘│  ├┤ └─┐└─┐ ║║╠╩╗  |
| ╩   ┴ ╚═╝└─┘┴└─ └┘ └─┘┴└─┴─┘└─┘└─┘└─┘═╩╝╚═╝  |
+----------------------------------------------+
| A Serverless DB for hobby python projects    |
+----------------------------------------------+
~  v0.0.1Beta          Author: Dhrumil Mistry  ~
+==============================================+
''')

HELP = textwrap.dedent('''
- Commands:
help\t\tprints help menu
exit\t\tclose interpreter
dbs\t\tprint all the created/connected dbs
createdb\tcreates/connects with the db
seldb\t\tselects a db
showdb\t\tshow selected db
printdb\t\tprints db content
tbls\t\tshow tables in selected db
createtbl\tcreate a table in selected db
deltbl\t\tdelete a table from selected db
seltbl\t\tselect a table from selected db
showtbl\t\tprint selected table name from selected db
printtbl\tprint selected table data from selected db
addobj\t\tadd object to selected table in selected db

- Short forms:
DB\t\tDatabase
tbl\t\tTable
sel\t\tSelect
del\t\tDelete
''')


dbs = []
selected_db:DB = None
selected_table_name:str = None

def dict_to_jsonstr(dictionary:dict) -> dict:
    '''
    description:
        takes dictionary as parameter and returns it as a json string.

    parameters:
        dictionary (dict):

    returns:
        str : dictionary as json string
        bool: False if dictionary is invalid 
    '''
    try:
        return json.dumps(dictionary, indent=4, sort_keys=True)
    except json.JSONDecodeError:
        return False


def jsonstr_to_dict() -> dict:
    '''
    description:
        takes json object as user input and returns it as a dictionary.

    parameters:
        None

    returns:
        dict: user input to dict
        bool: False if json object is invalid 
    '''
    try:
        user_input = input("[+] Enter Json Object : \n").strip()
        json_obj:dict = json.loads(user_input)
        return json_obj
    except json.JSONDecodeError:
        return False


def select_db(db_name:str) -> bool:
    '''
    description:
        selects a db from the dbs list using passed db_name.

    parameters:
        db_name (str): name of the db to be selected

    returns:
        type (bool): returns True if db is selected, else False
    '''
    global selected_db, dbs
    for db in dbs:
        if str(db) == db_name:
            selected_db = db
            return True
    return False


def handle_and_execute(command:str):
    '''
    description:
        handles commands and executes if valid.
        
        commands:
            createdb: creates db

    parameters:
        command (str): command to be executed.

    returns:
        result (bool): result after command execution. True if operation is successful else False.
    '''
    global HELP, dbs, selected_db, selected_table_name
    command = command.split(' ')
    words = len(command)

    if command[0] == "help":
        print(HELP)
    
    elif command[0] == "createdb":
        if words <= 1:
            print("[X] Database name missing. usage: createdb [db_name]")
            return False
        file_path = command[1]
        new_db = DB(file_path)
        dbs.append(new_db)
        print(f"[*] {file_path} DB has been created.")
    
    elif command[0] == "dbs":
        if len(dbs) == 0:
            print("[!] No database created/connected.")
            return False

        print("[*] Databases :")
        for db in dbs:
            print(db)

    elif command[0] == "seldb":
        if words <= 1:
            print("[X] Database name missing. usage: seldb [db_name]")
            return False

        if not command[1].endswith('.pysdb'):
            command[1] += '.pysdb'

        if select_db(command[1]):
            print(f"[*] {selected_db} DB selected.")
        else:
            print("[X] Invalid DB name. use dbs to view valid db list.")

    elif command[0] == "showdb":
        if selected_db is not None:
            print(selected_db)
        else:
            print("[!] Select a database before accessing.")
            return False

    elif command[0] == "printdb":
        if selected_db:
            print(dict_to_jsonstr(selected_db.get_db_copy()))
        else:
            print("[!] Select a database before accessing.")
            return False

    elif command[0] == "createtbl":
        if words <= 1:
            print("[X] table name missing. usage: createtbl [table_name]")
            return False
        if selected_db is None:
            print("[X] Select DB before creating a table. use createdb command to create db.")
            return False
        if selected_db.create_table(command[1]):
            print(f"[*] {command[1]} table created in {selected_db}.")
        else:
            print(f"[!] {command[1]} table was not created. Table might already exist.")            

    elif command[0] == "tbls":
        if selected_db is None:
            print("[X] Select DB before viewing tables. use createdb command to create db.")
            return False
        table_names = selected_db.get_table_names()
        if len(table_names) != 0:
            print("[*] Tables :")
            for tbl in table_names:
                print(tbl)

    elif command[0] == "deltbl":
        if words <= 1:
            print("[X] table name missing. usage: deletetbl [table_name]")
            return False
        if selected_db is None:
            print("[X] Select DB before deleting a table. use createdb command to create db.")
            return False
        if selected_db.delete_table(command[1]):
            print(f"[*] {command[1]} was deleted successfully from {selected_db} db.")
            return True
        else:
            print(f"[*] {command[1]} wasn't deleted. {command[1]} might be absent in {selected_db} db.")
            return False
        
    elif command[0] == "seltbl":
        if words <= 1:
            print("[X] table name missing. usage: seltbl [table_name]")
            return False
        if command[1] in selected_db.get_table_names():
            selected_table_name = command[1]
            print (f"[*] {selected_table_name} table selected from {selected_db} db.")
            return True

    elif command[0] == "showtbl":
        if selected_db is None:
            print("[X] Select DB before selecting tables. use createdb command to create db.")
            return False
        
        if selected_table_name is None:
            print("[!] No table selected. select a table using seltbl [table_name].")
            return False
        else:
            print(selected_table_name)
            return True

    elif command[0] == "printtbl":
        if selected_db is None:
            print("[X] Select DB before using printtbl. use createdb command to create db.")
            return False
        
        if selected_table_name is None:
            print("[!] No table selected. select a table using seltbl [table_name].")
            return False
        else:
            table_enteries = selected_db.get_table(selected_table_name)
            for index in range(len(table_enteries)):
                print(f"{index} : {dict_to_jsonstr(table_enteries[index])}")
            return True

    elif command[0] == "addobj":
        if words <= 1:
            print("[X] table name missing. usage: addobj [table_name]. Using selected table.")
            command.append(selected_table_name)

        if selected_db is None:
            print("[X] Select DB before adding object to the table. use createdb command to create db.")
            return False

        json_data = jsonstr_to_dict()
        if json_data:
            if selected_db.add_in_table(selected_table_name ,json_data):
                print(f"[*] json object added to {command[1]}")
                return True
            else:
                print(f"[X] Operation was unsuccessful. Table might not exist or data is already present.")
        else:
            print("[X] invalid json object.")
        

    elif command[0] == "dump":
        if selected_db.dump_data():
            print("[*] Data saved successfully.")
            return True
        else:
            print('[X] Error while Dumping data.')
            return False
    else:
        print("[X] Invalid Command. use help to view commands list.")
        return False

    return True


if __name__ == "__main__":
    print(BANNER)
    
    is_running = True
    while is_running:
        command = input('> ').lower().strip()
        if command == "exit":
            is_running = False
        else:
            handle_and_execute(command)

    print("see you later!!")