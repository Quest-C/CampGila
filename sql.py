CREATE_LOGIN_TABLE_SQL = """CREATE TABLE IF NOT EXISTS logins(
                            username text, 
                            password text,
                            UNIQUE(username))
                        """

CREATE_CAMPERS_TABLE_SQL = """CREATE TABLE IF NOT EXISTS campers(
                                first_name text NOT NULL,
                                last_name text NOT NULL, 
                                gender text NOT NULL, 
                                date_of_birth text, 
                                mobile text NOT NULL, 
                                address text, 
                                city text,
                                state text, 
                                zipcode text, 
                                email text PRIMARY KEY, 
                                registration_date text,
                                bunkhouse text,
                                tribe text)
                            """

CREATE_PAYMENTS_TABLE_SQL = """
                            CREATE TABLE IF NOT EXISTS payments(
                            transaction_id integer PRIMARY KEY, 
                            email text, 
                            payment_date text NOT NULL, 
                            payment_amount text NOT NULL, 
                            FOREIGN KEY(email) REFERENCES campers(email)
                                ON DELETE NO ACTION
                            )
                            """
