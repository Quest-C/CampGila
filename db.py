import sqlite3
from sql import CREATE_LOGIN_TABLE_SQL, CREATE_CAMPERS_TABLE_SQL, CREATE_PAYMENTS_TABLE_SQL

class Database:
    def __init__(self, db_name = "camperdb.db"):
        self.db = db_name
        self._create_table(CREATE_PAYMENTS_TABLE_SQL)
        self._create_table(CREATE_CAMPERS_TABLE_SQL)
        self._create_table(CREATE_LOGIN_TABLE_SQL)

    def create_connection(self):
        """
        create a database connection to the sqlit database
        """
        conn = None
        try:
            conn = sqlite3.connect(self.db)
            conn.execute("PRAGMA foreign_keys = ON")
            return conn
        except Exception as e:
            print(e)

    def _create_table(self, create_table_sql):
        """
        Creat table from the create_table_sql statement
        :return:
        """
        conn = self.create_connection()
        c = conn.cursor()
        try:
            c.execute(create_table_sql)
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)


    def insert_one_record(self, table_name, values):
        conn = self.create_connection()
        c = conn.cursor()
        try:
            c.execute("""INSERT INTO %s VALUES %s""" % (table_name, values))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False

    def delete_one_record(self, table_name, field_name, field_value):
        conn = self.create_connection()
        c = conn.cursor()
        try:
            c.execute(f"DELETE FROM {table_name} WHERE {field_name}=?", (field_value,))
            if c.rowcount == 0:
                conn.close()
                return False
            else:
                conn.commit()
                conn.close()
                return True
        except Exception as e:
            print(e)
            return False

    def query_table(self, table_name, field_name):
        conn = self.create_connection()
        c = conn.cursor()
        try:
                c.execute(f"SELECT {field_name} FROM {table_name}")
                result = c.fetchall()
                conn.close()
                return result
        except Execption as e:
            print(e)
            return False

    def query_table_with_condition(self, table_name, field_name, conditions):
        conn = self.create_connection()
        c = conn.cursor()
        try:
                c.execute(f"""SELECT {field_name} FROM {table_name} WHERE {conditions}""")
                result = c.fetchall()
                conn.close()
                return result
        except Execption as e:
            print(e)
            return False

    def get_last_payment(self):
        conn = self.create_connection()
        c = conn.cursor()
        c.execute('SELECT MAX(transaction_id) FROM payments')
        result = c.fetchone()[0]
        conn.close()
        return result

    def update_camper_data(self, f_name, l_name, gender, dob, mobile, address, city, state, zipcode, email):
        conn = self.create_connection()
        c = conn.cursor()
        try:
            c.execute(f"""UPDATE campers SET
                            first_name = '{f_name}',
                            last_name = '{l_name}',
                            gender = '{gender}',
                            date_of_birth = '{dob}',
                            mobile = '{mobile}',
                            address = '{address}',
                            city = '{city}',
                            state = '{state}',
                            zipcode = '{zipcode}'
                            WHERE email = '{email}'""")
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False

#db = Database()
#db.insert_one_record("logins", ("admin", "1234"))