def main():
    input_stream = []
    f = open("input.txt", "r")
    inp = f.readlines()
    f.close()
    input_stream = [i.strip() for i in inp]
    count = 0
    for i in input_stream:
        pwd_policy, passwd = i.split(":")
        pwd_pol, char = pwd_policy.split(" ")
        min_count, max_count = pwd_pol.split("-")
        count1 = 0
        for i in passwd:
            if i == char:
                count1 += 1
        if count1 >= int(min_count) and count1 <= int(max_count):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
