def main():
    f=open('input.txt','r')
    input_stream=f.readline()
    f.close()
    count_floor= 0 
    for i in input_stream:
        if i =='(':
            count_floor+=1
        elif i==')':
            count_floor-=1
    print(count_floor)

if __name__=='__main__':
    main()