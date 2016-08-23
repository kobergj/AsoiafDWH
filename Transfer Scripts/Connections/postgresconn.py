import psycopg2

class Connection:
    def __init__(self, db, uid, pwd):
        self.conn = psycopg2.connect(dbname=db, user=uid, password=pwd)

    def __call__(self, querygenerator):
        query = querygenerator()

        cur = self.conn.cursor()

        cur.execute(query)

        result = cur.fetchall()

        self.conn.commit()

        if result:
            primId = result[0][0]
            return primId