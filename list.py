from __future__ import print_function
import cv2 as cv
import pypdfium2 as pdfium
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import pandas as pd
from kontrola_ai import control
PY3 = sys.version_info[0] == 3

if PY3:
    xrange = range


entries = os.listdir('fotky/')
print(entries)
for i in entries:
    test = 'fotky/{}'.format(i)
    print(test)
    result = control(test)
    print('Number of mistakes: {}'.format(result))
