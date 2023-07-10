#include <iostream>
#include <queue>
#include <vector>
#include <unordered_set>

using namespace std;

void FIFOPageReplacement(const vector<int>& pages, int capacity) {
    queue<int> pageQueue;
    unordered_set<int> pageSet;

    int pageFaults = 0;

    cout << "Page Reference\t" << endl;

    for (int page : pages) {
        cout << page << "\t";

        if (pageSet.find(page) == pageSet.end()) {
            if (pageQueue.size() == capacity) {
                int frontPage = pageQueue.front();
                pageQueue.pop();
                pageSet.erase(frontPage);
            }

            pageQueue.push(page);
            pageSet.insert(page);
            pageFaults++;

            queue<int> tempQueue = pageQueue;
            while (!tempQueue.empty()) {
                cout << tempQueue.front() << " ";
                tempQueue.pop();
            }
        }
        else {
            queue<int> tempQueue = pageQueue;
            while (!tempQueue.empty()) {
                cout << tempQueue.front() << " ";
                tempQueue.pop();
            }
        }

        cout << endl;
    }

    cout << "Total Page Faults: " << pageFaults << endl;
}

int main() {
    vector<int> pages;
    int capacity,pageNo,x;

    cout<<"Enter capacity";
    cin>>capacity;
    cout<<"Enter number of page reference:";
    cin>>pageNo;
    cout<<"Enter page references:";
    for (int i = 0; i < pageNo; i++)
    {
        
        cin>>x;
        pages.push_back(x);
    }

    FIFOPageReplacement(pages, capacity);

    return 0;
}
