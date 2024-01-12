#include <bits/stdc++.h>
using namespace std;
// Partitioning the array on the basis of values at high as pivot value.
int Partition(int a[], int low, int high) {
   int pivot, index, i;
   index = low;
   pivot = high;
   for(i=low; i < high; i++) {
      // finding index of pivot.
      if(a[i] < a[pivot]) {
         swap(a[i], a[index]);
         index++;
      }
   }
   swap(a[pivot], a[index]);
   return index;
}
int RandomPivotPartition(int a[], int low, int high){
   // Random selection of pivot.
   int pvt, n, temp;
   n = rand();
   pvt = low + n%(high-low+1); // Randomizing the pivot value from sub-array.
   swap(a[high], a[pvt]);
   return Partition(a, low, high);
}
void quick_sort(int arr[], int p, int q) {
   //recursively sort the list
   int pindex;
   if(p < q) {
      pindex = RandomPivotPartition(arr, p, q); //randomly choose pivot
      // Recursively implementing QuickSort.
      quick_sort(arr, p, pindex-1);
    quick_sort(arr, pindex+1, q);
}
}
int main() {
int i;
int arr[]={5, 7 , 3, 4, 9 , 12 , 6 , 2};
cout<<"Before Sorting: ";
for (i = 0; i < 8; i++)
cout << arr[i] << " ";
cout << endl;
quick_sort(arr, 0, 8 - 1); //sort the elements of array
cout<<"After Sorting: ";
for (i = 0; i < 8; i++)
cout << arr[i] << " ";
cout << endl;
return 0;
}
