from flask import Flask, render_template, request 
import sqlite3 as sql 
app = Flask(__name__)

import sqlite3

conn = sqlite3.connect('Quiz0Db.db')

# print("Opened database successfully")

# conn.execute('CREATE TABLE vehicle (Vname VARCHAR, RNum VARCHAR, VPics VARCHAR)')
# print("Table created successfully")


# Save (commit) the changes
conn.execute("INSERT INTO vehicle VALUES ('Tesla','104','Nora.jpg')")
conn.commit()
conn.close()

@app.route('/')
def home():
   return render_template('home.html')

 
@app.route('/vehicleName', methods=['POST'])
def vehicleName():
    vehicleName= request.form['vehicleName'] 
    con = sql.connect("Quiz0Db.db") 
    con.row_factory = sql.Row
    cur = con.cursor()
    # print(vehicleName)
    cur.execute('SELECT * FROM vehicle where Vname like \'%'+vehicleName+'%\';') 
    rows = cur.fetchall() 
    # return vehicleName
    return render_template('list.html', rows=rows)

@app.route('/deleteVehicle', methods=['POST'])
def deleteVehicle():
    deleteVehicle= request.form['deleteVehicle'] 
    con = sql.connect("Quiz0Db.db") 
    con.row_factory = sql.Row
    cur = con.cursor()
    # print(vehicleName)
    # cur.execute('DELETE FROM vehicle where Vname like \'%'+deleteVehicle+'%\';')
    cur.execute('DELETE FROM vehicle where Vname=?',(deleteVehicle,))
    con.commit()

    msg="Record successfully deleted" 
     # return vehicleName
    return render_template('list.html',msg=msg)

@app.route('/editVehicle', methods=['POST'])
def editVehicle():
    editVehicle= request.form['editVehicle'] 
    con = sql.connect("Quiz0Db.db") 
    con.row_factory = sql.Row
    cur = con.cursor()
    # print(vehicleName)
    # cur.execute('DELETE FROM vehicle where Vname like \'%'+deleteVehicle+'%\';')
    cur.execute('UPDATE vehicle set Vname = ? where Rnum=?',("honda",editVehicle,))
    con.commit()

    msg="Record successfully deleted" 
     # return vehicleName
    return render_template('list.html',msg=msg)






if __name__ == '__main__': 
 app.run(debug = True)

    # con = sql.connect("Quiz0Db.db")               
    # con.row_factory = sql.rows                
    # cur = con.cursor()                
    # # param = request.form.get('ingridient')
 #    # print(request.form.get('ingridient'))               
 #    # cursor.execute('SELECT * FROM Vehicles where Vname like \'%'+vehicleName+'%\';')                
 #    rows = cursor.fetchall()              
 #    print ("Count is " + str(result))             
 #    return render_template('vehicleName.html', rows=rows)

    # if __name__ == '__main__':
    # app.run(debug = True)

