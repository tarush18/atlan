#create a database 
import sqlite3
mybookstore=sqlite3.connect('bookstore.db')
id=int(input("enter the book id :"))
author=input("Enter the book author :")
price=int(input("enter the price of books: "))
name=input("Enter the book name: ")
try:
    book=mybookstore.cursor()
    # book.execute(""" CREATE TABLE BOOKSTORE(
    #             BOOK_ID INT(20),
    #             BOOK_NAME VARCHAR(20),
    #             BOOK_AUTHOR VARCHAR(20),
    #             BOOK_PRICE INT(20)
    #         );""")
    book.execute("insert into BOOKSTORE values(?,?,?,?);",(id,name,author,price));
    #book.execute("insert into BOOKSTORE values(101,'c++','mamta',520);")
    # curschool.execute("INSERT INTO students VALUES (5,'Sherlock',32,50);")
    print("one record enter succesfuuly ")
    mybookstore.commit()
except:
   print("your entry is wrong ")
   mybookstore.rollback()

mybookstore.close()
 