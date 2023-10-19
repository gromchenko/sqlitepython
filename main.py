import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


connection = create_connection('apteka_sklad.db')
create_products_table = """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER,
    count INTEGER,
    wight TEXT,
    date DATE,
    srok INTEGER,
    id_sup INTEGER,
    FOREIGN KEY (id_sup) REFERENCES suppliers (id)
);"""
create_suppliers_table = """
CREATE TABLE IF NOT EXISTS suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT,
    contact TEXT,
    phone TEXT,
    email TEXT
);"""

create_supproducts_table = """
CREATE TABLE IF NOT EXISTS supproducts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_product INTEGER,
    id_supplier INTEGER,
    count INTEGER,
    date DATE,
    FOREIGN KEY (id_product) REFERENCES products (id),
    FOREIGN KEY (id_supplier) REFERENCES suppliers (id));"""
execute_query(connection, create_products_table)
execute_query(connection, create_suppliers_table)
execute_query(connection, create_supproducts_table)

#ВСТАВКА  (ДОБАВЛЕНИЕ) ЗАПИСЕЙ


create_suppliers = """
INSERT INTO
suppliers (name, address, contact, phone, email)
VALUES
('Поставщик 1', 'Тула, ул. Рязанская, д. 20', 'petrov', '(4872) 25-25-25', 'post1@yundex.ru'),
('Поставщик 2', 'Тула, ул. Рязанская,д. 25', 'ivanov', '(4872) 26-26-26', 'post2@yundex.ru'),
('Поставщик 3', 'Тула, ул Рязанская,д. 30', 'sidorov', '(4872) 27-27-27', 'post3@yundex.ru'),
('Поставщик 4', 'Тула, ул Рязанская,д. 35', 'tulskiy', '(4872) 28-28-28', 'post4@yundex.ru')
"""
#execute_query(connection, create_suppliers)


create_products = """
INSERT INTO
products (name, price, count, wight, date, srok, id_sup)
VALUES
('Продукт 1', 1000, 20, '50г', '2023-10-17', 12, 1),
('Продукт 2', 2000, 30, '60г', '2023-11-18', 13, 2),
('Продукт 3', 3000, 40, '70г', '2023-12-19', 14, 3),
('Продукт 4', 4000, 50, '80г', '2023-09-20', 15, 4)
"""
#execute_query(connection, create_products)

create_supproducts = """
INSERT INTO
supproducts (id_product, id_supplier, count, date)
VALUES
(1, 1, 200, '2023-10-17'),
(2, 2, 300, '2023-10-18'),
(3, 3, 400, '2023-10-19'),
(4, 4, 500, '2023-10-20')
"""
#execute_query(connection, create_supproducts)

#select_products = "SELECT * from products"
#products = execute_read_query(connection, select_products)
#for product in products:
#    print(products)

#select_suppliers = "SELECT * from suppliers"
#suppliers = execute_read_query(connection, select_suppliers)
#for supplier in suppliers:
#    print(supplier)

#select_supproducts = "SELECT * from supproducts"
#supproducts = execute_read_query(connection, select_supproducts)
#for supproduct in supproducts:
#    print(supproduct)

#По введенному товару выдает список поставщиков.


select_products_supplier = """
SELECT products.id, products.name, suppliers.name
FROM products
INNER JOIN suppliers ON products.id_sup = suppliers.id
"""
products_supplier = execute_read_query(connection, select_products_supplier)
#for products_supplie in products_supplier:
#    print(products_supplie)


select_products_supproducts= """
SELECT products.name, supproducts.count
FROM products
INNER JOIN supproducts ON products.id = supproducts.id_product
"""
products_supproducts = execute_read_query(connection, select_products_supproducts)
#for products_supproduct in products_supproducts:
#    print(products_supproduct)

select_product_where= """
SELECT * FROM products WHERE count > 40
"""
product_where = execute_read_query(connection, select_product_where)
#for product_wher in product_where:
#    print(product_wher)

select_product_where_2= """
SELECT * FROM products WHERE id = 2
"""
product_where_2 = execute_read_query(connection, select_product_where_2)
#for product_wher in product_where_2:
#    print(product_wher)

update_products_name = """
UPDATE products
SET
name = "Товар 22"
WHERE id = 2
"""
execute_query(connection, update_products_name)

delete_comment = "DELETE FROM products WHERE id = 3"
execute_query(connection, delete_comment)


select_product_all= """
SELECT * FROM products
"""
product_all = execute_read_query(connection, select_product_all)
for product_al in product_all:
    print(product_al)
