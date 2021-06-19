def main():
    input_stream=[]
    with open("input.txt","r") as f:
        inp=f.readlines()
        input_stream=[i.strip() for i in inp]
    print(input_stream)

main()