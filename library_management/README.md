----------
ENTITIES
----------
1.staff
2.readers
3.books 
4.publisher
5.authentication system
6.reports
-----------
ATTRIBUTES
-----------
1.staff
-----------
* staff_id 
* name 

-----------
2.readers
-----------
* user_id
* email
* name
    * firstname
    * lastname
* phone no
* address
* reserve date 
* return date
* due date

-----------
3.books
-----------
* authno
* ISBN
* title
* edition
* category
* price

------------
4.publisher
------------
* publisher_id
* year of publication
* name

------------------------
5.authentication system
------------------------
* password
* login_id

-----------
6.reports
-----------
* user_id
* reg no
* books no
* issue/return

staff -> readers,books,login,reports
books -> publisher
