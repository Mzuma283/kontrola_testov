from __future__ import print_function
import cv2 as cv
import pypdfium2 as pdfium
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import pandas as pd
from tkinter import Tk
from hladanie_chyb import control
PY3 = sys.version_info[0] == 3

if PY3:
    xrange = range

from tkinter.filedialog import askdirectory
from tkinter import filedialog as fd

path = askdirectory(title='Select your folder')
print('Path: ' + path)

entries = os.listdir(path)
print(entries)
correct = fd.askopenfilename(title='Select correct test')
print('Correct test: ' + correct)
exists = os.path.exists(path)
print(exists)
exists2 = os.path.exists(correct)
print(exists2)
path_str = str(path)
for i in entries:
    test = path.format(i)
    print(test)
    result = control(test, correct, path)
    print('Number of mistakes: {}'.format(result))