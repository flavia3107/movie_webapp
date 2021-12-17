from flask import Flask, render_template, request, redirect
from datetime import datetime
from mysql.connector import connect, Error
import mysql.connector


# import MySQLdb
# import sshtunnel

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

# try:
#     mydb = mysql.connector.connect( 
#         user="sql11459575",
#         password="8RWAvpjBuH",
#         host="sql11.freemysqlhosting.net",
#         port=3306,
#         database="sql11459575"
#     )
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with your user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   mydb.close()

# CREATE TABLE `bookings` (
#  `id` int(11) NOT NULL,
#  `firstname` varchar(40) NOT NULL,
#  `lastname` varchar(40) NOT NULL,
#  `package` varchar(30) NOT NULL,
#  `email` text NOT NULL,
#  `phone_number` text NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=latin1


cnx = mysql.connector.connect(user ='sql11459575', password= '8RWAvpjBuH', host = 'sql11.freemysqlhosting.net',port='3306', database='sql11459575')

cursor = cnx.cursor()


# try:
#     with connect(
#         host="sql11.freemysqlhosting.net",
#          user="sql11459575",
#         password="8RWAvpjBuH",
#           database="sql11459575"
#     ) as connection:
#         print(connection)
# except Error as e:
#     print(e)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/reserve")
def reserve():
    return render_template("reserve.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        firstname = 'Test Test'
        lastname = 'Test Test'
        email = 'test@test.com'
        package = 'albanian holiday'
        phone_number = '555 55555555'
   
        cursor.execute("INSERT INTO bookings (firstname, lastname, email , package, phone_number) VALUES(%s, %s, %s, %s, %s)",( firstname, lastname, email, package, phone_number ))
        cnx.commit()
        return render_template("highlights.html")
    else:    
        return render_template("register.html")

@app.route("/sailing")
def sailing():
    return render_template("sailing.html")

@app.route("/highlights")
def highlights():
    return render_template("highlights.html")

@app.route("/walking")
def walking():
    return render_template("walking.html")


if __name__ == "__main__":
    app.run()