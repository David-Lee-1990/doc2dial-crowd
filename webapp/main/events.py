import datetime

from flask import session
from flask_socketio import emit, join_room, leave_room

from .. import socketio
from .const import *
from .data import get_crowd_data_db, insert_crowd_info, get_chatdata


def get_message(role, text):
    if role == AGENT:
        return '<div><b class="blue-text">{0}: </b>{1}</div>'.format(role, text)
    else:
        return "<div<b>{0}: </b>{1}</div>".format(role, text)


@socketio.on('disconnect', namespace='/chat')
def on_disconnect():
    print("@@@ Client disconnected", str(datetime.datetime.utcnow()))


@socketio.on('connect', namespace='/chat')
def on_connect():
    print("@@@ Client connected", str(datetime.datetime.utcnow()))


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    task_id = session.get(TASK_ID)
    role = session.get(ROLE)
    username = session.get(USERNAME)
    print('##join', role, username, task_id)
    insert_crowd_info(session)
    session[TURN] = 0
    join_room(task_id)
    history = get_chatdata(session)
    if history:
        # session[TURN] = history[-1][TURN]
        for ele in history:
            emit('status', {MSG: get_message(ele[ROLE], ele[MSG]),
                            ROLE: ele[ROLE], MODE:'human'}, room=session[TASK_ID])
        emit('left', {})


@socketio.on('text', namespace='/chat')
def text(message):
    role = session.get(ROLE)
    mode = session.get(MODE)
    msg = message[MSG].strip()
    if msg:
        session[TURN] = session.get(TURN) + 1
        emit('message', {MSG: get_message(role, msg), ROLE: role, MODE: mode},
             room=session.get(TASK_ID))


@socketio.on('left', namespace='/chat')
def left(message):
    task_id = session.get(TASK_ID)
    leave_room(task_id)
    insert_crowd_info(session)
