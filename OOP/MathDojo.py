class MathDojo:
    def __init__(self, result=0):
        self.result=result
    def __str__(self):
        return str(self.result)

    def add(self, num, *nums):
        sum=0
        for a in nums:
            sum+=a  
        x=sum+num
        self.result+=x
        return self
    def subtract(self, num, *nums):
        total=0
        for a in nums:
            total+=a
        x=total+num
        self.result-=x
        return self
        

md1 = MathDojo()
md2 = MathDojo()
md3 = MathDojo()
print(md1.add(2).add(2,9,2).subtract(3,1))
print(md2.add(2).subtract(1).add(2,9,2).subtract(3,1))
print(md3.add(7,1,3).subtract(1,3).add(2,9,2).subtract(3))

