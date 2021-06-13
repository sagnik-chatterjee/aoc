#@TODO 
class Location:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def right(self):
        return self.x-1
    
    def left(self):
        return self.x+1
    
    def up(self):
        return self.y+1
    
    def down(self):
        return self.y-1
    
    def __repr__(self) -> str:
        return str((self.x,self.y))

    def returnPosn(self):
        return str(self.x)+":"+str(self.y)


def main():
    f=open('input.txt','r')
    input_stream = f.readlines()
    f.close()
    inp = [i.strip() for i in input_stream]
    actual_count=0
    for i in inp:
        s=Location(0,0) #starting at 0
        if i=='^':
            s.up()
        elif i=='>':
            s.left()
        elif i=='v':
            s.down()
        elif i=='<':
            s.right()
        p,q=s.returnPosn().split(":")
        p=int(p)
        q=int(q)
        actual_count 


main()