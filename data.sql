
mysql> show databases
    -> ;
+--------------------+
| Database           |
+--------------------+
| farahshop          |
| information_schema |
| mysql              |
| performance_schema |
| sakila             |
| sys                |
| todolist           |
| world              |
+--------------------+
8 rows in set (1.23 sec)

mysql> use farahshop;
Database changed
mysql> show tables;
+---------------------+
| Tables_in_farahshop |
+---------------------+
| customer            |
+---------------------+
1 row in set (0.37 sec)

mysql> desc  customer;
+-------------+-------------+------+-----+-------------------+-------------------+
| Field       | Type        | Null | Key | Default           | Extra             |
+-------------+-------------+------+-----+-------------------+-------------------+
| ID          | int         | NO   | PRI | NULL              | auto_increment    |
| FirstName   | varchar(45) | YES  |     | NULL              |                   |
| LastName    | varchar(45) | YES  |     | NULL              |                   |
| Adresse     | varchar(45) | YES  |     | NULL              |                   |
| Email       | varchar(45) | YES  |     | NULL              |                   |
| PhoneNumber | bigint      | YES  |     | NULL              |                   |
| Item        | varchar(45) | YES  |     | NULL              |                   |
| Quantity    | int         | YES  |     | NULL              |                   |
| Color       | varchar(45) | YES  |     | NULL              |                   |
| Size        | varchar(10) | YES  |     | NULL              |                   |
| PaymentType | varchar(45) | YES  |     | NULL              |                   |
| CardNumber  | bigint      | YES  |     | NULL              |                   |
| CodePromo   | varchar(10) | YES  |     | NULL              |                   |
| Discount    | int         | YES  |     | NULL              |                   |
| Price       | float       | YES  |     | NULL              |                   |
| Date        | datetime    | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+-------------+-------------+------+-----+-------------------+-------------------+
16 rows in set (0.37 sec)

mysql> select  *  from customer;
+----+-----------+----------+-----------+-------------------------+-------------+---------------+----------+-------+------+-------------+------------+-----------+----------+-------+---------------------+
| ID | FirstName | LastName | Adresse   | Email                   | PhoneNumber | Item          | Quantity | Color | Size | PaymentType | CardNumber | CodePromo | Discount | Price | Date                |
+----+-----------+----------+-----------+-------------------------+-------------+---------------+----------+-------+------+-------------+------------+-----------+----------+-------+---------------------+
|  8 | hgads     | jehw     | jkhde     | zxcvbnm                 |      675234 | long skirt    |       10 | pink  |  S   | visa        |       4644 | Yes       |       45 |  1375 | 2024-03-26 01:29:43 |
|  9 | wissal    | loutfi   | agadir    | wissalloutfi@gmail.com  |    67365281 | long skirt    |        2 | brown |  S   | visa        |      53462 | Yes       |       20 |   400 | 2024-03-26 04:03:01 |
| 11 | hjgws     | qhwb     | hjbws     | ghvswq                  |     2354156 | long skirt    |       12 | green | XS   | visa        |         12 | Yes       |       98 |    60 | 2024-03-26 04:22:57 |
| 16 | salima    | alami    | rabat     | salima@gmail.com        |    64261462 | long skirt    |        3 | blue  |  M   | visa        |     653267 | Yes       |       20 |   600 | 2024-03-26 05:28:12 |
| 18 | farah     | saiza    | marrakech | farahsaiza@gmail.com    |    46321763 | wedding shoes |        5 | green |  M   | master      |     783426 | Yes       |       80 |   300 | 2024-03-26 05:31:06 |
| 19 | farah     | saiza    | marrakech | farahsaiza@gmail.com    |    46321763 | wedding shoes |        5 | green |  M   | master      |     783426 | Yes       |       80 |   300 | 2024-03-26 05:31:07 |
| 20 | farah     | saiza    | marrakech | farahsaiza@gmail.com    |    46321763 | wedding shoes |        5 | green |  M   | master      |     783426 | Yes       |       80 |   300 | 2024-03-26 05:31:07 |
| 21 | farah     | saiza    | marrakech | farahsaiza@gmail.com    |    46321763 | wedding shoes |        5 | green |  M   | master      |     783426 | Yes       |       80 |   300 | 2024-03-26 05:31:08 |
| 22 | farah     | saiza    | marrakech | farahsaiza@gmail.com    |    46321763 | wedding shoes |        5 | green |  M   | master      |     783426 | Yes       |       80 |   300 | 2024-03-26 05:31:08 |
| 23 | farah     | saiza    | marrakech | farahsaiza@gmail.com    |    46321763 | wedding shoes |        5 | green |  M   | master      |     783426 | Yes       |       80 |   300 | 2024-03-26 05:31:09 |
| 24 | farah     | saiza    | marrakech | farahsaiza@gmail.com    |    46321763 | wedding shoes |        5 | green |  M   | master      |     783426 | Yes       |       80 |   300 | 2024-03-26 05:31:09 |
| 25 | wissal    | loutfi   | agadir    | wissalloutfi@gmail.com  |   777342676 | Brown bag     |        2 | brown |  XL  | master      |       7632 | Yes       |       15 |   850 | 2024-03-26 05:37:47 |
| 26 | farah     | saiza    | marrakech | farahsaiza@gmail.com    |     6826465 | long skirt    |        2 | blue  |  M   | master      |      65353 | Yes       |       20 |   400 | 2024-03-26 11:34:25 |
| 28 | farah     | saiza    | marrakech | farahsaiza@gmail.com    | 25417612876 | long skirt    |        2 | blue  |  L   | master      |     256341 | Yes       |       15 |   425 | 2024-05-02 18:16:24 |
+----+-----------+----------+-----------+-------------------------+-------------+---------------+----------+-------+------+-------------+------------+-----------+----------+-------+---------------------+
14 rows in set (0.05 sec)
