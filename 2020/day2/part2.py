"""
def main():
    input_stream = []
    f = open("input.txt", "r")
    inp = f.readlines()
    f.close()
    input_stream = [i.strip() for i in inp]
    sled_policy=0
    toboggan_policy=0
    for i in input_stream:
        pwd_policy, passwd = i.split(":")
        pwd_pol, char = pwd_policy.split(" ")
        posn1, posn2 = pwd_pol.split("-")
        posn1=int(posn1)
        posn2=int(posn2)

        #count number of occurences of smbol in pw 
        num_symbols = passwd.count(char)
        #count1=0
        if(posn1 <=num_symbols) and (num_symbols<=posn2):
            sled_policy+=1
        
        #check if the character at lower is the same as symbol or that 
        # the character at upper is the same as symbol , notet that both are 
        # not allowed(xor)
        if(passwd[posn1-1] is char) ^(passwd[posn2-1] is char):
            toboggan_policy+=1


    print(sled_policy)
    print(toboggan_policy)


if __name__ == "__main__":
    main()
"""
import fileinput

if __name__ == "__main__":
    count = 0

    for policy_with_password in fileinput.input(files="input.txt"):
        # Parse line (policy_with_password) like "3-11 k: password"
        rule, pw = policy_with_password.split(": ", maxsplit=1)
        minmax, symbol = rule.split(" ", maxsplit=1)
        lower, upper = (int(x) for x in minmax.split("-", maxsplit=1))

        # Count number of occurrences of symbol in pw
        num_symbols = pw.count(symbol)

        # Check that the character at lower is the same as symbol or that the character
        # at upper is the same as symbol, note that not both are allowed (thus the
        # "exclusive or" ^).
        if (pw[lower - 1] is symbol) ^ (pw[upper - 1] is symbol):
            count += 1

    print(count)
