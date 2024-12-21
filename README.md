# kujira

A python package that allows you to debug machine learning programs in real time. 

## Core Concept

Kujira allows you to "plug" your live and editable model analysis code within the training loop. 

```python
tracker = kujira.init(analytics_file=path)
for i, data in enumerate(dataset):
  output = model(data)
  tracker(output)
  #this links the "output" to the program in the analytics file that you passed
  #the program within tracker, which is in another file, is live editable

```
