#import library
from flask import Flask,redirect, url_for, render_template, request, session, flash
import datetime
from flask_cors import CORS
import json
import pymysql
import re
import recommendationBooking
import recommendationsLocation
import recommendations
import searchSportsCentre
from pprint import pprint

#Initializing Flask app
app = Flask(__name__)
app.secret_key = "hello"
app.jinja_env.filters["zip"] = zip
CORS(app) 


#Rendering index page      
@app.route('/')
def index():
    return render_template("index.html")

#Register page
@app.route('/register', methods=["POST", "GET"])
def register():

    msg = ''
    
    if request.method == 'POST':

        #Register account authentication
        if request.form["username"] == '' and request.form["email"] == '' and request.form["password"] == '' and request.form["location"] == 'Your location':
            msg = 'Please fill out the form!'    
            return render_template("register.html", message = msg)
        elif request.form["username"] == '':
            msg = 'Username is empty!'    
            return render_template("register.html", message = msg)
        elif request.form["email"] == '':
            msg = 'Email is empty!'    
            return render_template("register.html", message = msg)
        elif request.form["password"] == '':
            msg = 'Password is empty!'    
            return render_template("register.html", message = msg)
        elif request.form["location"] == 'Your location':
            msg = 'Location is empty!'    
            return render_template("register.html", message = msg)
        elif request.method =="POST" and 'username' in request.form and 'email' in request.form and 'password' in request.form and 'location' in request.form:
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            location = request.form['location']

            #Make a connection with local database
            connection = pymysql.connect(host ="localhost",user="root",password="",database="recommendationsport")
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            account = cursor.fetchone()
            
            if account:
                msg = 'Account already exists!'
                return render_template("register.html", message = msg)
            else:
                cursor.execute('INSERT INTO users VALUES (NULL, %s, %s, %s, %s)', (username, email, password,location,))
                connection.commit()
                msg = 'You have successfully registered!'
                return render_template("register.html", message = msg)
    else:
        return render_template("register.html", message = msg)
   
#Login Page
@app.route('/login', methods=["POST", "GET"])
def login():
    msg = ''

    
    if request.method =="POST":

        #Login account authentication
        if request.form["uname"] == '' and request.form["password"] == '':
            msg = 'Username and password is empty!'    
            return render_template("login.html", message = msg)
        elif request.form["uname"] == '':
            msg = 'Username is empty!'    
            return render_template("login.html", message = msg)
        elif request.form["password"] == '':
            msg = 'Password is empty!'    
            return render_template("login.html", message = msg)
        elif request.method =="POST" and 'uname' in request.form and 'password' in request.form:
    
            user = request.form["uname"]
            password = request.form["password"]
            session["user"] = user 

            connection = pymysql.connect(host ="localhost",user="root",password="",database="recommendationsport")
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (user, password,))
            account = cursor.fetchone()
            connection.commit()
            connection.close()

            if account:
                session['loggedin'] = True
                session['id'] = account[0]
                session['user'] = account[1]
                session['email'] = account[2]
                session['password'] = account[3]
                session['locationUser'] = account[4]
                id = session['id']

                return redirect(url_for("home"))
            else:
                msg = 'Incorrect username or password!'
                return render_template("login.html", message = msg)
    else:   
        return render_template("login.html", message = msg)

#Home page
@app.route('/home')
def home():
    if "user" in session:

        id = session['id']

        connection = pymysql.connect(host ="localhost",user="root", password="",database="recommendationsport")
        cursor = connection.cursor()
        #Query check if user already has booked in the system
        cursor.execute('SELECT sportsCentre FROM bookingcourt where user_id = %s order by order_id DESC LIMIT 1', (id,))
        row = cursor.fetchone()
        sportCheck = row

        #Sport centre recommendation for new user
        if sportCheck is None: 
            cursor2 = connection.cursor()  
            cursor2.execute('SELECT location FROM users where id = %s', (id,))
            row2 = str(cursor2.fetchone()[0])
            location = row2
            
            sportName = ""
            session['sportName'] = sportName
            session['location'] = location

            resData = recommendationsLocation.recommend(location)
            nameData = []
            locationData = []
            courtData = []
            for i in range(len(resData)):
                nameData.append(resData.iloc[i][0])
                locationData.append(resData.iloc[i][1])
                courtData.append(resData.iloc[i][2])

            connection.commit()
            connection.close()

            return render_template('homePage.html', nama=nameData, lokasi=locationData, gelanggang=courtData, res = resData, locaTion = location)
        
        #Sport centre recommendation based on latest booking
        else: 
            cursor3 = connection.cursor()
            cursor3.execute('SELECT sportsCentre FROM bookingcourt where user_id = %s order by order_id DESC LIMIT 1', (id,))
            row3 = str(cursor3.fetchone()[0])
            sportName = row3
            session['sportName'] = sportName

            resData = recommendationBooking.recommend(sportName)
            nameData = []
            locationData = []
            courtData = []

            #Fetching sports centre that already has been booking to display rating
            cursor4 = connection.cursor()
            cursor4.execute('SELECT sportsCentre, rating FROM bookingcourt where user_id = %s', (id,))
            ratingBook = cursor4.fetchall()
            rating = 0
            
            for i in range(len(resData)):
                    nameData.append(resData.iloc[i][0])
                    locationData.append(resData.iloc[i][1])
                    courtData.append(resData.iloc[i][2])
                        
            connection.commit()
            connection.close()
        
            return render_template("homePage.html", nama=nameData, lokasi=locationData, gelanggang=courtData, res = resData, sportname = sportName, ratingBook = ratingBook, rating = rating)
    else:
        return redirect(url_for("login"))
    

#Page of sports centre based on location filter
@app.route('/findSportCentreLocation', methods=["GET","POST"])
def findSportCentreLocation():
        if request.method == 'GET':
            return(render_template('findSportCentre.html'))
        else:
            location = request.form['location']
            session['searchLocation'] = location
            return redirect(url_for("findSportCentreLocationProcess"))
        
#Recommendation location filter process
@app.route('/findSportCentreLocationProcess', methods=["GET","POST"])
def findSportCentreLocationProcess():

        location = session['searchLocation']
        resData = recommendationsLocation.recommend(location)
        nameData = []
        locationData = []
        courtData = []

        connection = pymysql.connect(host ="localhost",user="root", password="",database="recommendationsport")
        cursor = connection.cursor()
        cursor.execute('SELECT sportsCentre, rating FROM bookingcourt where user_id = %s', (id,))
        ratingBook = cursor.fetchall()
        rating = 0
        connection.commit()
        connection.close()
        
        for i in range(len(resData)):
            nameData.append(resData.iloc[i][0])
            locationData.append(resData.iloc[i][1])
            courtData.append(resData.iloc[i][2])

        return render_template('outputSportLocation.html', nama=nameData, lokasi=locationData, gelanggang=courtData, locationFilter=location, res = resData, ratingBook = ratingBook, rating = rating)

#Page of sports centre based on court filter
@app.route('/findSportCentreCourt', methods=["GET","POST"])
def findSportCentreCourt():
        if request.method == 'GET':
            return(render_template('findSportCentreCourt.html'))
        else:
            court = request.form['court']
            session['typeCourt'] = court
            return redirect(url_for("findSportCentreCourtProcess"))

#Recommendation court filter process
@app.route('/findSportCentreCourtProcess', methods=["GET","POST"])
def findSportCentreCourtProcess():
        
        id = session['id']
        court = session['typeCourt']

        resData = recommendations.recommend(court)

        if court == "Badminton":
            resData = resData[0:30]
        elif court == "Futsal":
            resData = resData[0:30]

        nameData = []
        locationData = []
        courtData = []

        connection = pymysql.connect(host ="localhost",user="root", password="",database="recommendationsport")
        cursor = connection.cursor()
        cursor.execute('SELECT sportsCentre, rating FROM bookingcourt where user_id = %s', (id,))
        ratingBook = cursor.fetchall()
        rating = 0
        connection.commit()
        connection.close()

        for i in range(len(resData)):
                nameData.append(resData.iloc[i][0])
                locationData.append(resData.iloc[i][1])
                courtData.append(resData.iloc[i][2])
                
        return render_template('outputSportCourt.html', nama=nameData, lokasi=locationData, gelanggang=courtData, courtFilter=court, res = resData, ratingBook = ratingBook, rating = rating)

#Recommendation court filter page 2
@app.route('/findSportCentreCourt2', methods=["GET","POST"])
def findSportCentreCourt2():
        
        id = session['id']
        court = session['typeCourt']
        resData = recommendations.recommend(court)

        if court == "Badminton":
            resData = resData[31:61]
        elif court == "Futsal":
            resData = resData[31:61]

        nameData = []
        locationData = []
        courtData = []

        connection = pymysql.connect(host ="localhost",user="root", password="",database="recommendationsport")
        cursor = connection.cursor()
        cursor.execute('SELECT sportsCentre, rating FROM bookingcourt where user_id = %s', (id,))
        ratingBook = cursor.fetchall()
        rating = 0
        connection.commit()
        connection.close()

        for i in range(len(resData)):
            nameData.append(resData.iloc[i][0])
            locationData.append(resData.iloc[i][1])
            courtData.append(resData.iloc[i][2])

        return render_template('outputSportCourt2.html', nama=nameData, lokasi=locationData, gelanggang=courtData, courtFilter=court, res = resData, ratingBook = ratingBook, rating = rating)

#Recommendation court filter page 3
@app.route('/findSportCentreCourt3', methods=["GET","POST"])
def findSportCentreCourt3():
        
        id = session['id']
        court = session['typeCourt']
        resData = recommendations.recommend(court)

        if court == "Badminton":
            resData = resData[62:92]
        elif court == "Futsal":
            resData = resData[62:92]

        nameData = []
        locationData = []
        courtData = []

        connection = pymysql.connect(host ="localhost",user="root", password="",database="recommendationsport")
        cursor = connection.cursor()
        cursor.execute('SELECT sportsCentre, rating FROM bookingcourt where user_id = %s', (id,))
        ratingBook = cursor.fetchall()
        rating = 0
        connection.commit()
        connection.close()

        for i in range(len(resData)):
            nameData.append(resData.iloc[i][0])
            locationData.append(resData.iloc[i][1])
            courtData.append(resData.iloc[i][2])

        return render_template('outputSportCourt3.html', nama=nameData, lokasi=locationData, gelanggang=courtData, courtFilter=court, res = resData, ratingBook = ratingBook, rating = rating)

#Recommendation court filter page 4
@app.route('/findSportCentreCourt4', methods=["GET","POST"])
def findSportCentreCourt4():
        
        id = session['id']
        court = session['typeCourt']
        resData = recommendations.recommend(court)

        if court == "Badminton":
            resData = resData[93:123]
        elif court == "Futsal":
            resData = resData[93:123]

        nameData = []
        locationData = []
        courtData = []

        connection = pymysql.connect(host ="localhost",user="root", password="",database="recommendationsport")
        cursor = connection.cursor()
        cursor.execute('SELECT sportsCentre, rating FROM bookingcourt where user_id = %s', (id,))
        ratingBook = cursor.fetchall()
        rating = 0
        connection.commit()
        connection.close()

        for i in range(len(resData)):
            nameData.append(resData.iloc[i][0])
            locationData.append(resData.iloc[i][1])
            courtData.append(resData.iloc[i][2])

        return render_template('outputSportCourt4.html', nama=nameData, lokasi=locationData, gelanggang=courtData, courtFilter=court, res = resData, ratingBook = ratingBook, rating = rating)

#Recommendation court filter page 5
@app.route('/findSportCentreCourt5', methods=["GET","POST"])
def findSportCentreCourt5():
        
        id = session['id']
        court = session['typeCourt']
        resData = recommendations.recommend(court)

        if court == "Badminton":
            resData = resData[124:154]
        elif court == "Futsal":
            resData = resData[124:154]

        nameData = []
        locationData = []
        courtData = []

        connection = pymysql.connect(host ="localhost",user="root", password="",database="recommendationsport")
        cursor = connection.cursor()
        cursor.execute('SELECT sportsCentre, rating FROM bookingcourt where user_id = %s', (id,))
        ratingBook = cursor.fetchall()
        rating = 0
        connection.commit()
        connection.close()

        for i in range(len(resData)):
            nameData.append(resData.iloc[i][0])
            locationData.append(resData.iloc[i][1])
            courtData.append(resData.iloc[i][2])

        return render_template('outputSportCourt5.html', nama=nameData, lokasi=locationData, gelanggang=courtData, courtFilter=court, res = resData, ratingBook = ratingBook, rating = rating)

#Recommendation court filter page 6
@app.route('/findSportCentreCourt6', methods=["GET","POST"])
def findSportCentreCourt6():
        
        id = session['id']
        court = session['typeCourt']
        resData = recommendations.recommend(court)

        if court == "Badminton":
            resData = resData[155:185]
        elif court == "Futsal":
            resData = resData[155:160]

        nameData = []
        locationData = []
        courtData = []

        connection = pymysql.connect(host ="localhost",user="root", password="",database="recommendationsport")
        cursor = connection.cursor()
        cursor.execute('SELECT sportsCentre, rating FROM bookingcourt where user_id = %s', (id,))
        ratingBook = cursor.fetchall()
        rating = 0
        connection.commit()
        connection.close()

        for i in range(len(resData)):
            nameData.append(resData.iloc[i][0])
            locationData.append(resData.iloc[i][1])
            courtData.append(resData.iloc[i][2])

        return render_template('outputSportCourt6.html', nama=nameData, lokasi=locationData, gelanggang=courtData, courtFilter=court, res = resData, ratingBook = ratingBook, rating = rating)

#Recommendation court filter page 7
@app.route('/findSportCentreCourt7', methods=["GET","POST"])
def findSportCentreCourt7():
        
        id = session['id']
        court = session['typeCourt']
        resData = recommendations.recommend(court)

        if court == "Badminton":
            resData = resData[186:216]
        elif court == "Futsal":
            resData = resData[186:216]

        nameData = []
        locationData = []
        courtData = []

        connection = pymysql.connect(host ="localhost",user="root", password="",database="recommendationsport")
        cursor = connection.cursor()
        cursor.execute('SELECT sportsCentre, rating FROM bookingcourt where user_id = %s', (id,))
        ratingBook = cursor.fetchall()
        rating = 0
        connection.commit()
        connection.close()

        for i in range(len(resData)):
            nameData.append(resData.iloc[i][0])
            locationData.append(resData.iloc[i][1])
            courtData.append(resData.iloc[i][2])

        return render_template('outputSportCourt7.html', nama=nameData, lokasi=locationData, gelanggang=courtData, courtFilter=court, res = resData, ratingBook = ratingBook, rating = rating)

#Page of selected sports centre information
@app.route('/sportsCentreDetails', methods=["GET","POST"])
def sportsCentreDetails():
    if "user" in session:
        if request.method == 'POST':

            id = session['id']
            sportsCentreDetailsName = request.form['sportsCentre']
            session.modified = True
            session['sportsCentreDetailsName'] = sportsCentreDetailsName
            return redirect(url_for("sportsCentreDetailsProcess"))
           
        else:
            return redirect(url_for("login"))

@app.route('/sportsCentreDetailsProcess', methods=["GET","POST"])
def sportsCentreDetailsProcess():
    if "user" in session:
        sportsCentreDetailsName = session['sportsCentreDetailsName']
        resData = searchSportsCentre.recommend(sportsCentreDetailsName)
        nameData = []
        addressData = []
        locationData = []
        courtData = []

        for i in range(len(resData)):
                nameData.append(resData.iloc[i][0])
                addressData.append(resData.iloc[i][1])
                locationData.append(resData.iloc[i][2])
                courtData.append(resData.iloc[i][3])

        return render_template("sportsCentreDetails.html", nama=nameData, address=addressData, lokasi=locationData, gelanggang=courtData, res = resData)
    else:
            return redirect(url_for("login"))
    
#User booking history
@app.route('/bookingHistory', methods=["GET","POST"])
def bookingHistory():
    if "user" in session:

            from datetime import datetime, date, timedelta

            id = session['id']
            connection = pymysql.connect(host ="localhost",user="root",password="",database="recommendationsport")
            cursor = connection.cursor()
            cursor.execute('SELECT *, DATE(dateBooking) as dateBook from bookingcourt where user_id = %s', (id,))
            booking = cursor.fetchall()

            ratingDisplay = cursor.fetchall()
            rating = 0
            connection.commit()
            connection.close()

            #Get current date
            current_date = date.today()

            #Get current time
            timeNow = datetime.now()
            current_time = timedelta(hours=timeNow.hour, minutes=timeNow.minute, seconds=timeNow.second)

            return render_template("bookingHistory.html", book = booking, ratingDis = ratingDisplay, rating= rating, current_date=current_date, current_time = current_time)
    else:
        return redirect(url_for("login"))

#Selected booking history details
@app.route('/updateRating', methods=["GET","POST"])
def updateRating():
    if "user" in session:
        if request.method == 'POST':

            id = session['id']
            sportsCentreName = request.form['sportsCentreName']
            ratingBooking = request.form['ratingBooking']
            session.modified = True
            session['sportsCentreName'] = sportsCentreName
            session['ratingBooking'] = ratingBooking

            resData = searchSportsCentre.recommend(sportsCentreName)
            nameData = []
            addressData = []
            locationData = []
            courtData = []

            for i in range(len(resData)):
                    nameData.append(resData.iloc[i][0])
                    addressData.append(resData.iloc[i][1])
                    locationData.append(resData.iloc[i][2])
                    courtData.append(resData.iloc[i][3])

            return render_template("updateRating.html", nama=nameData, address=addressData, lokasi=locationData, gelanggang=courtData, res = resData)
        else:
            return redirect(url_for("login"))

#Update rating for selected sports centre that has been booked
@app.route('/updateRatingProcess', methods=["GET","POST"])
def updateRatingProcess():
    if "user" in session:

        if request.method == 'POST':

            id = session['id']
            ratingTest = request.form.get('rating')

            #Authenticate rating value
            if ratingTest is None:
                flash("Your given rating value is 0. Please try again!")
                return redirect(url_for("updateRatingProcess"))
            #Update rating
            else:
                ratingUpdate = request.form['rating']
                nameSportsCentre = request.form['nameSportsCentre']

                connection = pymysql.connect(host ="localhost",user="root",password="",database="recommendationsport")

                cursor = connection.cursor()
                cursor.execute('SELECT * from bookingcourt where user_id = %s and sportsCentre = %s', (id, nameSportsCentre,))
                bookRate = cursor.fetchall()

                if bookRate: 
                    cursor2 = connection.cursor()
                    cursor2.execute('UPDATE bookingcourt set rating = %s where user_id = %s and sportsCentre = %s', (ratingUpdate, id, nameSportsCentre,))
                    updateRating = cursor2.fetchall()
                    connection.commit()
                    connection.close()
                    flash("You have successfully update the rating for "+nameSportsCentre+". Thank you!")
                    return redirect(url_for("bookingHistory"))
                else :
                    return redirect(url_for("updateRatingProcess"))
        else :
            return render_template("updateRating.html")
        
#Make a booking cancellation
@app.route('/cancellationBooking', methods=["GET","POST"])
def cancellationBooking():
    if "user" in session:
        if request.method == 'POST':
            id = session['id']
            orderid = request.form['orderId']
            namaportsCentre = request.form['sportsCentreName']

            session.modified = True
            session['orderId'] = orderid
            session['namaportsCentre'] = namaportsCentre

            connection = pymysql.connect(host ="localhost",user="root",password="",database="recommendationsport")

            cursor = connection.cursor()
            cursor.execute('SELECT * from bookingcourt where order_id = %s', (orderid,))
            bookOrder = cursor.fetchone()
            connection.commit()
            connection.close()

            return render_template("cancellationBooking.html", book = bookOrder)

@app.route('/cancellationBookingProcess', methods=["GET","POST"])
def cancellationBookingProcess():
    if request.method == 'POST':

        orderId = session['orderId']

        connection = pymysql.connect(host ="localhost",user="root",password="",database="recommendationsport")

        cursor = connection.cursor()
        #Delete selected booking from database
        cursor.execute('DELETE from bookingcourt where order_id = %s', (orderId,))
        cancelBook = cursor.fetchone()
        connection.commit()
        connection.close()

        flash("You have successfully make cancellation booking for "+session['namaportsCentre']+". The payment will be refund to your bank account.")
        return redirect(url_for("bookingHistory"))

#User information page
@app.route('/userInfo', methods=["GET","POST"])
def userInfo():
    if "user" in session:
        if request.method =="POST":
            return redirect(url_for('editUser'))
        else:

            userName = session['user']
            eMail = session['email']
            passWord = session['password']
            locaTion = session['locationUser']

            return render_template("userInformation.html", username = userName, email = eMail, password = passWord, locationUser = locaTion)
    else:
        return redirect(url_for("login"))

#Update user information
@app.route('/editUser', methods=["GET","POST"])
def editUser():
    if "user" in session:
        if request.method =="POST":

            #Authenticate updating user information form
            if request.form["username"] == '':
                flash("Your username to be updated is empty!")   
                return redirect(url_for("editUser"))
            elif request.form["email"] == '':
                flash("Your email to be updated is empty!")    
                return redirect(url_for("editUser"))
            elif request.form["password"] == '':
                flash("Your password to be updated is empty!")
                return redirect(url_for("editUser"))   
            else:
                id = session['id']
                username = request.form['username']
                password = request.form['password']
                email = request.form['email']
                locationPlace = request.form['location']

                connection = pymysql.connect(host ="localhost",user="root",password="",database="recommendationsport")
                cursor = connection.cursor()
                cursor.execute('UPDATE users set username = %s, email = %s, password = %s, location = %s where id = %s', (username, email, password, locationPlace, id,))
                update = cursor.fetchone()
                connection.commit()


                cursor.execute('SELECT * FROM users WHERE id = %s', (id,))
                row = cursor.fetchone()
                session.modified = True
                session['user'] = row[1]
                session['email'] = row[2]
                session['password'] = row[3]
                session['locationUser'] = row[4]
                connection.commit()
                connection.close()
                flash("Your information have been updated successfully!")

                return redirect(url_for("userInfo"))
        else:

            userName = session['user']
            eMail = session['email']
            passWord = session['password']
            locaTion = session['locationUser'] 

            return render_template("editUser.html", username = userName, email = eMail, password = passWord, location = locaTion)
    else:
        return redirect(url_for("login"))

#Displaying sports court available for selected sports centre
@app.route('/sportsCourt', methods=["GET","POST"])
def sportsCourt():
    if "user" in session:

        if request.method =="POST":
            sportName = request.form['sportsCentre']
            court = request.form['court']
            location = request.form['location']
            session.modified = True
            session['sportsCentre'] = sportName
            session['sportCourt'] = court
            session['location'] = location

            return redirect(url_for("sportsCourtProcess"))
        else : 
            return redirect(url_for("sportsCourtProcess"))

    else:
        return redirect(url_for("login"))


@app.route('/sportsCourtProcess', methods=["GET","POST"])
def sportsCourtProcess():
    if "user" in session:

        return render_template("sportsCourt.html")
    else:
        return redirect(url_for("login"))

#Court booking page
@app.route('/courtBooking', methods=["GET","POST"])
def courtBooking():
    if "user" in session:
        if request.method =="POST":
            courtSport = request.form['courtSport']           
            session.modified = True
            session['courtSport'] = courtSport
            return render_template("courtBooking.html")
        else:
            return render_template("courtBooking.html")
    else:
        return redirect(url_for("login"))

#Court booking process
@app.route('/courtBookingProcess', methods=["GET","POST"])
def courtBookingProcess():
    if "user" in session:
        if request.method =="POST":

            #Email format authentication
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

            #Court booking form authentication
            if request.form["fullName"] == '' and request.form["phoneNum"] == '' and request.form["email"] == '':
                flash("Please fill out the form!")   
                return redirect(url_for("courtBookingProcess"))
            elif request.form["fullName"] == '':
                flash("Fullname is empty!")   
                return redirect(url_for("courtBookingProcess"))
            elif request.form["phoneNum"] == '':
                flash("Phone number is empty!")    
                return redirect(url_for("courtBookingProcess"))
            elif request.form["email"] == '':
                flash("Email is empty!")
                return redirect(url_for("courtBookingProcess"))   
            else:
                fullName = request.form['fullName']
                phoneNum = request.form['phoneNum']
                email = request.form['email']

                if(not re.fullmatch(regex, email)):
                    flash("Email is invalid!")
                    return redirect(url_for("courtBookingProcess"))

                session.modified = True
                session['fullName'] = fullName
                session['phoneNum'] = phoneNum

                if session['courtSport'] == "Badminton":
                    return redirect(url_for('courtSelection'))
                elif session['courtSport'] == "Futsal":
                    return redirect(url_for('courtSelectionFutsal'))
                elif session['courtSport'] == "Squash":
                    return redirect(url_for('courtSelectionSquash'))
                elif session['courtSport'] == "Tennis":
                    return redirect(url_for('courtSelectionTennis'))
                elif session['courtSport'] == "Volleyball":
                    return redirect(url_for('courtSelectionVolleyball'))
        else:
            return render_template("courtBooking.html")
    else:
        return redirect(url_for("login"))

#Badminton court selection
@app.route('/courtSelection', methods=["GET","POST"])
def courtSelection():
    if "user" in session:
        if request.method =="POST":           
            return render_template("courtSelection.html")
        else:
            return render_template("courtSelection.html")
    else:
        return redirect(url_for("login"))


#Futsal court selection
@app.route('/courtSelectionFutsal', methods=["GET","POST"])
def courtSelectionFutsal():
    if "user" in session:
        if request.method =="POST":
            return render_template("courtSelectionFutsal.html")
        else:
            return render_template("courtSelectionFutsal.html")
    else:
        return redirect(url_for("login"))


#Squash court selection
@app.route('/courtSelectionSquash', methods=["GET","POST"])
def courtSelectionSquash():
    if "user" in session:
        if request.method =="POST":
            return render_template("courtSelectionSquash.html")
        else:
            return render_template("courtSelectionSquash.html")
    else:
        return redirect(url_for("login"))

#Tennis court selection
@app.route('/courtSelectionTennis', methods=["GET","POST"])
def courtSelectionTennis():
    if "user" in session:
        if request.method =="POST":
            return render_template("courtSelectionTennis.html")
        else:
            return render_template("courtSelectionTennis.html")
    else:
        return redirect(url_for("login"))

#Volleyball court selection
@app.route('/courtSelectionVolleyball', methods=["GET","POST"])
def courtSelectionVolleyball():
    if "user" in session:
        if request.method =="POST":
            return render_template("courtSelectionVolleyball.html")
        else:
            return render_template("courtSelectionVolleyball.html")
    else:
        return redirect(url_for("login"))

#Court selection process
@app.route('/courtSelectionProcess', methods=["GET","POST"])
def courtSelectionProcess():
    
    if "user" in session:
        if request.method =="POST":

            
            #Authenticate court form selection
            if request.form["setTodaysDate"] == '' and request.form['bookTime'] == "Select" and request.form['bookDuration'] == "Select":
                flash("Please fill out all of the form!")   

                if session['courtSport'] == "Badminton":
                    return redirect(url_for('courtSelection'))
                elif session['courtSport'] == "Futsal":
                    return redirect(url_for('courtSelectionFutsal'))
                elif session['courtSport'] == "Squash":
                    return redirect(url_for('courtSelectionSquash'))
                elif session['courtSport'] == "Tennis":
                    return redirect(url_for('courtSelectionTennis'))
                elif session['courtSport'] == "Volleyball":
                    return redirect(url_for('courtSelectionVolleyball'))
                
            elif request.form["setTodaysDate"] == '':
                flash("Please select the date for booking!")  

                if session['courtSport'] == "Badminton":
                    return redirect(url_for('courtSelection'))
                elif session['courtSport'] == "Futsal":
                    return redirect(url_for('courtSelectionFutsal'))
                elif session['courtSport'] == "Squash":
                    return redirect(url_for('courtSelectionSquash'))
                elif session['courtSport'] == "Tennis":
                    return redirect(url_for('courtSelectionTennis'))
                elif session['courtSport'] == "Volleyball":
                    return redirect(url_for('courtSelectionVolleyball'))
                
            elif request.form['bookTime'] == "Select" :
                flash("Please select the time for booking!")   
                
                if session['courtSport'] == "Badminton":
                    return redirect(url_for('courtSelection'))
                elif session['courtSport'] == "Futsal":
                    return redirect(url_for('courtSelectionFutsal'))
                elif session['courtSport'] == "Squash":
                    return redirect(url_for('courtSelectionSquash'))
                elif session['courtSport'] == "Tennis":
                    return redirect(url_for('courtSelectionTennis'))
                elif session['courtSport'] == "Volleyball":
                    return redirect(url_for('courtSelectionVolleyball'))
                
            elif request.form['bookDuration'] == "Select" :
                flash("Please select the duration for booking!")   
                
                if session['courtSport'] == "Badminton":
                    return redirect(url_for('courtSelection'))
                elif session['courtSport'] == "Futsal":
                    return redirect(url_for('courtSelectionFutsal'))
                elif session['courtSport'] == "Squash":
                    return redirect(url_for('courtSelectionSquash'))
                elif session['courtSport'] == "Tennis":
                    return redirect(url_for('courtSelectionTennis'))
                elif session['courtSport'] == "Volleyball":
                    return redirect(url_for('courtSelectionVolleyball'))
                
            elif request.form['sportsTools'] != "None" and request.form['quantityInput'] == "0" :
                flash("The quantity of sports tools is empty. Please try again!")   
                
                if session['courtSport'] == "Badminton":
                    return redirect(url_for('courtSelection'))
                elif session['courtSport'] == "Futsal":
                    return redirect(url_for('courtSelectionFutsal'))
                elif session['courtSport'] == "Squash":
                    return redirect(url_for('courtSelectionSquash'))
                elif session['courtSport'] == "Tennis":
                    return redirect(url_for('courtSelectionTennis'))
                elif session['courtSport'] == "Volleyball":
                    return redirect(url_for('courtSelectionVolleyball'))
            else :
                id = session['id']
                sportName = session['sportsCentre']
                courtSports = session['courtSport']
                courtName = request.form['courtSelect']
                dateBook = request.form['setTodaysDate']
                timeBook = request.form['bookTime']
                durationBook = request.form['bookDuration']
                sportsTools = request.form['sportsTools']
                quantityInput = request.form['quantityInput']
                totalFee = request.form['totalFee']

                #Fetching court booking from database that has exact value with court selection form
                connection = pymysql.connect(host ="localhost",user="root",password="",database="recommendationsport")
                cursor = connection.cursor()
                cursor.execute('Select * from bookingcourt where sportsCentre = %s and sportsCourt = %s and courtName = %s and dateBooking = %s and time = %s', (sportName, courtSports, courtName, dateBook, timeBook,))
                bookCompare = cursor.fetchone()
                connection.commit()

                selectHour = durationBook+":00"
                selectTime = timeBook

                selectHour = datetime.datetime.strptime(selectHour, "%H:%M")
                selectTime = datetime.datetime.strptime(timeBook, "%H:%M")

                #Calculating finish time
                finishTime = selectTime + datetime.timedelta(hours=selectHour.hour, minutes=selectHour.minute)
                
                from datetime import date, timedelta
                current_date = date.today()
                timeNow = datetime.datetime.now()
                current_time = timedelta(hours = timeNow.hour, minutes = timeNow.minute, seconds=timeNow.second)
                min_time = datetime.datetime.min.time()
                result_time = (datetime.datetime.combine(datetime.date.min, min_time) + current_time).time()
                date_obj = datetime.datetime.strptime(dateBook, '%Y-%m-%d').date()
                time_object = datetime.datetime.strptime(timeBook, '%H:%M').time()

                cursor3 = connection.cursor()
                cursor3.execute('Select * from bookingcourt where sportsCentre = %s and sportsCourt = %s and courtName = %s and dateBooking = %s and (%s > time and %s < timeFinish) ', (sportName, courtSports, courtName, dateBook, selectTime, selectTime,))
                bookCompare2 = cursor3.fetchone()
                connection.commit()

                cursor4 = connection.cursor()
                cursor4.execute('Select time from bookingcourt where sportsCentre = %s and sportsCourt = %s and courtName = %s and dateBooking = %s and ( %s < time and %s > time)', (sportName, courtSports, courtName, dateBook, selectTime, finishTime,))
                bookCompare3 = cursor4.fetchone()
                connection.commit()

                #Authenticate booking time
                if current_date == date_obj and result_time > time_object:
                    flash("The time of the booking has already passed. Please select another time!")

                    if session['courtSport'] == "Badminton":
                        return redirect(url_for('courtSelection'))
                    elif session['courtSport'] == "Futsal":
                        return redirect(url_for('courtSelectionFutsal'))
                    elif session['courtSport'] == "Squash":
                        return redirect(url_for('courtSelectionSquash'))
                    elif session['courtSport'] == "Tennis":
                        return redirect(url_for('courtSelectionTennis'))
                    elif session['courtSport'] == "Volleyball":
                        return redirect(url_for('courtSelectionVolleyball'))
                #Authenticate booking time if exceed business hour 
                if (timeBook == "22:00" and durationBook == "5") or (timeBook == "23:00" and durationBook == "5") or (timeBook == "23:00" and durationBook == "4") or (timeBook == "00:00" and durationBook == "5") or (timeBook == "00:00" and durationBook == "4") or (timeBook == "00:00" and durationBook == "3") :
                    flash("The duration of booking is exceed the time of business hour at 2 AM. Please try again!")

                    if session['courtSport'] == "Badminton":
                        return redirect(url_for('courtSelection'))
                    elif session['courtSport'] == "Futsal":
                        return redirect(url_for('courtSelectionFutsal'))
                    elif session['courtSport'] == "Squash":
                        return redirect(url_for('courtSelectionSquash'))
                    elif session['courtSport'] == "Tennis":
                        return redirect(url_for('courtSelectionTennis'))
                    elif session['courtSport'] == "Volleyball":
                        return redirect(url_for('courtSelectionVolleyball'))
                #Authenticate booking time if it already has been reserved
                if bookCompare:
                    flash("The selected booking slot for this sports centre has already been reserved. Please try again!")

                    if session['courtSport'] == "Badminton":
                        return redirect(url_for('courtSelection'))
                    elif session['courtSport'] == "Futsal":
                        return redirect(url_for('courtSelectionFutsal'))
                    elif session['courtSport'] == "Squash":
                        return redirect(url_for('courtSelectionSquash'))
                    elif session['courtSport'] == "Tennis":
                        return redirect(url_for('courtSelectionTennis'))
                    elif session['courtSport'] == "Volleyball":
                        return redirect(url_for('courtSelectionVolleyball'))
                    
                elif bookCompare2:
                    flash("The selected booking time slot for this sports centre has already been reserved. Please try again!")

                    if session['courtSport'] == "Badminton":
                        return redirect(url_for('courtSelection'))
                    elif session['courtSport'] == "Futsal":
                        return redirect(url_for('courtSelectionFutsal'))
                    elif session['courtSport'] == "Squash":
                        return redirect(url_for('courtSelectionSquash'))
                    elif session['courtSport'] == "Tennis":
                        return redirect(url_for('courtSelectionTennis'))
                    elif session['courtSport'] == "Volleyball":
                        return redirect(url_for('courtSelectionVolleyball'))
                elif bookCompare3:

                    flash("The booking duration has been exceed for next reservation slot. Please try again!")
                    
                    if session['courtSport'] == "Badminton":
                        return redirect(url_for('courtSelection'))
                    elif session['courtSport'] == "Futsal":
                        return redirect(url_for('courtSelectionFutsal'))
                    elif session['courtSport'] == "Squash":
                        return redirect(url_for('courtSelectionSquash'))
                    elif session['courtSport'] == "Tennis":
                        return redirect(url_for('courtSelectionTennis'))
                    elif session['courtSport'] == "Volleyball":
                        return redirect(url_for('courtSelectionVolleyball'))
                elif not bookCompare : 

                    session.modified = True
                    session['dateBook'] = dateBook
                    session['timeBook'] = timeBook
                    session['timeFinish'] = finishTime
                    session['durationBook'] = durationBook
                    session['courtName'] = courtName
                    session['sportsTools'] = sportsTools
                    session['quantityInput'] = quantityInput
                    session['totalFee'] = totalFee

                    return redirect(url_for("payment"))

                connection.close()
        else:
            return redirect(url_for("courtSelection"))
    else:
        return redirect(url_for("login"))

@app.route('/payment', methods=["GET","POST"])
def payment():
    if "user" in session:
        if request.method =="POST":
            #Payment authentication
            if request.form["paymentMethod"] == "Select" :
                flash("Please select the payment method!")   
                return redirect(url_for("payment"))
            elif request.form["paymentMethod"] == "DebitCard" :
                if request.form["firstName"] == '' and request.form['lastName'] == '' and request.form['debitNumber'] == ''  and request.form['securityCode'] == ''  and request.form['cardExpire'] == '':
                    flash("Please fill out all of the form!")  
                    return redirect(url_for("payment")) 
                elif request.form["firstName"] == '' : 
                    flash("First Name is empty!")  
                    return redirect(url_for("payment"))
                elif request.form["lastName"] == '' : 
                    flash("Last Name is empty!")  
                    return redirect(url_for("payment"))
                elif request.form["debitNumber"] == '' : 
                    flash("Debit Card is empty!")  
                    return redirect(url_for("payment"))
                elif request.form["securityCode"] == '' : 
                    flash("Security Code is empty!")  
                    return redirect(url_for("payment"))
                elif request.form["cardExpire"] == '' : 
                    flash("Card Expiration is empty!")  
                    return redirect(url_for("payment"))
                else :

                    card_number = request.form.get('debitNumber')
                    pattern = re.compile(r'^\d{4} \d{4} \d{4} \d{4}$')

                    if " " in request.form["firstName"]:
                        flash("First Name cannot have extra space! Please try again.")  
                        return redirect(url_for("payment")) 
                    elif " " in request.form["lastName"]:
                        flash("Last Name cannot have extra space! Please try again.")  
                        return redirect(url_for("payment"))
                    elif not pattern.match(card_number):
                        flash("Card Number format is mismatch! Please try again.")
                        return redirect(url_for("payment"))
                    else :

                        id = session['id']
                        sportName = session['sportsCentre']
                        location = session['location']
                        courtSports = session['courtSport']
                        courtName = session['courtName']
                        dateBook = session['dateBook']
                        timeBook = session['timeBook']
                        finishTime = session['timeFinish']
                        durationBook = session['durationBook']
                        totalFee = session['totalFee']
                        custName = session['fullName'] 
                        phoneNum = session['phoneNum'] 

                        connection = pymysql.connect(host ="localhost",user="root",password="",database="recommendationsport")
                        cursor2 = connection.cursor()
                        cursor2.execute('Select * from bookingcourt where sportsCentre = %s and sportsCourt = %s and courtName = %s and dateBooking = %s and time = %s', (sportName, courtSports, courtName, dateBook, timeBook,))
                        bookCompare = cursor2.fetchone()
                        connection.commit()

                        if bookCompare:
                            flash("You have already make payment for this booking slot. Thank you!")
                            return redirect(url_for("paymentReceipt"))
                        else:     

                            cursor3 = connection.cursor()
                            cursor3.execute('SELECT rating FROM bookingcourt where user_id = %s and sportsCentre = %s ', (id, sportName,))
                            ratingTest = cursor3.fetchone()

                            if ratingTest :
                                rating = ratingTest
                            else :
                                rating = 0

                            #Insert booking court information into database
                            cursor = connection.cursor()
                            cursor.execute('INSERT INTO bookingcourt VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (id, sportName, location, courtSports, courtName, dateBook, timeBook, finishTime, durationBook, totalFee, rating, custName, phoneNum,))
                            connection.commit()
                            connection.close()
                            return redirect(url_for("paymentReceipt"))


            elif request.form["paymentMethod"] == "OnlineBanking" :
                if request.form["onlineBank"] == "Select" and request.form['username'] == '' and request.form['password'] == '' :
                    flash("Please fill out all of the form!")  
                    return redirect(url_for("payment")) 
                elif request.form["onlineBank"] == "Select" : 
                    flash("Please select your online banking!")  
                    return redirect(url_for("payment"))    
                elif request.form["username"] == '' and request.form["password"] == '' : 
                    flash("Username and password is empty!")  
                    return redirect(url_for("payment"))
                elif request.form["username"] == '' : 
                    flash("Username is empty!")  
                    return redirect(url_for("payment"))
                elif request.form["password"] == '' : 
                    flash("Password is empty!")  
                    return redirect(url_for("payment"))
                else :

                        id = session['id']
                        sportName = session['sportsCentre']
                        location = session['location']
                        courtSports = session['courtSport']
                        courtName = session['courtName']
                        dateBook = session['dateBook']
                        timeBook = session['timeBook']
                        finishTime = session['timeFinish']
                        durationBook = session['durationBook']
                        totalFee = session['totalFee']
                        custName = session['fullName'] 
                        phoneNum = session['phoneNum'] 

                        connection = pymysql.connect(host ="localhost",user="root",password="",database="recommendationsport")
                        cursor2 = connection.cursor()
                        cursor2.execute('Select * from bookingcourt where sportsCentre = %s and sportsCourt = %s and courtName = %s and dateBooking = %s and time = %s', (sportName, courtSports, courtName, dateBook, timeBook,))
                        bookCompare = cursor2.fetchone()
                        connection.commit()
                        
                        if bookCompare:
                            flash("You have already make payment for this booking slot. Thank you!")
                            return redirect(url_for("paymentReceipt"))
                        else:     
                            
                            cursor3 = connection.cursor()
                            cursor3.execute('SELECT rating FROM bookingcourt where user_id = %s and sportsCentre = %s ', (id, sportName,))
                            ratingTest = cursor3.fetchone()

                            if ratingTest :
                                rating = ratingTest
                            else :
                                rating = 0

                            cursor = connection.cursor()
                            cursor.execute('INSERT INTO bookingcourt VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (id, sportName, location, courtSports, courtName, dateBook, timeBook, finishTime, durationBook, totalFee, rating,custName,phoneNum,))
                            connection.commit()
                            connection.close()
                            return redirect(url_for("paymentReceipt"))
        else:
            return render_template("payment.html")
    else:
        return redirect(url_for("login"))

#Payment receipt page
@app.route('/paymentReceipt')
def paymentReceipt():
    if "user" in session:
        return render_template("paymentReceipt.html")
    else:
        return redirect(url_for("login"))

#Login page for staff of sports centre
@app.route('/loginStaff', methods=["POST", "GET"])
def loginStaff():
    msg = ''

    if request.method =="POST":

        if request.form["sportCentreHandling"] == '' and request.form["password"] == '':
            msg = 'Sports centre name and password is empty!'    
            return render_template("loginStaff.html", message = msg)
        elif request.form["sportCentreHandling"] == '':
            msg = 'Sports centre name is empty!'    
            return render_template("loginStaff.html", message = msg)
        elif request.form["password"] == '':
            msg = 'Password is empty!'    
            return render_template("loginStaff.html", message = msg)
        elif request.method =="POST" and 'sportCentreHandling' in request.form and 'password' in request.form:
    

            staffSportsCentre = request.form["sportCentreHandling"]
            password = request.form["password"] 

            connection = pymysql.connect(host ="localhost",user="root",password="",database="recommendationsport")
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM staff WHERE sportsCentre = %s AND password = %s', (staffSportsCentre, password,))
            accountStaff = cursor.fetchone()
            connection.commit()

            if accountStaff:
                session.modified = True
                session['loggedin'] = True
                session["staff"] = staffSportsCentre 
                session['staffId'] = accountStaff[0]

                return redirect(url_for("homeStaff"))
            else:
                msg = 'Incorrect Sports centre name or password!'
                return render_template("loginStaff.html", message = msg)
    else: 
        return render_template("loginStaff.html", message = msg)

#Home page for sports centre staff
@app.route('/homeStaff')
def homeStaff():
    if "staff" in session:

        staffSportsCentre = session['staff']

        connection = pymysql.connect(host ="localhost",user="root",password="",database="recommendationsport")
        cursor = connection.cursor()
        cursor.execute('SELECT * from bookingcourt where sportsCentre = %s', (staffSportsCentre,))
        viewBooking = cursor.fetchall()
        connection.commit()
        connection.close()

        return render_template("homePageStaff.html", viewBooking = viewBooking) 
    else:
        return redirect(url_for("loginStaff"))

#Print transaction process
@app.route('/printTransaction', methods=["POST", "GET"])
def printTransaction():
    if "staff" in session:

        if request.method == 'POST':

            orderid = request.form['orderId']

            connection = pymysql.connect(host ="localhost",user="root",password="",database="recommendationsport")

            cursor = connection.cursor()
            cursor.execute('SELECT * from bookingcourt where order_id = %s', (orderid,))
            transactionOrder = cursor.fetchone()
            connection.commit()
            connection.close()

            return render_template("printTransaction.html", transactionOrder = transactionOrder)
            
        else:
            return redirect(url_for("homeStaff"))

#User logout
@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))

#Staff logout
@app.route('/logoutStaff')
def logoutStaff():
    session.pop("staffId", None)
    return redirect(url_for("loginStaff"))


if __name__=='__main__':
        app.run(port = 5002, debug = True)