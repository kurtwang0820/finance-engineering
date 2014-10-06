#create pattern model (1,0) 1 changes to 0 at intersect
class FinModel:
    def __init__(self,x,y,intersect=0):
        self.x=x
        self.y=y
        self.intersect=intersect
    def set_intersect(self,num):
        self.intersect=num
    def __str__(self):
        if self.x==0:
            if self.y==1:
                return 'Buy a call at strike price %d \n'%(self.intersect)
            else:
                return 'Sell a call at strike price %d \n'%(self.intersect)
        elif self.x==1:
            return 'Sell a put at strike price %d \n'%(self.intersect)
        else:
            return 'Buy a put at strike price %d \n'%(self.intersect)
    def __repr__(self):
        return self.__str__()
#create a period (0,50)->slope:1
class SlopeModel:
    def __init__(self,start,end,slope):
        self.start=start
        self.end=end
        self.slope=slope        

output=[]
def find_model(aList):
    global output
    i=0
    #1(0,1)2(-1,0)3(0,-1)4(1,0)
    while i < len(aList):
        if len(aList)==1:
            one_point_left(aList)
            break
        if i>2:
            add_compension(aList,i)
        if i==len(aList)-1:
            break
        if i==len(aList)-2:
            two_point_left(aList,i)
            break
        firstSlope=aList[i].slope
        secondSlope=aList[i+1].slope
        thirdSlope=aList[i+2].slope
        patternRecogThree={'010':zero_one_zero,'01-1':zero_one_none,'0-11':zero_none_one,
        '0-10':zero_none_zero,'-101':none_zero_one,'-10-1':none_zero_none,'-110':none_one_zero,
        '-11-1':none_one_none,'1-11':one_none_one,'1-10':one_none_zero,'101':one_zero_one,'10-1':one_zero_none}
        patternMesg=str(firstSlope)+str(secondSlope)+str(thirdSlope)
        patternRecogThree[patternMesg](i)
        i+=3
#add compension
def add_compension(aList,i):
    firstSlope=aList[i-1].slope
    secondSlope=aList[i].slope
    patternRecog={'01':comp_zero_one,'0-1':comp_zero_none,'-11':comp_none_one,'-10':comp_none_zero,'1-1':comp_one_none,'10':comp_one_zero}
    patternMesg=str(firstSlope)+str(secondSlope)
    patternRecog[patternMesg](i-1)


    
def comp_one_zero(i):
    global output
    output.append(FinModel(0,-1,aSlopeModelList[i].end))
def comp_one_none(i):
    global output
    output.append(FinModel(0,-1,aSlopeModelList[i].end))
    output.append(FinModel(0,-1,aSlopeModelList[i].end))
def comp_none_zero(i):
    global output
    output.append(FinModel(0,1,aSlopeModelList[i].end))
def comp_none_one(i):
    global output
    output.append(FinModel(0,1,aSlopeModelList[i].end))
    output.append(FinModel(0,1,aSlopeModelList[i].end))
def comp_zero_none(i):
    global output
    output.append(FinModel(0,-1,aSlopeModelList[i].end))
def comp_zero_one(i):
    global output
    output.append(FinModel(0,1,aSlopeModelList[i].end))
    
#only two left
def two_point_left(aList,i):
    firstSlope=aList[i].slope
    secondSlope=aList[i+1].slope
    patternRecog={'01':zero_one,'0-1':zero_none,'-11':none_one,'-10':none_zero,'1-1':one_none,'10':one_zero}
    patternMesg=str(firstSlope)+str(secondSlope)
    patternRecog[patternMesg](i)

def two_point_left(aList,i):
    firstSlope=aList[i].slope
    secondSlope=aList[i+1].slope
    patternRecog={'01':zero_one,'0-1':zero_none,'-11':none_one,'-10':none_zero,'1-1':one_none,'10':one_zero}
    patternMesg=str(firstSlope)+str(secondSlope)
    patternRecog[patternMesg](i)

def one_zero(i):
    global output
    output.append(FinModel(1,0,aSlopeModelList[i].end))
def one_none(i):
    global output
    output.append(FinModel(1,0,aSlopeModelList[i].end))
    output.append(FinModel(0,-1,aSlopeModelList[i].end))
def none_zero(i):
    global output
    output.append(FinModel(-1,0,aSlopeModelList[i].end))
def none_one(i):
    global output
    output.append(FinModel(-1,0,aSlopeModelList[i].end))
    output.append(FinModel(0,1,aSlopeModelList[i].end))
def zero_none(i):
    global output
    output.append(FinModel(0,-1,aSlopeModelList[i].end))
def zero_one(i):
    global output
    output.append(FinModel(0,1,aSlopeModelList[i].end))
#every three
def one_zero_none(i):
    global output
    output.append(FinModel(1,0,aSlopeModelList[i].end))
    output.append(FinModel(0,-1,aSlopeModelList[i+1].end))
def one_zero_one(i):
    global output
    output.append(FinModel(1,0,aSlopeModelList[i].end))
    output.append(FinModel(0,1,aSlopeModelList[i+1].end))
def one_none_zero(i):
    global output
    output.append(FinModel(1,0,aSlopeModelList[i].end))
    output.append(FinModel(0,-1,aSlopeModelList[i].end))
    output.append(FinModel(0,1,aSlopeModelList[i+1].end))
def one_none_one(i):
    global output
    output.append(FinModel(1,0,aSlopeModelList[i].end))
    output.append(FinModel(0,-1,aSlopeModelList[i].end))
    output.append(FinModel(0,1,aSlopeModelList[i+1].end))
    output.append(FinModel(0,1,aSlopeModelList[i+1].end))
def none_one_none(i):
    global output
    output.append(FinModel(0,1,aSlopeModelList[i].end))
    output.append(FinModel(0,1,aSlopeModelList[i].end))
    output.append(FinModel(0,-1,aSlopeModelList[i+1].end))
    output.append(FinModel(0,-1,aSlopeModelList[i+1].end))
def none_one_zero(i):
    global output
    output.append(FinModel(-1,0,aSlopeModelList[i].end))
    output.append(FinModel(0,1,aSlopeModelList[i].end))
    output.append(FinModel(0,-1,aSlopeModelList[i+1].end))
def none_zero_none(i):
    global output
    output.append(FinModel(-1,0,aSlopeModelList[i].end))
    output.append(FinModel(0,-1,aSlopeModelList[i+1].end))
def none_zero_one(i):
    global output
    output.append(FinModel(-1,0,aSlopeModelList[i].end))
    output.append(FinModel(0,1,aSlopeModelList[i+1].end))
def zero_none_zero(i):
    global output
    output.append(FinModel(0,-1,aSlopeModelList[i].end))
    output.append(FinModel(0,1,aSlopeModelList[i+1].end))
def zero_none_one(i):
    global outpout
    output.append(FinModel(0,-1,aSlopeModelList[i].end))
    output.append(FinModel(0,1,aSlopeModelList[i+1].end))
    output.append(FinModel(0,1,aSlopeModelList[i+1].end))
def zero_one_none(i):
    global output
    output.append(FinModel(0,1,aSlopeModelList[i].end))
    output.append(FinModel(0,-1,aSlopeModelList[i+1].end))
    output.append(FinModel(0,-1,aSlopeModelList[i+1].end))    
def zero_one_zero(i):
    global output
    output.append(FinModel(0,1,aSlopeModelList[i].end))
    output.append(FinModel(0,-1,aSlopeModelList[i+1].end))
#only one left
def one_point_left(aList):
    global output
    if aList[-1].slope==1:
        output.append(FinModel(1,0,aList[-1].end))
    if aList[-1].slope==-1:
        output.append(FinModel(-1,0,aList[-1].end))
    if aList[-1].slope==0:
        if len(output)==0:
            output.append(FinModel(0,-1,aList[-1].end))
            output.append(FinModel(0,1,aList[-1].end))
        else:
            if output[-1].y==1:
                output.append(FinModel(0,-1,aList[-1].start))
            if output[-1].y==-1:
                output.append(FinModel(0,1,aList[-1].start))
#test output
aSlopeModelList=[]
end_input=False
print 'example (0,50)->1 please enter: 0,50,1'
while not end_input:    
    user_mesg=raw_input("please enter your input, enter done to exit: ")
    if user_mesg=='done':
        end_input=True
    else:
        user_input=user_mesg.split(',')
        aSlopeModelList.append(SlopeModel(int(user_input[0]),int(user_input[1]),int(user_input[2])))

find_model(aSlopeModelList)
print output

"""
first=SlopeModel(0,10,1)
second=SlopeModel(10,20,-1)
third=SlopeModel(20,30,1)
forth=SlopeModel(30,50,-1)
fifth=SlopeModel(50,60,0)
sixth=SlopeModel(60,70,1)
seventh=SlopeModel(70,80,0)
eighth=SlopeModel(80,90,-1)
ninth=SlopeModel(90,100,0)
tenth=SlopeModel(100,120,-1)
eleventh=SlopeModel(120,130,1)
twelfth=SlopeModel(130,200,-1)
aSlopeModelList=[first,second,third,forth,fifth,sixth,seventh,eighth,ninth,tenth,eleventh,twelfth]
"""
