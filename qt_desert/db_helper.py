import pymysql

DB_CONFIG = dict(
    host = 'localhost',
    user = 'root',
    password = '1102',
    database = 'desertdb',
    charset = 'utf8'
)

class DB:
    def __init__(self, **config):
        self.config = config

    def connect(self):
        return pymysql.connect(**self.config)

    def watch_products(self):
        sql = 'select * from products'
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()

    def watch_names(self):
            sql = 'select name from products'
            with self.connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    return cur.fetchall()

    def insert_product(self, name, price, count):
        sql = 'insert into products (name, price, count) values (%s, %s, %s)'
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (name, price, count))
                conn.commit()
                return True
            except Exception:
                conn.rollback()
                return False

    def delete_product(self, name):
        sql = 'delete from products where name=%s'
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (name))
                conn.commit()
                return True
            except Exception:
                conn.rollback()
                return False

    def update_name(self, name, new_name):
        sql = 'update products set name=%s where name=%s'
        with self.connect() as conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, (new_name, name))
                conn.commit()
                return True
            except Exception:
                conn.rollback()
                return False

    def update_price(self, name, new_price):
            sql = 'update products set price=%s where name=%s'
            with self.connect() as conn:
                try:
                    with conn.cursor() as cur:
                        cur.execute(sql, (new_price, name))
                    conn.commit()
                    return True
                except Exception:
                    conn.rollback()
                    return False

    def update_count(self, name, new_count):
            sql = 'update products set count=%s where name=%s'
            with self.connect() as conn:
                try:
                    with conn.cursor() as cur:
                        cur.execute(sql, (new_count, name))
                    conn.commit()
                    return True
                except Exception:
                    conn.rollback()
                    return False