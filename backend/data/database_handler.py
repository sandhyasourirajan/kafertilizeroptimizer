import psycopg2
from psycopg2.extras import RealDictCursor
import logging
from backend.config.config_parser import configuration

class DatabaseConnection:


    """
        This Class fetches content from iimb_cabes_db - iimb_cabes_fertilizer_schema
    """

    def __init__(self):
        # db credentials
        self.name = configuration.get('DatabaseSection', 'db_username',fallback=None)
        self.password = configuration.get('DatabaseSection', 'db_password',fallback=None)
        self.db_name = configuration.get('DatabaseSection', 'db_name',fallback=None)

        # database host config
        self.db_host = configuration.get('DatabaseSection', 'db_host',fallback=None)
        self.db_port = configuration.get('DatabaseSection', 'db_port',fallback=None)
        self.schema = configuration.get('DatabaseSection', 'db_schema',fallback=None)

        # logger
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger()

        """
            Now try connecting to the database
        """

        try:
            self.conn = psycopg2.connect(
                                        user=self.name, password=self.password,
                                        database=self.db_name, host=self.db_host, port=self.db_port,
                                        options=f'-c search_path={self.schema}'
                                        )
            self.logger.info("SUCCESS: Connection to database instance succeeded")
        except psycopg2.Warning as e:
            self.logger.error("Warning")
            self.logger.error(e)

        except psycopg2.Error as e:
            self.logger.error("InternalError")
            self.logger.error(e)

        except:
            self.logger.error("Unknown error occurred")


    def select_table_detail(self,sql,params):

        # Select the contents of the postgres table

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql,params)
                data = cursor.fetchall()
                
            return data

        # Handle any query errors
        #

        except psycopg2.Warning as e:
            self.logger.error("Warning")
            self.logger.error(e)
            return e

        except psycopg2.Error as e:
            self.logger.error("InternalError")
            self.logger.error(e)
            return e

    def insert_table_detail(self,sql,params):
        # Insert into postgres table
        cursor = self.conn.cursor()

        try:
            # with self.conn.cursor() as cursor:
            cursor.execute(sql,params)
            self.conn.commit()
            self.conn.close;
            return "You have successfully inserted data into the database"

        # Handle any query errors
        #

        except psycopg2.Warning as e:
            self.logger.error("Warning")
            self.logger.error(e)
            return e

        except psycopg2.Error as e:
            self.logger.error("InternalError")
            self.logger.error(e)
            return e

    def update_table_detail(self,sql,params):
        # Insert into postgres table

        cursor = self.conn.cursor();

        try:
            cursor_data = cursor.execute(sql,params);
            self.conn.commit();
            self.conn.close;
            message = "Database edit completed successfully"
            return message

        except psycopg2.Warning as e:
            self.logger.error("Warning")
            self.logger.error(e)
            return e

        except psycopg2.Error as e:
            self.logger.error("InternalError")
            self.logger.error(e)
            return e
