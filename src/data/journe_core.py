import sqlite3
from common.app_config import *
from src.utils import read_sql_command

"""
this class handles the entire database connections & payload management 
    
"""

class JourneConnection:

    def __init__(self):
        self.conn = JourneConnection.connect_to_journe_core()  # create a new db or connect to an existing one
        self.cursor = self.conn.cursor()

    @staticmethod
    def connect_to_journe_core():
        return sqlite3.connect(DATABASE_PATH)

    # wipes the existing journe core db/starts one from scratch and creates a brand-new schema
    def create_new_journe_core(self):
        # retrieve sql command for core creation
        core_sql = read_sql_command(JOURNE_CORE_CREATE_SQL_PATH)
        # execute
        self.cursor.executescript(core_sql)
        print("Fresh Journe db created")

    """
    sends journe object to the db. 
    """
    def send_payload(self, payload_obj):
        payload_sql = payload_paths[payload_obj.journe_object_type]['SEND']  # getting the sql command path
        sql_command = read_sql_command(payload_sql)  # getting the sql command
        self.cursor.execute(sql_command, payload_obj.to_payload())  # execute
        self.conn.commit()
        print(f"{payload_obj.to_payload()[f'{payload_obj.journe_object_type}_title']} sent to journe core!")

    """
    object_type = string - task, pot, block
    object_id = string - passing object_id to get the object
    object_title = string - passing object_title to get the object
    read_all = bool - reads in entire object type data
    """
    def read_payload(self, object_type, object_id=None, object_title=None, read_all=False):
        # get all data
        if read_all:
            # retrieve sql command for core creation
            sql_command_path = payload_paths[object_type]['READ']['ALL']
            query_dict = {}
        else:
            if object_id:  # if we are using id to read
                sql_command_path = payload_paths[object_type]['READ']['ID']
                query_dict = {'_id': object_id}
            else: # we are using title to read
                sql_command_path = payload_paths[object_type]['READ']['TITLE']
                query_dict = {'_title': object_title}
        print(sql_command_path)
        # execute
        sql = read_sql_command(sql_command_path)
        self.cursor.execute(sql, query_dict)
        return self.cursor.fetchall()

    # def read_pots(self):
    #     # retrieve sql command for core creation
    #     sql = read_sql_command(JOURNE_CORE_READ_POTS)
    #     # execute
    #     self.cursor.execute(sql)
    #     return self.cursor.fetchall()

    # def get_pot_id_from_pot_title(self, query_dict):
    #     # retrieve sql command for core creation
    #     sql = read_sql_command(JOURNE_CORE_GET_POT_ID_FROM_POT_TITLE)
    #     # execute
    #     self.cursor.execute(sql, query_dict)
    #     return self.cursor.fetchall()
    #
    # def get_pot_title_from_pot_id(self, query_dict):
    #     # retrieve sql command for core creation
    #     sql = read_sql_command(JOURNE_CORE_GET_POT_TITLE_FROM_POT_ID)
    #     # execute
    #     self.cursor.execute(sql)
    #     return self.cursor.fetchall()


