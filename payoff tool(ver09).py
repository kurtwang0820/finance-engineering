#payoff that we replicate from the given payoff
class FinModel:
    def __init__(self,x,y,intersect=0,num_calls=1):
        self.x=x
        self.y=y
        self.intersect=intersect
        self.num_calls=num_calls
    def set_intersect(self,num):
        self.intersect=num
    def __str__(self):
        if self.x==0:
            if self.y==1:
                return 'Buy %d call at strike price %d \n'%(self.num_calls,self.intersect)
            else:
                return 'Sell %d call at strike price %d \n'%(self.num_calls,self.intersect)
        elif self.x==1:
            return 'Sell %d put at strike price %d \n'%(self.num_calls,self.intersect)
        else:
            return 'Buy %d put at strike price %d \n'%(self.num_calls,self.intersect)
    def __repr__(self):
        return self.__str__()
#create a payoff period
class SlopeModel:
    def __init__(self,start,end,slope):
        self.start=start
        self.end=end
        self.slope=slope  
#used to store the output         
output=[]
#find the correct payoff combinations of given payoff
def find_model(aList):
    global output
    i=0
    if len(aList)==1:
        one_slope_exist(aList)
    #pre-processing the first two periods
    if len(aList)>1:
        process_first_two(aList)
        #buy call(0,1) buy put(-1,0) sell call(0,-1) sell put(1,0)
        for i in range(2,len(aList)):
            if aList[i].slope-aList[i-1].slope<0:
                output.append(FinModel(0,-1,aList[i].start,aList[i-1].slope-aList[i].slope))
            else:
                output.append(FinModel(0,1,aList[i].start,aList[i].slope-aList[i-1].slope))
#process the first two periods
def process_first_two(aList):
    if aList[0].slope==0:
        if aList[1].slope>0:
            output.append(FinModel(0,1,aList[0].end,aList[1].slope))
        else:
            output.append(FinModel(0,-1,aList[0].end,-aList[1].slope))
    elif aList[0].slope>0:
        output.append(FinModel(1,0,aList[0].end,aList[0].slope))
        output.append(FinModel(0,-1,aList[0].end,aList[0].slope-aList[1].slope))
    else:
        output.append(FinModel(-1,0,aList[0].end,-aList[0].slope))
        output.append(FinModel(0,1,aList[0].end,aList[1].slope-aList[0].slope))
#from start to end, there is only one kind of payoff trend exist
def one_slope_exist(aList):
    global output
    if aList[-1].slope==1:
        output.append(FinModel(1,0,aList[-1].end))
    if aList[-1].slope==-1:
        output.append(FinModel(-1,0,aList[-1].end))
    if aList[-1].slope==0:
        if len(output)==0:
            #if the slope is 0 for all the time, we choose the above model
            #as default            
            output.append(FinModel(0,-1,aList[-1].end))
            #output.append(FinModel(0,1,aList[-1].end))


while True:
    aSlopeModelList=[]
    output=[]
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
    

