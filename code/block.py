class block():
    def __init__(self, N, normalCell, input1, input2):
        self.N = N
        self.normalCell = normalCell
        self.input1 = input1
        self.input2 = input2

    def setInput1(self,input):
        self.input1 = input
    def setInput2(self,input):
        self.input2 = input
    def setN(self,N):
        self.N = N
    def setNormalCell(self,normalCell):
        self.normalCell = normalCell

    def getOutput(self):
        cellSet = []
        tmp1 = 1
        while (1):
            cellSet.append(self.normalCell)
            if tmp1 == self.N :
                break
            tmp1 += 1
        tmp2 = 0
        output = []
        for cell in cellSet:
            if tmp2 == 0:
                cell.setInput(self.input1, self.input2)
                output.append(cell.getOutput())
            elif tmp2 == 1:
                cell.setInput(self.input2, output[tmp2 - 1])
                output.append(cell.getOutput())
            else :
                cell.setInput(output[tmp2 - 2], output[tmp2 - 1])
                output.append(cell.getOutput())
        return output[len(output) - 2], output[len(output) - 1]





