import unittest

class Computer(unittest.TestCase):
    def setUp(self): #初始化方法,必须是setUp
        self.s = 0
        self.n = 2**20

    def testComputer(self):
        for i in range(self.n):
            self.s += i
    def tearDown(self):
        print('计算结束,结果为',self.s)

if __name__=='__main__':

    unittest.main()




