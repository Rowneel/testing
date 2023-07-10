def pageFaults(pages, n, capacity):
    s = set()
    indexes = {}
    page_faults = 0

    for i in range(n):
        print(pages[i],end="\t")
        if len(s) < capacity:
            if pages[i] not in s:
                s.add(pages[i])
                page_faults += 1
            indexes[pages[i]] = i
            print(list(s))
        else:
            if pages[i] not in s:
                lru = float('inf')
                for page in s:
                    if indexes[page] < lru:
                        lru = indexes[page]
                        val = page
                s.remove(val)
                s.add(pages[i])
                page_faults += 1
            indexes[pages[i]] = i
            print(list(s))

    return page_faults


pages = [4,1,2,4,5]
n = len(pages)
capacity = 3
print(pageFaults(pages, n, capacity))
