import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents=[]
        for k,v in kwargs.items():
            for _ in range(v):
                self.contents.append(k)
    
    def draw(self,x):
        if x>len(self.contents):
            return self.contents
        else:
            ans=[]
            while x:
                rand=random.randint(0,len(self.contents)-1)
                ans.append(self.contents[rand])
                self.contents.pop(rand)
                x-=1
            return ans

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m=0
    for experiment in range(num_experiments):
        hat_copy=copy.deepcopy(hat)
        drawn=hat_copy.draw(num_balls_drawn)
        temp=0
        flag=True
        for k,v in expected_balls.items():
            if drawn.count(k)<v:
                flag=False
        if flag:
            m+=1
    return m/num_experiments