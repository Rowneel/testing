from queue import Queue
def fifo_page(pages,frame):
    pageQueue = Queue()
    pagefault = 0
    print("Page\tReference")
    for page in pages:
        print(page,end="\t")
        if page not in list(pageQueue.queue):
            if len(list(pageQueue.queue)) == frame:
                pageQueue.get()
            pageQueue.put(page)
            pagefault +=1
            print(list(pageQueue.queue))                
        else:
            print(list(pageQueue.queue))
        print("")
    print(pagefault)
    
pages = [4,1,2,4,5]
frame = 3  
fifo_page(pages,frame)