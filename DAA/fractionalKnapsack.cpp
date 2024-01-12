// C++ program to solve fractional
// Knapsack Problem
#include <bits/stdc++.h>
using namespace std;

// Structure for an item which stores
// weight & corresponding value of Item
// struct Item {
// 	int value, weight;

// 	// Constructor
// 	Item(int value, int weight)
// 		: value(value), weight(weight)
// 	{
// 	}
// };

class Item {
public:
    int value;
    int weight;

    // Constructor with initialization in the body
    Item(int val, int w) {
        value = val;
        weight = w;
    }
};


// Comparison function to sort Item
// according to val/weight ratio
bool cmp(Item a,Item b)
{
	double r1 = (double)a.value / a.weight;
	double r2 = (double)b.value / b.weight;
	return r1 > r2;
}

// Main greedy function to solve problem
double fractionalKnapsack(Item arr[],
						int N, int size)
{
	// Sort Item on basis of ratio
	sort(arr, arr + size, cmp);

	cout << "Value \tWeight"<< endl;
	for (int i = 0; i < size; i++)
	{
		/* code */
		cout << arr[i].value << "\t" << arr[i].weight << endl ;
	}
	cout << endl;
	
	// Current weight in knapsack
	int curWeight = 0;

	// Result (value in Knapsack)
	double finalvalue = 0.0;

	// Looping through all Items
	cout << "\tValue \tweight" << endl;
	for (int i = 0; i < size; i++) {

		// If adding Item won't overflow,
		// add it completely
		if (curWeight + arr[i].weight <= N) {
			curWeight += arr[i].weight;
			finalvalue += arr[i].value;
			cout << "added: " << arr[i].value << "\t" << arr[i].weight << endl;
		}

		// If we can't add current Item,
		// add fractional part of it
		else {
			int remain = N - curWeight;
			finalvalue += arr[i].value
						* ((double)remain
							/ arr[i].weight);
			cout << "added: " << arr[i].value << "*" <<  (double)remain <<"/"<< arr[i].weight << "\t" << (double)remain <<'/'<< arr[i].weight << endl;
			break;
		}
	}

	// Returning final value
	return finalvalue;
}

// Driver Code
int main()
{
	// Weight of knapsack
	int N = 60;

	// Given weights and values as a pairs
	Item arr[] = { { 100, 10 },
				{ 280, 40 },
				{ 120, 20 },
				{ 120, 24 } };

	int size = sizeof(arr) / sizeof(arr[0]);

	// Function Call
	cout << "Maximum profit earned = "
		<< fractionalKnapsack(arr, N, size);
	return 0;
}
