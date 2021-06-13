def main():
    f=open('input.txt')
    inp= f.readlines()
    f.close()
    input_stream = [i.strip() for i in inp]
    print(input_stream)

if __name__=='__main__':
    main()