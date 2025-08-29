# equipemnts: machines, devices, topics,
# mandatory columns of an equipment table: id, name, creation_date, created_by, updation_date, updated_by
# mandatory columns of a computation table: id,logic mapping with equipment ids to have relation,creation_date
# crud:
# database, schema, tables,views,indexes, constraints, functions, procedures,triggers, rules,extensions, roles,permissions.
# learn other tools and components to integrate in the application as storage for the user cases and storage.
# after completion create deep report of usercases
# unit testing, integrity, user testing compulasy
# unit: for technical 
# integrity: all components are aligned to constraints of db constraints
# user testing: all end-end testing are aligned with use case pipelines
# security test: exposing to external to serve-client
# Use SQLAlchemy ORM to manage PostgreSQL tables (sensors, devices, logs, users).
# Use GraphQL to expose those ORM models safely to dashboards, mobile apps, or reports.
# use Appoloql at frontend on the same
# first do scratch and test and turn to ORM for sqlalchermy and graphql for exposure of models
# fully test for machine services with frontend after authentication and authorization services by backtracking
import configparser 
from datetime import datetime as dt 
import psycopg2,os
from psycopg2 import pool, OperationalError
import pandas as pd
import traceback
import logging
class Energy:
    def __init__(self):
        # Create a logger specific to this instance
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
        log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),  "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_filename = f"energy_manager_{dt.now().strftime('%Y-%m-%d')}.log"
        log_path = os.path.join(log_dir, log_filename)
        handler = logging.FileHandler(log_path)
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        if not self.logger.handlers:
            self.logger.addHandler(handler)
        print('logger initiated sucessfully.',self.logger)

        # env setup
        self.configparser = configparser.ConfigParser()       
        file_path = os.path.join(os.path.dirname(__file__), "properties.ini")
        self.configparser.read(file_path)
        print('parser initiated sucessfully.',self.configparser)

        # postgresql db configuration
        self.postgres_credentials = {
            'user': self.configparser.get('postgresql','user'),
            'password' : self.configparser.get('postgresql','password'),
             'dbname':self.configparser.get('postgresql','dbname'),
             'host': self.configparser.get('postgresql','host'),
            'port': self.configparser.get('postgresql','port'),

        }
        
        # normal db connecting and testing 
        self.db = self.postgresql_db_connection()
        self.testing_postgres_db = self.postgresql_db_activity()

        # pool db connection and testing 
        self.pool_db_connection = self.db_pool_postgresql__connection()
        self.testing_postgres_pool_db = self.postgresql_pool_db_activity()

        # checking all the above instances got initialized
        print('checking logger',self.logger,self.db,self.pool_db_connection,self.configparser)
    
    # connecting to db with normal connection
    def postgresql_db_connection(self):
        try:
            print('i am inside db connection')
            print('checking credentials before adding',self.postgres_credentials)
            connection = psycopg2.connect(
                user=self.postgres_credentials['user'],
                password = self.postgres_credentials['password'],
                host = self.postgres_credentials['host'],
                port = self.postgres_credentials['port'],
                dbname = self.postgres_credentials['dbname']
            )
            print('postgresql db connection created successfully',connection)
            return connection
        except Exception as e:
            error_trace = traceback.format_exc()
            self.logger.info(f'handling postgresql connection error {error_trace}')
    # connecting to db with pool connection
    def db_pool_postgresql__connection(self):
        try:

            db_pool = pool.ThreadedConnectionPool(
                1,              # min connections
                10,             # max connections
                user=self.postgres_credentials['user'],
                password = self.postgres_credentials['password'],
                host = self.postgres_credentials['host'],
                port = self.postgres_credentials['port'],
                dbname = self.postgres_credentials['dbname']
            )
            if db_pool:
                self.logger.info(" Connection pool created successfully")
            return db_pool
        except Exception as e:
            error_trace = traceback.format_exc()
            
            self.logger.info(f'handling pool postgresql connection error {error_trace}')

    # 2️⃣ Get a connection from the pool
    def get_connection(self):
        return self.pool_db_connection.getconn()

    # 3️⃣ Release connection back to pool
    def release_connection(self,conn):
        self.pool_db_connection.putconn(conn)

    # testing normal connection
    def postgresql_db_activity(self):

        try:
            cursor = self.db.cursor()
            # 1️⃣ Fetch data from source table
            cursor.execute("SELECT id, name FROM iiot_project.test_table;")
            rows = cursor.fetchall()
            print('rows with normal connection',rows)
        
        except Exception as e:
            print(traceback.format_exc())
    # testing the pool connection
    def postgresql_pool_db_activity(self):

        try:

            connect = self.pool_db_connection.getconn()
            cursor = connect.cursor()
            # 1️⃣ Fetch data from source table
            cursor.execute("SELECT id, name FROM iiot_project.test_table;")
            rows = cursor.fetchall()
            print('rows with pool connection',rows)
        
        except Exception as e:
            print(traceback.format_exc())
        finally:
            if cursor: cursor.close()
            if connect: self.release_connection(connect)
        
    # machines apis
    def insert_machines(self):
        try:
            connect = self.pool_db_connection.getconn()
            cursor = connect.cursor()
            # single
            sql_query = 
            # multiple
            sql_query=
        except Exception as e:
            print(traceback.format_exc())
        

    def extract_machine(self):
        # extract single or multi machines
        pass
    def update_machines(self):
        # update single or multi machines
        pass

    # devices api
    def insert_devices(self):
        # insert single or multi machines
        pass

    def extract_devices(self):
        # extract single or multi machines
        pass
    def update_devices(self):
        # update single or multi machines
        pass

    # parameters apis
    def insert_parameters(self):
        # insert single or multi machines
        pass

    def extract_parameters(self):
        # extract single or multi machines
        pass
    def update_parameters(self):
        # update single or multi machines
        pass

if __name__ == '__main__':
    energy = Energy()

