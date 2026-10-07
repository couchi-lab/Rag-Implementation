import sys
from pathlib import Path
import psycopg
sys.path.append(str(Path(__file__).parent.parent))
from setting import DB_PASSWORD, PORT, DSN

import asyncio

async def get_connection():
    return psycopg.connect(
        host="localhost",
        port=PORT,
        dbname=DSN,
        user="postgres",
        password=DB_PASSWORD
    )


async def add_user(func,name):
    conn = await get_connection()

    with conn.cursor() as cur:
        cur.execute(
            func,
            (name,)
        )

    conn.commit()
    conn.close()

async def update_user(primary_key, new_name):
    conn = await get_connection()

    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE users
            SET name = %s
            WHERE id = %s
            """,
            (new_name, primary_key)
        )

    conn.commit()
    conn.close()
if __name__ == "__main__":
    async def main():
        await add_user("INSERT INTO users(name) VALUES(%s)", "Alice")
        await update_user(1, "Alice Updated")

    asyncio.run(main())

