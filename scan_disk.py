size = 5
disk_size = 200

def SCAN(arr, head, direction):
	seek_count = 0
	distance, cur_track = 0, 0
	left = []
	right = []
	seek_sequence = []

	if direction == "left":
		left.append(0)
	elif direction == "right":
		right.append(disk_size - 1)

	for i in range(size):
		if arr[i] < head:
			left.append(arr[i])
		if arr[i] > head:
			right.append(arr[i])

	left.sort()
	right.sort()

	run = 2
	while run != 0:
		if direction == "left":
			for i in range(len(left) - 1, -1, -1):
				cur_track = left[i]
				seek_sequence.append(cur_track)
				distance = abs(cur_track - head)
				seek_count += distance
				head = cur_track
			
			direction = "right"
	
		elif direction == "right":
			for i in range(len(right)):
				cur_track = right[i]
				seek_sequence.append(cur_track)
				distance = abs(cur_track - head)
				seek_count += distance
				head = cur_track
			
			direction = "left"
		
		run -= 1

	print("Total seek operations =", seek_count)
	print("Seek Sequence is")

	for i in range(len(seek_sequence)):
		print(seek_sequence[i])

arr = [180,70,30,60,40]
head = 73
direction = "left"

SCAN(arr, head, direction)
