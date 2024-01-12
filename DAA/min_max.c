#include <stdio.h>
int max, min;
int a[] = {5, 7, 3, 4, 9, 12, 6, 2};
void maxmin(int l, int r)
{
  int max1, min1, mid;
  if (l == r)
  {
    max = min = a[l];
  }
  else if (l == r - 1)
  {
    if (a[l] < a[r])
    {
      max = a[r];
      min = a[l];
    }
    else
    {
      max = a[l];
      min = a[r];
    }
  }
  else
  {
    mid = (l + r) / 2;
    maxmin(l, mid);
    max1 = max;
    min1 = min;
    maxmin(mid + 1, r);
    if (max1 > max)
      max = max1;
    if (min1 < min)
      min = min1;
  }
}
int main()
{
  int num = 7;
  // max = a[0];
  // min = a[0];
  maxmin(0, num);
  printf("Max element in an array : %d\n", max);
  printf("Min element in an array : %d\n", min);
  return 0;
}
