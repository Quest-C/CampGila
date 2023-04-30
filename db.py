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

    def verify_login_from_database(self, username, password):
        conn = self.create_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM logins WHERE username=? AND password=?", (username, password))
        result = c.fetchone()
        conn.close()
        return result is not None

    def update_camper_data(self, f_name, l_name, gender, dob, mobile, address, city, state, zipcode, email, bunkhouse, tribe):
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
                            zipcode = '{zipcode}',
                            bunkhouse = '{bunkhouse}',
                            tribe = '{tribe}'
                            WHERE email = '{email}'""")
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False

    def camper_count_with_condition(self, conditions):
        conn = self.create_connection()
        c = conn.cursor()
        try:
            c.execute(f"""SELECT COUNT(*) FROM campers WHERE {conditions}""")
            result = c.fetchone()[0]
            conn.close()
            return result
        except Exception as e:
            print(e)
            return False
        return count

    def camper_count(self):
        conn = self.create_connection()
        c = conn.cursor()
        try:
            c.execute(f"""SELECT COUNT(*) FROM campers""")
            result = c.fetchone()[0]
            conn.close()
            return result
        except Exception as e:
            print(e)
            return False
        return count

    def reset_camper(self):
        conn = self.create_connection()
        c = conn.cursor()
        c.execute('UPDATE campers SET bunkhouse = NULL, tribe = NULL')
        conn.commit()
        conn.close()

    def assign_bunkhouses(self):
        conn = self.create_connection()
        c = conn.cursor()

        c.execute(
            'SELECT first_name, last_name, gender, date_of_birth, mobile, address, city, state, zipcode, email, registration_date, bunkhouse, tribe FROM campers ORDER BY date_of_birth')
        campers = c.fetchall()

        male_count = 0
        female_count = 0
        for camper in campers:
            if camper[2] == 'Male':
                if male_count < 12:
                    c.execute('UPDATE campers SET bunkhouse = ? WHERE first_name = ? AND last_name = ?',
                              (1, camper[0], camper[1]))
                elif male_count < 24:
                    c.execute('UPDATE campers SET bunkhouse = ? WHERE first_name = ? AND last_name = ?',
                              (2, camper[0], camper[1]))
                elif male_count < 36:
                    c.execute('UPDATE campers SET bunkhouse = ? WHERE first_name = ? AND last_name = ?',
                              (3, camper[0], camper[1]))
                else:
                    print("Error assigning male camper bunkhouse")
                male_count += 1
            elif camper[2] == 'Female':
                if female_count < 12:
                    c.execute('UPDATE campers SET bunkhouse = ? WHERE first_name = ? AND last_name = ?',
                              (4, camper[0], camper[1]))
                elif female_count < 24:
                    c.execute('UPDATE campers SET bunkhouse = ? WHERE first_name = ? AND last_name = ?',
                              (5, camper[0], camper[1]))
                elif female_count < 36:
                    c.execute('UPDATE campers SET bunkhouse = ? WHERE first_name = ? AND last_name = ?',
                              (6, camper[0], camper[1]))
                else:
                    print("Error assigning female camper bunkhouse")
                female_count += 1

        conn.commit()
        conn.close()

    def assign_tribes(self):
        conn = self.create_connection()
        c = conn.cursor()

        c.execute(
            'SELECT first_name, last_name, gender, date_of_birth, mobile, address, city, state, zipcode, email, registration_date, bunkhouse, tribe FROM campers ORDER BY date_of_birth')
        campers = c.fetchall()

        male_count = 0
        female_count = 0
        for camper in campers:
            if camper[2] == 'Male':
                if male_count < 6:
                    c.execute('UPDATE campers SET tribe = ? WHERE first_name = ? AND last_name = ?',
                              (1, camper[0], camper[1]))
                elif male_count < 12:
                    c.execute('UPDATE campers SET tribe = ? WHERE first_name = ? AND last_name = ?',
                              (2, camper[0], camper[1]))
                elif male_count < 18:
                    c.execute('UPDATE campers SET tribe = ? WHERE first_name = ? AND last_name = ?',
                              (3, camper[0], camper[1]))
                elif male_count < 24:
                    c.execute('UPDATE campers SET tribe = ? WHERE first_name = ? AND last_name = ?',
                              (4, camper[0], camper[1]))
                elif male_count < 30:
                    c.execute('UPDATE campers SET tribe = ? WHERE first_name = ? AND last_name = ?',
                              (5, camper[0], camper[1]))
                elif male_count < 36:
                    c.execute('UPDATE campers SET tribe = ? WHERE first_name = ? AND last_name = ?',
                              (6, camper[0], camper[1]))
                else:
                    print("Error assigning male camper tribe")
                male_count += 1
            elif camper[2] == 'Female':
                if female_count < 6:
                    c.execute('UPDATE campers SET tribe = ? WHERE first_name = ? AND last_name = ?',
                              (1, camper[0], camper[1]))
                elif female_count < 12:
                    c.execute('UPDATE campers SET tribe = ? WHERE first_name = ? AND last_name = ?',
                              (2, camper[0], camper[1]))
                elif female_count < 18:
                    c.execute('UPDATE campers SET tribe = ? WHERE first_name = ? AND last_name = ?',
                              (3, camper[0], camper[1]))
                elif female_count < 24:
                    c.execute('UPDATE campers SET tribe = ? WHERE first_name = ? AND last_name = ?',
                              (4, camper[0], camper[1]))
                elif female_count < 30:
                    c.execute('UPDATE campers SET tribe = ? WHERE first_name = ? AND last_name = ?',
                              (5, camper[0], camper[1]))
                elif female_count < 36:
                    c.execute('UPDATE campers SET tribe = ? WHERE first_name = ? AND last_name = ?',
                              (6, camper[0], camper[1]))
                else:
                    print("Error assigning female camper tribe")
                female_count += 1

        conn.commit()
        conn.close()
