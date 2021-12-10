def maxActivities(times):
    i = 0
    print(i, end=" ")

    for j in range(1, len(times)):
        if times[j][0] > times[i][1]:
            print(j, end=" ")
            i = j

    print("")


times = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
times.sort(key=lambda x: x[1])

print(times)

maxActivities(times)
