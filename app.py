from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL



app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'diem_thi_ptnk'

mysql = MySQL(app)



@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT *,(`final_1`.`Toan`*2+`final_1`.`Toan_KC`+`final_1`.`Van_KC`+`final_1`.`Anh_KC`) as tong_diem FROM `final_1` Where `final_1`.`Toan` !='V' and `final_1`.`Toan` !='N/A' ORDER BY (`final_1`.`Toan`*2+`final_1`.`Toan_KC`+`final_1`.`Van_KC`+`final_1`.`Anh_KC`) DESC Limit 35")
    data = cur.fetchall()
    cur.close()
    return render_template('pages/dochuyentoan.html', data=data)
@app.route('/chuyenli')
def chuyenli():
    cur = mysql.connection.cursor()
    cur.execute("SELECT *,(`final_1`.`Ly`*2+`final_1`.`Toan_KC`+`final_1`.`Van_KC`+`final_1`.`Anh_KC`) as tong_diem FROM `final_1` Where `final_1`.`Ly` !='V' and `final_1`.`Ly` !='N/A' ORDER BY (`final_1`.`Ly`*2+`final_1`.`Toan_KC`+`final_1`.`Van_KC`+`final_1`.`Anh_KC`) DESC Limit 35")
    data = cur.fetchall()
    cur.close()
    return render_template('pages/dochuyenli.html', data=data)

@app.route('/chuyenhoa')
def chuyenhoa():
    cur = mysql.connection.cursor()
    cur.execute("SELECT *,(`final_1`.`Hoa`*2+`final_1`.`Toan_KC`+`final_1`.`Van_KC`+`final_1`.`Anh_KC`) as tong_diem FROM `final_1` Where `final_1`.`Hoa` !='V' and `final_1`.`Hoa` !='N/A' ORDER BY (`final_1`.`Hoa`*2+`final_1`.`Toan_KC`+`final_1`.`Van_KC`+`final_1`.`Anh_KC`) DESC Limit 35")
    data = cur.fetchall()
    cur.close()
    return render_template('pages/dochuyenhoa.html', data=data)

@app.route('/chuyentin')
def chuyentin():
    cur = mysql.connection.cursor()
    cur.execute("SELECT *,(`final_1`.`Tin`*2+`final_1`.`Toan_KC`+`final_1`.`Van_KC`+`final_1`.`Anh_KC`) as tong_diem FROM `final_1` Where `final_1`.`Tin` !='V' and `final_1`.`Tin` !='N/A' ORDER BY (`final_1`.`Tin`*2+`final_1`.`Toan_KC`+`final_1`.`Van_KC`+`final_1`.`Anh_KC`) DESC Limit 35")
    data = cur.fetchall()
    cur.close()
    return render_template('pages/dochuyentin.html', data=data)

@app.route('/chuyenvan')
def chuyenvan():
    cur = mysql.connection.cursor()
    cur.execute("SELECT *,(`final_1`.`Van`*2+`final_1`.`Toan_KC`+`final_1`.`Van_KC`+`final_1`.`Anh_KC`) as tong_diem FROM `final_1` Where `final_1`.`Van` !='V' and `final_1`.`Van` !='N/A' ORDER BY (`final_1`.`Van`*2+`final_1`.`Toan_KC`+`final_1`.`Van_KC`+`final_1`.`Anh_KC`) DESC Limit 70")
    data = cur.fetchall()
    cur.close()
    return render_template('pages/dochuyenvan.html', data=data)

@app.route('/chuyensinh')
def chuyensinh():
    cur = mysql.connection.cursor()
    cur.execute("SELECT *,(`final_1`.`Sinh`*2+`final_1`.`Toan_KC`+`final_1`.`Van_KC`+`final_1`.`Anh_KC`) as tong_diem FROM `final_1` Where `final_1`.`Sinh` !='V' and `final_1`.`Sinh` !='N/A' ORDER BY (`final_1`.`Sinh`*2+`final_1`.`Toan_KC`+`final_1`.`Van_KC`+`final_1`.`Anh_KC`) DESC Limit 35")
    data = cur.fetchall()
    cur.close()
    return render_template('pages/dochuyensinh.html', data=data)
@app.route('/chuyenanh')
def chuyenanh():
    cur = mysql.connection.cursor()
    cur.execute("SELECT *,(`final_1`.`Anh`*2+`final_1`.`Toan_KC`+`final_1`.`Van_KC`+`final_1`.`Anh_KC`) as tong_diem FROM `final_1` Where `final_1`.`Anh` !='V' and `final_1`.`Anh` !='N/A' ORDER BY (`final_1`.`Anh`*2+`final_1`.`Toan_KC`+`final_1`.`Van_KC`+`final_1`.`Anh_KC`) DESC Limit 35")
    data = cur.fetchall()
    cur.close()
    return render_template('pages/dochuyenanh.html', data=data)
