from flask_socketio import emit, join_room, leave_room
from app import socketio

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    emit('response', {'data': message}, broadcast=True)

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    emit('response', {'data': f'{username} has entered the room.'}, room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    emit('response', {'data': f'{username} has left the room.'}, room=room)
