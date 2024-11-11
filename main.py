from jones import *
n=1

input_knot=np.array([[[1, 0, 0],[4, 0, 0],[1, 6, 2],[0, 2, -5],[5, 2, 5],[4, 6, -2]]], dtype=object)

start_time=time.time()

expected = expected_jones(input_knot, n)

end_time=time.time()

print("Jones Polynomial : ", expected)
print("Time (Seconds): ", end_time-start_time)