

import mxnet as mx


x = mx.nd.array([1,2,3,4])
x.attach_grad()
with mx.autograd.record():
    y = x * x + 1
    y=y.backward()
    print(x.grad)