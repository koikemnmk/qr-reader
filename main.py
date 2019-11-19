from flask import Flask, Response
from pyzbar import pyzbar
from picamera.array import PiRGBArray
datetime import datetime

import numpy as np
import cv2
import time

camera = PiCamera()
