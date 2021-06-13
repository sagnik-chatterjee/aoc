from itertools import chain 
from math import prod

def main():
    # part 1
    list1 = []
    with open("input.txt") as f:
        read = f.readlines()
        list1 = [int(i.strip()) for i in read]
    result = 0
    for i in list1:
        for j in list1:
            if i != j:
                if i + j == 2020:
                    result = i * j
    #print(result)
    ## part 2
    ## solving for the 3 parts
    '''
    dict1={}
    #dict2={}
    for i in list1:
        temp1= 2020-i
        for j in list1:
            temp2= temp1-j
            if temp2<0:
                pass 
            else:
                #tup1=(temp2,j)
                dict1[i]=temp2*j
                break
    #for key,value in dict1.values():
    #print(dict1)    
    #sanity check
    list1=[] 
    for keys,values in zip(dict1.keys(),dict1.values()):
        list1.append(keys*values)
    list1=list1.sort(reverse=True)
    print(list1[0])
    '''
if __name__ == "__main__":
    main()
