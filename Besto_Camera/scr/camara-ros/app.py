import rospy
import cv2
from threading import Thread, Event
from flask import *
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage

frame = None
bridge = CvBridge()
event = Event()

def on_image(data):
    global frame
    cv_image = bridge.compressed_imgmsg_to_cv2(data, "passthrough")
    frame = cv2.imencode(".jpg",cv_image)[1].tobytes()
    event.set()

Thread(target=lambda: rospy.init_node('cam_listener', disable_signals=True)).start()
rospy.Subscriber("/phone1/camera/image/compressed", CompressedImage, on_image)

app = Flask(__name__)

def get_frame():
    event.wait()
    event.clear()
    return frame

@app.route('/')
def camara():
    return render_template('camara.html')

def gen():
    while True:
        frame = get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='192.168.0.7', port=5000 ,debug=True)
