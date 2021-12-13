from flask import Flask, render_template, request, redirect
from datetime import datetime
# import MySQLdb
# import sshtunnel

app = Flask(__name__)



# sshtunnel.SSH_TIMEOUT = 5.0
# sshtunnel.TUNNEL_TIMEOUT = 5.0

# with sshtunnel.SSHTunnelForwarder(
#     ('your SSH hostname'),
#     ssh_username='your PythonAnywhere username', ssh_password='the password you use to log in to the PythonAnywhere website',
#     remote_bind_address=('your PythonAnywhere database hostname, eg. yourusername.mysql.pythonanywhere-services.com', 3306)
# ) as tunnel:
#     connection = MySQLdb.connect(
#         user='your PythonAnywhere database username',
#         passwd='your PythonAnywhere database password',
#         host='127.0.0.1', port=tunnel.local_bind_port,
#         db='your database name, eg yourusername$mydatabase',
#     )
#     # Do stuff
#     connection.close()



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
        client = 'Test Test'
        email = 'test@test.com'
        package = 'albanian holiday'
        phone = '555 55555555'

        # data = Bookings(client=client, email=email, package=package, phone=phone)
        try:
            # db.session.add(data)
            # db.session.commit()
            return render_template("highlights.html")
        except:
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
# @app.route("/path")
# def test():
# return redirect(url_for("movie", var=varMew))


if __name__ == "__main__":
    app.run()