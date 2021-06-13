def main():
    f = open("input.txt", "r")
    input_stream = f.readlines()
    f.close()
    inp = [i.strip() for i in input_stream]
    total = 0
    for i in inp:
        l, w, h = i.split("x")
        l=int(l)
        w=int(w)
        h=int(h)
        paper_needed = min(l+l+w+w,l+l+h+h,w+w+h+h)

        volume= l*w*h
        total += paper_needed+volume
    print(total)


if __name__ == "__main__":
    main()
