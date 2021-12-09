from typing import List, Tuple, Union

from .exceptions import NotSquareException, ValidationError

Number = Union[int, float]


class Matrix:
    def __init__(self, rows: List[List[Number]]) -> None:
        self.rows = rows
        self._validate()

    def __str__(self) -> str:
        return str(self.rows)

    def __round__(self, ndigits: int = None) -> "Matrix":
        temp = self._get_zero_matrix()
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                temp[i][j] = round(self.rows[i][j], ndigits)
        return Matrix(temp)

    def __add__(self, other: "Matrix") -> "Matrix":
        temp = self._get_zero_matrix()
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                temp[i][j] = self.rows[i][j] + other.rows[i][j]
        return Matrix(temp)

    def __sub__(self, other: "Matrix") -> "Matrix":
        temp = self._get_zero_matrix()
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                temp[i][j] = self.rows[i][j] - other.rows[i][j]
        return Matrix(temp)

    def __mul__(self, other: Union["Matrix", Number]) -> "Matrix":
        if isinstance(other, (int, float)):
            temp = self._get_zero_matrix()
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    temp[i][j] = self.rows[i][j] * other
        else:
            temp = self._get_zero_matrix_with_size(self.num_rows, other.num_cols)
            for i in range(self.num_rows):
                for j in range(other.num_cols):
                    for k in range(self.num_cols):
                        temp[i][j] += self.rows[i][k] * other.rows[k][j]
        return Matrix(temp)

    def __eq__(self, other: "Matrix") -> bool:
        return self.rows == other.rows

    def __neg__(self) -> "Matrix":
        return self * -1

    def _validate(self) -> None:
        self.num_rows = len(self.rows)
        num_cols = len(self.rows[0])
        if all([len(element) == num_cols for element in self.rows]):
            self.num_cols = num_cols
        else:
            raise ValidationError("All rows must have equal number of columns")

    def _get_zero_matrix_with_size(self, rows: int, cols: int) -> List[List[Number]]:
        return [[0 for _ in range(cols)] for _ in range(rows)]

    def _get_zero_matrix(self) -> List[List[Number]]:
        return self._get_zero_matrix_with_size(self.num_rows, self.num_cols)

    def _get_diagonal_and_non_diagonal_entries(
        self,
    ) -> Tuple[List[Number], List[Number]]:
        if not self.is_square_matrix():
            raise NotSquareException(
                "Cannot check for diagonal matrix because it is not a square matrix"
            )
        diagonal = []
        non_diagonal = []
        [
            diagonal.append(self.rows[i][j])
            if i == j
            else non_diagonal.append(self.rows[i][j])
            for i in range(self.num_rows)
            for j in range(self.num_cols)
        ]
        return diagonal, non_diagonal

    def prettify(self) -> None:
        print("\n".join([str(row) for row in self.rows]))

    def transpose(self) -> "Matrix":
        temp = self._get_zero_matrix_with_size(self.num_cols, self.num_rows)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                temp[j][i] = self.rows[i][j]
        return Matrix(temp)

    def is_row_matrix(self) -> bool:
        return self.num_rows == 1

    def is_column_matrix(self) -> bool:
        return self.num_cols == 1

    def is_rectangular_matrix(self) -> bool:
        return self.num_rows != self.num_cols

    def is_square_matrix(self) -> bool:
        return self.num_rows == self.num_cols

    def is_zero_matrix(self) -> bool:
        return self._get_zero_matrix() == self.rows

    def is_symmetric_matrix(self) -> bool:
        return self == self.transpose()

    def is_skew_symmetric_matrix(self) -> bool:
        return -self == self.transpose()

    def is_diagonal_matrix(self) -> bool:
        diagonal, non_diagonal = self._get_diagonal_and_non_diagonal_entries()
        return all(element == 0 for element in non_diagonal) and any(diagonal)

    def is_scalar_matrix(self) -> bool:
        diagonal, non_diagonal = self._get_diagonal_and_non_diagonal_entries()
        return all(element == 0 for element in non_diagonal) and all(
            element != 0 and element == diagonal[0] for element in diagonal
        )

    def is_identity_matrix(self) -> bool:
        diagonal, non_diagonal = self._get_diagonal_and_non_diagonal_entries()
        return all(element == 0 for element in non_diagonal) and all(
            element == 1 for element in diagonal
        )
