# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 11:26:17 2018

@author: 1804002
"""






import tensorflow as tf
import numpy as np



## Crate Data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3


#### Creat tensorflow structure start ######
Weights = tf.Variable(tf.random_uniform([1] , -1.0 , 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()
#### Creat tensorflow structure start ######

sess = tf.Session()
sess.run(init)                        ##### Very important

for step in range(0,201):
     sess.run(train)
     if step % 20 == 00:
          print(step,sess.run(Weights),sess.run(biases))












