# PyServerlessDB
```
+==============================================+
| ╔═╗┬ ┬╔═╗┌─┐┬─┐┬  ┬┌─┐┬─┐┬  ┌─┐┌─┐┌─┐╔╦╗╔╗   |
| ╠═╝└┬┘╚═╗├┤ ├┬┘└┐┌┘├┤ ├┬┘│  ├┤ └─┐└─┐ ║║╠╩╗  |
| ╩   ┴ ╚═╝└─┘┴└─ └┘ └─┘┴└─┴─┘└─┘└─┘└─┘═╩╝╚═╝  |
+----------------------------------------------+
| A Serverless DB for hobby python projects    |
+----------------------------------------------+
~  v0.0.1Beta          Author: Dhrumil Mistry  ~
+==============================================+
```
A Serverless DB for hobby python projects

# Installation

## Using pip+git (Faster)
- Install using
    ```bash
    pip3 install git+https://github.com/dmdhrumilmistry/pyserverlessdb.git
    ```

## Using clone+pip (Safer)
- clone/download repo
    ```bash
    git clone https://github.com/dmdhrumilmistry/pyserverlessdb.git
    ```
- change directory
    ```bash
    cd pyserverlessdb
    ```
- run tests
    ```bash
    python3 setup.py test
    ```
- if test is ok, then install
    ```bash
    pip3 install -e .
    ```

# Usage

## Using interpreter/console
- Start console using
    ```
    python3 -m pyserverlessdb
    ```
- Use `help` command for instructions
    ```
    > help
    ```
    
    
    | Command | description |
    |:-------:|:------------|
    |help|prints help menu|
    |exit|close interpreter
    |dbs|print all the created/connected dbs|
    |createdb|creates/connects with the db|
    |seldb|selects a db|
    |showdb|show selected db|
    |printdb|prints db content|
    |tbls|show tables in selected db|
    |createtbl|create a table in selected db|
    |deltbl|delete a table from selected db|
    |seltbl|select a table from selected db|
    |showtbl|print selected table name from selected db|
    |printtbl|print selected table data from selected db|
    |addobj|add object to selected table in selected db|
    |updateobj|update object from selected table in selected db|


    |abbreviation|full form|
    |:----------:|:--------|
    |DB|Database|
    |tbl|Table|
    |sel|Select|
    |del|Delete|


# Important Notes:
- Windows User need to use `pip` instead of `pip3` and `python` or `py` instead of `python3`
- PyServerlessDB is still under development and is currently in Beta version.


# Instructions for Contribution:
- Create a issue with your idea. I will assign it to you.
- Create Fork
- Edit source code & create tests
- make Pull Request
- I everything is fine, then it will be merged to main
