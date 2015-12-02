def pascal_triangle(num_row):
    tri_list = []
    for row in range(num_row):
        for col in range(row + 1):
            if col == 0:
                tri_list.append([1])
            elif col == row:
                tri_list[row].append(1)
            else:
                tri_list[row].append(tri_list[row - 1][col - 1] + tri_list[row - 1][col])
                
    for row in tri_list:
        print(row)
        
pascal_triangle(12)        