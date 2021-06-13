def main():
    f = open("input.txt", "r")
    input_stream = f.readlines()
    f.close()
    inp = [i.strip() for i in input_stream]
    total = 0
    for i in inp:
        l, w, h = i.split("x")
        total_cover = 2 * int(l) * int(w) + 2 * int(w) * int(h) + 2 * int(l) * int(h)
        list1 = []
        list1.append(int(l))
        list1.append(int(w))
        list1.append(int(h))
        list1.sort()
        cover_area = list1[0] * list1[1]
        total += cover_area + total_cover
    print(total)


if __name__ == "__main__":
    main()
