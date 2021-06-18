
def part1(str1):
    count=0
    status=False
    for i in str1:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count+=1
            if count ==3:
                status=True
                break 
    return status 

def part2(str1):
    status=False
    count=0
    for i in range(len(str1)-1):
        if str1[i] == str1[i+1]:
            count+=1
        
        if count ==1 :
            status=True
            break 
    return status 

def part3(str1):
    status=True
    for i in range(len(str1)-1):
        if str1[i]!='a' and str1[i+1]!='b':
            status=False
            break
        elif str1[i]!='c' and str1[i+1]!='d':
            status=False
            break
        elif str1[i]!='p' and str1[i+1]!='q':
            status=False
            break
        elif str1[i]!='x' and str1[i]!='y':
            status=False
            break 
    return status        
                        


def main():
    input_stream=[]
    with open("input.txt") as f:
        inp= f.readlines()
        input_stream=[i.strip() for i in inp]
    
    nice_strings=0
    for i in input_stream:
        if part1(i) and part2(i) and part3(i):
            nice_strings+=1
        
    print(nice_strings)



main()