#Задание 1



class Matrix:
    def __init__(self, list):
        self.list = list

    def __add__(self, other):
        matr = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(self.list)):
            for j in range(len(self.list[i])):
                matr[i][j] = self.list[i][j] + other.list[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.list]))


my_matrix_1 = Matrix([[3, 5, 32],[2, 4, 6],[-1, 64, -8]])

my_matrix_2 = Matrix([[1, 1, 1], [1, 1, 1],[1, 1, 1]])

my_matrix_3 = my_matrix_1 + my_matrix_2

print(my_matrix_3)
print(my_matrix_1)