
class MathDojo:
    def __init__(this, result=0):
        this.result = result
    def add(this, *nums):
        # this.result += num
        for n in nums:
            this.result += n
        return this
    def subtract(this, *nums):
        for n in nums:
            this.result -= n
        return this
    def printNum(this):
        print("num: " + str(this.result))

md = MathDojo()
md.add(5).add(2).add(3,5,1,4).printNum()
md.subtract(1).subtract(3).printNum()
