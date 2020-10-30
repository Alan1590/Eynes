class Matriz():

    def iniciar(self):
        m = [[10, 5, 82, 15, 32],
             [34, 2, 5, 32, 54],
             [35, 9, 13, 15, 36],
             [45, 16, 33, 15, 44],
             [76, 74, 43, 15, 66]]
        self.matriz(m)

    def matriz(self, m):
        """
                This function take a array list 5x5 and returns
                the position initial_position (x and y) and final_position (x,y)
                of all repeated values
                >>> matriz=[[43,32,55,66,1],
                ...     [4,53,64,66,12],
                ...     [3,9,66,12,29],
                ...     [85,88,91,25,48],
                ...     [12,14,13,12,1]]
                >>> m = Matriz()
                >>> m.matriz(matriz)
                [(' 0,3', '1,3'), (' 1,3', '2,2'), (' 1,4', '2,3'), (' 2,3', '4,0'), (' 4,0', '4,3'), (' 0,4', '4,4')]
                """
        result = []
        position_x = 0
        position_y = 0
        while (position_x < 5 and position_y < 5):
            element = m[position_x][position_y]
            not_empty = self.element_to_search(m, element, position_x, position_y)
            if not_empty:
                result.append(self.element_to_search(m, element, position_x, position_y))
            if position_y == 4:
                position_x += 1
                position_y = 0
            else:
                position_y += 1
        return self.get_final_result(result)

    def get_final_result(self, result):
        """
                This method return the result order and filter the elements give it
                for the method matriz()
                >>> res=[['1,3; 0,3', '2,2; 0,3'], ['4,4; 0,4'], ['2,2; 1,3'], ['2,3; 1,4', '4,0; 1,4', '4,3; 1,4'], ['4,0; 2,3', '4,3; 2,3'], ['4,3; 4,0']]
                >>> m = Matriz()
                >>> m.get_final_result(res)
                [(' 0,3', '1,3'), (' 1,3', '2,2'), (' 1,4', '2,3'), (' 2,3', '4,0'), (' 4,0', '4,3'), (' 0,4', '4,4')]
                """
        result.sort()
        final_result = []
        for item in result:
            element = item[0].split(";")[1], item[0].split(";")[0]
            if not element in final_result:
                final_result.append(element)
        set(final_result)
        return final_result

    def element_to_search(self, matriz, element, pos_x, pos_y):
        """
                This method search one value on the array and return position x and y on the array
                >>> matriz=[[43,32,55,66,1],
                ...     [32,53,64,66,12],
                ...     [3,9,66,12,29],
                ...     [85,88,32,25,48],
                ...     [12,14,13,12,1]]
                >>> m = Matriz()
                >>> m.element_to_search(matriz,32,0,0)
                ['0,1; 0,0', '1,0; 0,0', '3,2; 0,0']
                """
        pos_inicial = "%s,%s" % (pos_x, pos_y)
        result = []
        self.num_list.append(element)
        while (pos_x <= 4):
            if pos_x == 4 and pos_y == 4:
                break
            if pos_y >= 4:
                pos_x += 1
                pos_y = 0
            else:
                pos_y += 1
            if matriz[pos_x][pos_y] == element:
                result.append("%s,%s; %s" % (pos_x, pos_y, pos_inicial))
        if result:
            return result
        else:
            return False


import doctest
doctest.testmod()
Matriz().iniciar()