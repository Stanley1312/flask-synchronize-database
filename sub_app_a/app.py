from flask_app import app, sio

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=5002)
    sio.connect('http://localhost:5000')
    sio.emit('my_message', {'foo': 'bar'})
    sio.wait()
