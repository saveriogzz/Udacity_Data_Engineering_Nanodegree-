import configparser
import psycopg2
from time import time
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Function that drops, if exist,
    tables that are going to be created in the next step.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Function that creates tables
    by iterating the queries in the query script.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    t0 = time()
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()

    print('Done in {t:.2f} s'.format(t=time()-t0))


if __name__ == "__main__":
    main()