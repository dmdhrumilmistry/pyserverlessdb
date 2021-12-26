from pyserverlessdb.db import DB


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

HELP = textwrap.dedent('''commands:
help\t\tprints help menu
exit\t\tclose interpreter
createdb\tcreates/connects with the db
dbs\t\tprint all the created/connected dbs
selectdb\tselects a db
showdb\t\tshow selected db
''')


dbs = []
selected_db = None
selected_table = None


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
    global HELP, dbs, selected_db, selected_table
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
    
    elif command[0] == "dbs":
        if len(dbs) == 0:
            print("[!] No database created/connected.")
            return False

        print("Databases :")
        for db in dbs:
            print(db)

    elif command[0] == "selectdb":
        if words <= 1:
            print("[X] Database name missing. usage: createdb [db_name]")
            return False

        if not command[1].endswith('.pysdb'):
            command[1] += '.pysdb'

        if command[1] in [str(db) for db in dbs]:
            selected_db = command[1]
            print(f"[*] {selected_db} DB selected.")
        else:
            print("[X] Invalid DB name. use dbs to view valid db list.")


    elif command[0] == "showdb":
        if selected_db is not None:
            print(selected_db)
        else:
            print("[!] Select a database before accessing.")
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

    print("see ya! later!!")