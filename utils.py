import logging

import psycopg2

logger = logging.getLogger(__name__)

pool = None


def init_pool(p):
    global pool
    pool = p


def _execute_query(query, params=None):
    conn = None
    cursor = None
    try:
        conn = pool.getconn()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        return cursor.fetchall() if cursor.description else None
    except (Exception, psycopg2.Error) as error:
        logger.error(f"Database error: {error}")
        if conn:
            conn.rollback()
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            pool.putconn(conn)
