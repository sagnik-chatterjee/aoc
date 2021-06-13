def main():
    list1=[]
    with open('input.txt') as f:
        read=f.readlines()
        list1=[int(i.strip()) for i in read]
    reuslt=0
    for i in list1:
        for j in list1:
            if i!=j:
                if i+j == 2020:
                    result=i*j
    print(result)


if __name__=='__main__':
    main()