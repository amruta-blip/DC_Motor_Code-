import RPi.GPIO as GPIO  # needed to use IO Pins on the Raspberry Pi
import time  # to use the sleep function
from tkinter import *  # just to create a temporary UI
from tkinter import ttk
import threading  # needed to run direction loop and GUI runnning simultaneously

from flask import (
    Blueprint, render_template, Response
)

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html',
                           title='UV Disinfectant Bot')


direction = 'stop'


@bp.route('/forward')
def forward():
    direction = 'forward'
    return Response({
        direction
    }, 200)


@bp.route('/backward')
def backward():
    direction = 'backward'
    return Response(direction, 200)


@bp.route('/left')
def left():
    direction = 'left'
    return Response(direction, 200)


@bp.route('/right')
def right():
    direction = 'right'
    return Response(direction, 200)


@bp.route('/stop')
def stop():
    direction = 'stop'
    return Response(direction, 200)


# current direction
direction = 'stop'

# Pin configuration
right_motor = (7, 8)  # rotates clockwise to move forward
left_motor = (10, 12)  # rotates anit-clockwise to move forward

# array of controls
arr = [[GPIO.HIGH, GPIO.LOW],
       [GPIO.LOW, GPIO.HIGH]]

# stopped state
stop = [GPIO.LOW, GPIO.LOW]

# setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(right_motor, GPIO.OUT)
GPIO.setup(left_motor, GPIO.OUT)


def rotate_clockwise(motor):
    
        GPIO.output(motor, arr[0])
        


def rotate_anticlockwise(motor):
    
        GPIO.output(motor, arr[1])
        


# To keep the motors running
def direction_loop():
    global direction
    while True:
        if direction == 'forward':
            rotate_clockwise(right_motor)
            rotate_anticlockwise(left_motor)
            print('moving forward')
        elif direction == 'left':
            rotate_anticlockwise(right_motor)
            rotate_anticlockwise(left_motor)
            print('turning left')
        elif direction == 'backward':
            rotate_anticlockwise(right_motor)
            rotate_clockwise(left_motor)
            print('moving backward')
        elif direction == 'right':
            rotate_clockwise(right_motor)
            rotate_clockwise(left_motor)
            print('turning right')
        elif direction == 'stop':
            GPIO.output(right_motor, stop)
            GPIO.output(left_motor, stop)
            print('stopped')
            continue
        else:
            continue
