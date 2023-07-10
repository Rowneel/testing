size = 5
disk_size = 200


def CSCAN(arr, head):

	seek_count = 0
	distance = 0
	cur_track = 0
	left = []
	right = []
	seek_sequence = []

	left.append(0)
	right.append(disk_size - 1)

	for i in range(size):
		if (arr[i] < head):
			left.append(arr[i])
		if (arr[i] > head):
			right.append(arr[i])

	left.sort()
	right.sort()

	for i in range(len(right)):
		cur_track = right[i]

		seek_sequence.append(cur_track)

		distance = abs(cur_track - head)

		seek_count += distance

		head = cur_track

	head = 0
	seek_count += (disk_size - 1)

	for i in range(len(left)):
		cur_track = left[i]
		seek_sequence.append(cur_track)
		distance = abs(cur_track - head)
		seek_count += distance
		head = cur_track

	print("Total seek operations =",
		seek_count)
	print("Seek Sequence is")
	print(*seek_sequence, sep="\n")

# Driver code

arr = [180,70,30,60,40]
head = 73

CSCAN(arr, head)

