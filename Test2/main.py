rows = 8
cols = 9
gems = [[1, 2, 1],[1, 3, 1],[1, 4, 1],[1, 5, 1],[1, 6, 1],[1, 7, 1],[2, 2, 1],[2, 3, 2],[2, 4, 2],[2, 5, 2],[2, 6, 2],[2, 7, 1],[3, 2, 1],[3, 3, 2],[3, 4, 1],[3, 5, 1],[3, 6, 2],[3, 7, 1],[4, 2, 1],[4, 3, 2],[4, 4, 1],[4, 5, 1],[4, 6, 2],[4, 7, 1],[5, 2, 1],[5, 3, 2],[5, 4, 2],[5, 5, 2],[5, 6, 2],[5, 7, 1],[6, 2, 1],[6, 3, 1],[6, 4, 1],[6, 5, 1],[6, 6, 1],[6, 7, 1]]
hits = [[3, 4]]
def countExplodedGems(rows, cols, gems, hits):
    # rows = hang
    # cols = cot 
    # gem = mang 2 chieu
    # hits = mang 2 chieu - hit
    # print(gems[hits[0][0]][hits[0][1]])
    result = 0
    HashGems = hashArray(gems)
    # print(HashGems[hits[0][0]*rows+hits[0][1]])
    for i in hits:
        if type(HashGems[i[0]*cols+i[1]]) is int:
            continue
        if HashGems[i[0]*cols+i[1]][1]==0:
            result+=1
            HashGems[i[0]*cols+i[1]][1] = 1
        result+=checkNeighBor(i,HashGems)
    return result
def checkNeighBor(hits,array):
    count =0
    if hits[1]-1>=0:
        # # check left 
        # left = [hits[0],hits[1]-1]
        # count += checkNeighBor(left,array)
        count += checkValue(array,hits,[hits[0],hits[1]-1])
    if hits[1]+1 < cols:
        # check right
        # right = [hits[0],hits[1]+1]
        # count += checkNeighBor(right,array)
        count +=checkValue(array,hits,[hits[0],hits[1]+1])
    if hits[0]-1 >=0:
        # check up
        # up = [hits[0]-1,hits[1]]
        # count += checkNeighBor(up,array)
        count +=checkValue(array,hits,[hits[0]-1,hits[1]])
    if hits[0]+1 < rows:
        # check down
        # down = [hits[0]+1,hits[1]]
        # count += checkNeighBor(down,array)
        count +=checkValue(array,hits,[hits[0]+1,hits[1]])  
    return count
def checkValue(array,hits,check):
    if type(array[hits[0]*cols+hits[1]]) is list and type(array[check[0]*cols+check[1]]) is list:
        if array[check[0]*cols+check[1]][1] == 0:
            if array[hits[0]*cols+hits[1]][0] == array[check[0]*cols+check[1]][0]:
                array[check[0]*cols+check[1]][1] = 1
                # print(check)
                return 1 + checkNeighBor(check,array)
    return 0
def hashArray(gems):
    HashArray = []
    for i in range(rows*cols):
        HashArray.append(0)
    for i in gems:
        HashArray[i[0]*cols+i[1]]=[i[2],0]
    return HashArray
print(countExplodedGems(rows, cols, gems, hits))
# array = []
# for i in range(rows):
#     array.append([])
#     for j in range(cols):
#         array[i].append(0)
# for i in gems:
#     array[i[0]][i[1]] = i[2]
# for i in array:
#     print(i)