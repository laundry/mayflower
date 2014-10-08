import string

cc = [c for c in string.lowercase]
ccs = range(len(cc))

def cost(word):
    heat = 0
    running = 1
    for i in ccs:
        if cc[i] not in word:
            running *= 4
        else:
            heat += running
            running = 1
    return heat + running

def main():
    words = [line.strip().lower() for line in open("en_GB.txt")]
    costs = []
    for word in words:
        wort = [c for c in word]
        wort.sort()
        costs.append((cost(word), word, wort))
    costs.sort()
    q = open("costs.txt", "w")
    for costco in costs:
        q.write("%d %s %s\n" % (costco[0], costco[1], costco[2]))
    q.close()

if __name__ == "__main__":
    main()

