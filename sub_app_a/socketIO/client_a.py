import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('connected to server')


@sio.event
def disconnect():
    print('disconnected from server')

@sio.event
def my_response(data):
    print('message received with ', data)


if __name__ == '__main__':
    sio.connect('http://localhost:5000')

    sio.emit('my_message', {'foo': 'bar'})
    sio.wait()
