import sqlite3
mybookstore=sqlite3.connect('bookstore.db')
book=mybookstore.cursor()
sql="select * from BOOKSTORE;"
book.execute(sql)
result=book.fetchall()
print("**** THE LIST OF BOOKS THAT WE HAVE*****")
for i in result:
    print(i)
try:
    title=input("enter the book title :")
    sql="select * from BOOKSTORE where BOOK_NAME='"+title+"';"
    book.execute(sql)
    result=book.fetchone()
    for i in result:
        print(i)
    quant=int(input("Enter the number of book you take :"))
    print("ADD MORE COPIES OR NOT")
    ans=input("yes/no:")
    if(ans=='yes'):
        c=0
        c=int(input("now add more copies :"))
        c=c+quant
    elif(ans=='no'):
        c=quant
    else:
        pass
    sql="select BOOK_PRICE from BOOKSTORE where BOOK_NAME='"+title+"';"
    book.execute(sql)
    result=book.fetchone()
    for i in result:
        print("the cost of the book is ",i)
        print("the number of copies you take ",c)
        print("total cost of the book is ", i*c)
    #result=int(result)       
    # print("the cost of the book is : ",result)
    # print("your total quantity ", c)
    # print("The total price of the book is ", result*c )    
except:
    print("your input is wrong ")
    mybookstore.rollback()


mybookstore.close()