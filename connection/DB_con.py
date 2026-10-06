import sys
from pathlib import Path
import psycopg
sys.path.append(str(Path(__file__).parent.parent))
from setting import DB_PASSWORD, PORT, DSN


def get_connection():
    return psycopg.connect(
        host="localhost",
        port=PORT,
        dbname=DSN,
        user="postgres",
        password=DB_PASSWORD
    )

def add_user(name):
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO users(name) VALUES(%s)",
            (name,)
        )

    conn.commit()
    conn.close()
def get_users():
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users")

        users = cur.fetchall()

    conn.close()

    return users
def get_user(user_id):
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM users WHERE id = %s",
            (user_id,)
        )

        user = cur.fetchone()

    conn.close()

    return user

def update_user(user_id, new_name):
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE users
            SET name = %s
            WHERE id = %s
            """,
            (new_name, user_id)
        )

    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM users WHERE id = %s",
            (user_id,)
        )

    conn.commit()
    conn.close()

