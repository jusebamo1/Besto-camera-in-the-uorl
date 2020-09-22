from flask import *
import sqlite3
from threading import *
import ros, rospy
import netifaces as ni
from geometry_msgs.msg import Twist

db = 'database.db'
app = Flask(__name__)
app.secret_key = "ros"
data = ros.RosSensors()

def Query(query):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        data = cursor.execute(query)
        conn.commit()
    return data

@app.route('/')
def index():
    if "logged" in session:
        return render_template('indexl.html')
    else:
        return render_template('index.html')

@app.route('/camara')
def camara():
    return redirect(url_for('camara'))

@app.route('/auth', methods=['POST'])
def Auth():
    if request.method == 'POST':
        user = request.form['user']
        passw = request.form['pass']
        query = 'SELECT * FROM authorization WHERE username = "{}";'.format(user)
        data = Query(query)
        if data:
            for acc in data:
                if passw == acc[2]:
                    session['account'] = acc[1]
                    session['logged'] = 1
                    return redirect(url_for('index'))
                else:
                    flash ("Wrong password")
                    return redirect(url_for('index'))
        else:
            pass
        flash("Wrong user")
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('account')
    session.pop('logged')
    return redirect(url_for('index'))

@app.route('/commands', methods=['POST'])
def commands():
    try:
        linearVel = float(request.form["linearVel"])
        angularVel = float(request.form["angularVel"])
    except:
        pass
    if request.form["command"] == "w":
        data.Publish(linearVel, 0)
    elif request.form["command"] == "a":
        data.Publish(0, -angularVel)
    elif request.form["command"] == "s":
        data.Publish(-linearVel, 0)
    elif request.form["command"] == "d":
        data.Publish(0, angularVel)
    elif request.form["command"] == "stop":
        data.Publish(0, 0)
    else:
        pass
    return "None"

def get_frame():
    data.event.wait()
    data.event.clear()
    return data.frame

def gen():
    while True:
        frame = data.frame
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/data', methods=['GET'])
def printData():
    return (jsonify( illu_data =  data.illu_data, imu_ox =  data.imu_data_ox, imu_oy =  data.imu_data_oy, imu_oz =  data.imu_data_oz, imu_vax =  data.imu_data_avx, imu_vay =  data.imu_data_avy, imu_vaz =  data.imu_data_avz, imu_lax =  data.imu_data_lax, imu_lay =  data.imu_data_lay, imu_laz =  data.imu_data_laz, mfx =  data.mfx, mfy =  data.mfy, mfz =  data.mfz ))

if __name__ == '__main__':
    ip_page = ni.ifaddresses('wlp2s0')[ni.AF_INET][0]['addr']
    app.run(host='192.168.0.7', debug = True)
