class Node():
    def __init__(self, seqnum, value):
        self.seqnum = seqnum
        self.value = value
    def getSeqnum(self):
        return self.seqnum
    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value


class Edge():
    def __init__(self, begin, end, weight, F, T):
        self.begin = begin
        self.end = end
        self.weight = weight
        self.F = F
        self.T = T

    def setBegin(self, begin):
        self.begin = begin
    def setEnd(self, end):
        self.end = end
    def setWeight(self, weight):
        self.weight = weight
    def setT(self, T):
        self.T = T

    def getBegin(self):
        return self.begin
    def getEnd(self):
        return self.end
    def getWeight(self):
        return self.weight
    def getF(self):
        return self.F
    def getT(self):
        return self.T

class cell():
    def __init__(self, nodeSet, edgeSet):
        self.nodeSet = nodeSet
        self.edgeSet = edgeSet

    def addVertex(self, node):
        if node not in self.nodeSet:
            self.nodeSet.add(node)
            return True
        return False

    def addEdge(self, edge):
        if edge.weight < 0 :
            return
        for eg in self.edgeSet:
            if eg.begin == edge.begin and eg.begin == edge.begin:
                eg.setWeight(edge.weight)
                eg.setT(edge.T)
                return True
        self.edgeSet.add(edge)
        return True

    def removeEdge(self, begin, end):
        for edge in self.edgeSet:
            if edge.begin == begin and edge.end == end:
                self.edgeSet.remove(edge)
                return True
        return False

    def getbegin(self, end):
        beginS = set()
        for edge in self.edgeSet:
            if edge.end == end:
                beginS.add(edge.begin)
        return beginS

    def getend(self, begin):
        endS = set()
        for edge in self.edgeSet:
            if edge.begin == begin:
                endS.add(edge.begin)
        return endS

    def getNodeSet(self):
        return self.nodeSet
    def getEdgeSet(self):
        return self.edgeSet

    def setInput(self, input1, input2):
        for node in self.nodeSet:
            if node.getSeqnum() == 1:
                node.setValue(input1)
            elif node.getSeqnum() == 2:
                node.setValue(input2)
            else:
                continue

    def getOutput(self):
        for node in self.nodeSet:
            if node.getSeqnum() == 7:
                return node.getValue()


    def toString(self):
        print('node:')
        for node in self.nodeSet:
            print(str(node.seqnum) + str(node.value))
        print('-------------------------------')
        print('edge')
        for edge in self.edgeSet:
            print(str(edge.begin) + ', ' + str(edge.end) + edge.weight + edge.T)


