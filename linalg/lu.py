class LUDecomposition():
    """ LU Decomposition - https://en.wikipedia.org/wiki/LU_decomposition

    Note: Implemented for revising basics, not for operational usage.
    Please refer to scipy.linalg.lu function for operational use
    """

    def __init__(self, A):
        """ Calculates LU Decomposition

        Args:
            A: input matrix for LU calculation. Input matrix must be square
        Returns:
            L: Lower triangular matrix
            U: Upper triangular matrix
        """
        self.A = A
        self.n = len(A)

    def decompose(self):
        self.L = [[0.0] * self.n for i in range(self.n)]
        self.U = [[0.0] * self.n for i in range(self.n)]

        P = self._set_pivot_matrix()
        PA = self._multiply_matrices(P)

        for j in range(len(self.A)):
            pass

    def _set_pivot_matrix(self):
        """ Returns pivot matrix for A
        """
        i_mat = [[float(i == j) for i in range(self.n)] for j in range(self.n)]
        print(i_mat)
        for j in range(self.n):
            row = max(range(j, self.n), key=lambda i: abs(self.A[i][j]))
            if j != row:
                i_mat[j], i_mat[row] = i_mat[row], i_mat[j]
        return i_mat

    def _multiply_matrices(self, P):
        """ Multiply matrices and return the result
        """
        tuple_N = zip(*self.A)
        return [
            [sum(el_m * el_n for el_m, el_n in zip(
                row_m, col_n)) for col_n in tuple_N] for row_m in P]

    def _is_square(self):
        """ Checks if input matrix is square, returns true if it is.
        """
        return all(len(row) == len(self.A) for row in self.A)
