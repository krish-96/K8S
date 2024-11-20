import os

from db_connection import get_connection
from functools import lru_cache

# Module constants
DB_CON_FAILED = "Database Connection Failed"
DB_VERSION_FETCH_FAILED = "Database Version Fetch Failed"


def get_db_version():
    try:
        connection = get_connection()
        if not connection:
            print(DB_CON_FAILED)
            return DB_CON_FAILED
        print(f"Connection received, Con: {connection}")
        cursor = connection.cursor()
        cursor.execute("select version();")
        postgres_details = cursor.fetchall()
        if postgres_details:
            postgres_details = postgres_details[0]
        return postgres_details
    except Exception as db_version_err:
        from logs_configs import logger
        logger.error(f"Exception occurred while Fetching the DB version, Exception: {db_version_err}")
        return DB_VERSION_FETCH_FAILED


@lru_cache(maxsize=1)
def get_cache_db_version():
    try:
        return get_db_version()
    except Exception as db_version_err:
        from logs_configs import logger
        logger.error(f"Exception occurred while Fetching the DB version (Cache), Exception: {db_version_err}")
        return DB_VERSION_FETCH_FAILED


def create_dir(dirs):
    try:
        print("Creating directories")
        os.makedirs(os.path.dirname(dirs), exist_ok=True)
        print(f"Created directories @ {dirs}")
    except Exception as dir_create_err:
        from logs_configs import logger
        logger.error(f"Failed to create the directories..., Exception: {dir_create_err}")
