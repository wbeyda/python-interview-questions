def rotate2dMatrix(a):
  return list(zip(*a[::-1]))

if __name__ == '__main__':
    grid2 = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    expected_result_grid2 = [(7,4,1),
                            (8,5,2),
                            (9,6,3)]
    assert rotate2dMatrix(grid2) == expected_result_grid2