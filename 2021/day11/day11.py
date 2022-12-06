import numpy as np

matrix = np.loadtxt(open("input.txt", "r"), dtype ='int')
ones_10x10 = np.ones((10,10), dtype = int)
ones_3x3 = np.ones((3,3), dtype = int)

explosions = 0
for step in range(1,1000):
    matrix = matrix + ones_10x10
    flashed_matrix = np.zeros((10,10), dtype = int)
    check_for_flashes = True
    while check_for_flashes:
        check_for_flashes = False
        energy_matrix = np.zeros((12,12), dtype = int)
        for x in range(0,10):
            for y in range(0,10):
                if matrix[x][y]>9 and flashed_matrix[x][y] == 0:
                    check_for_flashes = True
                    flashed_matrix[x][y] = 1
                    explosions += 1
                    energy_matrix[x:x+3,y:y+3] += ones_3x3
        matrix += energy_matrix[1:11,1:11]
        
    # clear flashed    
    for x in range(0,10):
        for y in range(0,10):
            if matrix[x][y]>9:
                matrix[x][y] = 0
                
    if (np.array_equal(flashed_matrix, ones_10x10)):
        print("Step {} - Explosions {}".format(step, explosions))
        quit()
