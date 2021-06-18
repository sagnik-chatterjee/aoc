import hashlib 


inp1='abcdef'
inp2='pqrstuv'

def main():
    try:
        input_str="yzbqklnj"
        #hash_output =hashlib.md5(bytes(input_str,'utf-8'))
        num1=0
        for i in range(0,100000000):
            str1= input_str+str(i)
            hash_output=(hashlib.md5(bytes(str1,'utf-8'))).hexdigest()
            if hash_output[:5] == '00000':
                num1=i
                break 
            print(f" Test #{i} is not the solution , doing next")
        print(num1)
    except Exception as e:
        print(e)             

main()

#check()   
