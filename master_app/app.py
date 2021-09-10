from flask_app import app
import eventlet

if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=True)
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)