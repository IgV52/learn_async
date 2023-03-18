from typing import List

import asyncio
import asyncpg
import schema_create_db

async def main():
    connection = await asyncpg.connect(host="127.0.0.1",
                                       port=5432,
                                       user="postgres",
                                       database="products",
                                       password="postgres")
    
    statements = [
        schema_create_db.CREATE_BRAND_TABLE,
        schema_create_db.CREATE_PRODUCT_TABLE,
        schema_create_db.CREATE_PRODUCT_COLOR_TABLE,
        schema_create_db.CREATE_PRODUCT_SIZE_TABLE,
        schema_create_db.CREATE_SKU_TABLE,
        schema_create_db.SIZE_INSERT,
        schema_create_db.COLOR_INSERT
    ]

    print(f"Создается база данных product...")
    for statement in statements:
        status = await connection.execute(statement)
        print(status)
    print("База данных product создана!")
    await connection.close()

async def main_fetch():
    connection = await asyncpg.connect(host="127.0.0.1",
                                       port=5432,
                                       user="postgres",
                                       database="products",
                                       password="postgres")
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')")
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')")

    brand_query = "SELECT brand_id, brand_name FROM brand"
    results: List[asyncpg.Record] = await connection.fetch(brand_query)

    for brand in results:
        print(f"id: {brand['brand_id']}, name: {brand['brand_name']}")
    await connection.close()

asyncio.run(main_fetch())