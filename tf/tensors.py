import tensorflow as tf

# @nikhilrp - 2015-07-04
# The following code is written to understand TensorFlow in detail
# Please do not use it for any meaningful reasons

a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
add = tf.add(a, b)
multiply = tf.multiply(a, b)
mat_a = tf.constant([[3., 3.]])
mat_b = tf.constant([[2.], [3.]])
mat_mul = tf.matmul(mat_a, mat_b)

sess = tf.InteractiveSession()
print("Addition: %i" % sess.run(add, feed_dict={a: 2, b: 3}))
print("Multiplication: %i" % sess.run(multiply, feed_dict={a: 2, b: 3}))
print(mat_a.eval())
sess.close()
