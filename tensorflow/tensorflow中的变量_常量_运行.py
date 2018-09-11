import tensorflow as tf

W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)


sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)



print sess.run(W)

print sess.run(b)





