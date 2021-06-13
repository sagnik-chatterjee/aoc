def main():
    f=open('input.txt','r')
    input_stream=f.readline()
    f.close()
    posn=0
    score=0
    for i in input_stream:
        if i=='(':
            posn+=1
            score+=1
        elif i==')':
            posn+=1
            score-=1
            if score<0:
                break 
    print(posn)

if __name__ =='__main__':
    main()
         