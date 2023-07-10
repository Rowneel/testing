from queue import Queue
def fifo_page(pages,frame):
    s = set()
    pageQueue = Queue()
    pagefault = 0
    print("Page\t\tReference")
    for page in pages:
        print(page,end="\t")
        if page not in s:
            if len(list(pageQueue.queue)) == frame:
                oldPage = pageQueue.queue[0]
                pageQueue.get()
                s.remove(oldPage)                 
            pageQueue.put(page)
            s.add(page)
            pagefault +=1
            print(list(pageQueue.queue))                
        else:
            print(list(pageQueue.queue))
        print("")
     
pages = [4,1,2,4,5]
frame = 2
      
fifo_page(pages,frame)