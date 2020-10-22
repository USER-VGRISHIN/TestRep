import math
class Triangle(object):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.A = [x1, y1]
        self.B = [x2, y2]
        self.C = [x3, y3]
        self.AB = math.sqrt(pow(self.B[0] - self.A[0], 2) + pow(self.B[1] - self.A[1], 2))
        self.BC = math.sqrt(pow(self.C[0] - self.B[0], 2) + pow(self.C[1] - self.B[1], 2))
        self.AC = math.sqrt(pow(self.C[0] - self.A[0], 2) + pow(self.C[1] - self.A[1], 2))

    def triangleExist(self):

        if (self.A[0] == self.B[0] and self.A[1] == self.B[1]) or \
                (self.B[0] == self.C[0] and self.B[1] == self.C[1]) or \
                (self.A[0] == self.C[0] and self.A[1] == self.C[1]):
            return False
        else:
            return True

    def getArea(self):
        return 0.5 * abs((self.B[0] - self.A[0]) * (self.C[1] - self.A[1]) - (self.C[0] - self.A[0]) * (self.B[1] - self.A[1]))

    def getPer(self):
        return self.AB + self.AC + self.BC