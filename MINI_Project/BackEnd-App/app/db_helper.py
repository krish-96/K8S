from db_connection import get_connection
from logs_configs import logger


def execute_query(query, connection=None):
    try:
        if not connection:
            connection = get_connection()
        if not query:
            raise Exception("Query is reuqired")
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as query_exec_err:
        logger.error(f"Exception occurred while executing the query, {query_exec_err}")


def execute_ddl_query(query, connection=None):
    try:
        if not connection:
            connection = get_connection()
        if not query:
            raise Exception("Query is reuqired")
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    except Exception as query_exec_err:
        logger.error(f"Exception occurred while executing the query, {query_exec_err}")


def check_table(query, connection=None):
    try:
        if not connection:
            connection = get_connection()
        if not query:
            raise Exception("Query is reuqired")
        cursor = connection.cursor()
        cursor.execute(query)
        return True
    except Exception as query_exec_err:
        logger.error(f"Exception occurred while executing the query, {query_exec_err}")
        return False
