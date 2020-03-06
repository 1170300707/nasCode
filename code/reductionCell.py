from keras.models import Model
from keras.layers import Conv2D, MaxPool2D, Concatenate


class reductionCell():
    def __init__(self,input1,input2):
        self.input1 = input1
        self.input2 = input2

    def setInput1(self,input):
        self.input1 = input
    def setInput2(self,input):
        self.input2 = input

    def getOutput(self):
        x = Conv2D(kernel_size = (1, 3), strides = (1, 2))(self.input1)
        x = Conv2D(kernel_size = (3, 1), strides = (2, 1))(x)
        x = Conv2D(kernel_size = (1, 1))(x)

        y = Conv2D(kernel_size=(1, 3), strides=(1, 2))(self.input2)
        y = Conv2D(kernel_size=(3, 1), strides=(2, 1))(y)
        y = Conv2D(kernel_size=(1, 1))(y)

        m = MaxPool2D(pool_size = (3, 3))(self.input1)

        n = MaxPool2D(pool_size = (3, 3))(self.input2)

        output = Concatenate([x, y, m, n])

        return output



