import kujira
import time
import numpy as np

path = "analytics.py"
run = kujira.init(analytics_file=path)

#simple demo -- feel free to mess around
while True:
    xs = np.linspace(0, 10)
    run(xs)
    time.sleep(1)