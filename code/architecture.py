from keras.models import Model
from reductionCell import reductionCell
from block import block
import keras
from keras.layers import Conv2D, Activation


class architecture():
    def __init__(self, block, input, reductionCell):
        self.block = block
        self.input = input
        self.reductionCell = reductionCell

    def getOutput(self):
        x = Conv2D(kernel_size = (3, 3))(self.input)
        self.block.setInput1(self.input)
        self.block.setInput2(x)
        y, z = self.block.getOutput()
        self.reductionCell.setInput1(y)
        self.reductionCell.setInput2(z)
        self.block.setInput1(z)
        self.block.setInput2(self.reductionCell.getOutput())
        m, n = self.block.getOutput()
        self.reductionCell.setInput1(m)
        self.reductionCell.setInput2(n)
        self.block.setInput1(n)
        self.block.setInput2(self.reductionCell.getOutput())
        a, b = self.block.getOutput()
        finalOutput = keras.activations.sofmax(b)

        return  finalOutput

