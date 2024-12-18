import kujira
import time
import numpy as np

run = kujira.init(job_type=None, project=None, analytics_file="/Users/abitpalgyawali/Documents/projects/kujira/demo/analytics1.py")


for i in range(100):
    xs = np.linspace(0, 10)
    run(xs)
    time.sleep(1)