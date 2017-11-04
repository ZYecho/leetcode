def longestIncreasingPath(matrix):

    shape_0 = len(matrix)
    shape_1 = len(matrix[1])
    d = [[1]*shape_1 for _ in range(shape_0)]
    v = [[0]*shape_1 for _ in range(shape_0)]
    pre = [[(0,0)]*shape_1 for _ in range(shape_0)]

    def search(i, j):
        if v[i][j] >0: return d[i][j]
        _max, idx= 0, (i, j)
        for m, n in [(0,1),(0,-1),(1,0),(-1,0)]:
                p = i+m
                q = j+ n
                if p >= shape_0 or q >= shape_1 or p < 0 or q < 0 : continue
                if matrix[i+m][j+n] < matrix[i][j]:
                    _len = search(i+m, j+n)
                    if _len > _max:
                        _max = _len
                        idx = (i+m, j+n)

        pre[i][j] = idx
        v[i][j] = 1
        d[i][j]+=_max
        return d[i][j]

    _max, idx = 0, (0,0)
    for i in range(shape_0):
        for j in range(shape_1):
            _len = search(i, j)
            if _len > _max:
                _max= _len
                idx = (i, j)
    print(_max)
    _list = []
    while pre[idx[0]][idx[1]]!= (idx[0],idx[1]):
        _list.append(matrix[idx[0]][idx[1]])
        idx = pre[idx[0]][idx[1]]
    _list.append(matrix[idx[0]][idx[1]])
    print(_list[::-1])

if __name__ == '__main__':
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    # matrix = [[3,4,5],[3,2,6],[2,2,1]]
    longestIncreasingPath(matrix)
