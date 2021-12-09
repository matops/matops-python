import pytest
from matops.exceptions import NotSquareException, ValidationError
from matops.matrix import Matrix


def test_valid_matrix_1():
    m = Matrix(
        [
            [1, 2],
            [3, 4],
        ]
    )
    assert m.num_rows == 2
    assert m.num_cols == 2


def test_valid_matrix_2():
    m = Matrix(
        [
            [1, 2],
            [3, 4],
            [5, 6],
        ]
    )
    assert m.num_rows == 3
    assert m.num_cols == 2


def test_valid_matrix_3():
    m = Matrix(
        [
            [1, 2, 3],
            [4, 5, 6],
        ]
    )
    assert m.num_rows == 2
    assert m.num_cols == 3


def test_valid_matrix_4():
    m = Matrix(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    )
    assert m.num_rows == 3
    assert m.num_cols == 3


def test_invalid_matrix_1():
    with pytest.raises(ValidationError):
        m = Matrix(
            [
                [1],
                [3, 4],
            ]
        )


def test_invalid_matrix_2():
    with pytest.raises(ValidationError):
        m = Matrix(
            [
                [1, 2],
                [],
                [5, 6],
            ]
        )


def test_invalid_matrix_3():
    with pytest.raises(ValidationError):
        m = Matrix(
            [
                [1, 2, 3],
                [5, 6],
            ]
        )


def test_invalid_matrix_4():
    with pytest.raises(ValidationError):
        m = Matrix(
            [
                [1, 3],
                [4, 5, 6],
                [7, 8, 9],
            ]
        )


def test_add_1():
    m1 = Matrix(
        [
            [1, 2],
            [3, 4],
        ]
    )
    m2 = Matrix(
        [
            [5, 6],
            [7, 8],
        ]
    )
    assert m1 + m2 == Matrix([[6, 8], [10, 12]])


def test_sub_1():
    m1 = Matrix(
        [
            [1, 2],
            [3, 4],
        ]
    )
    m2 = Matrix(
        [
            [5, 6],
            [7, 8],
        ]
    )
    assert m1 - m2 == Matrix([[-4, -4], [-4, -4]])


def test_mul_1():
    m1 = Matrix(
        [
            [4, 0],
            [1, -9],
        ]
    )
    assert m1 * 2, Matrix([[8, 0], [2, -18]])


def test_mul_2():
    m1 = Matrix(
        [
            [1, 2, 3],
            [4, 5, 6],
        ]
    )
    m2 = Matrix(
        [
            [7, 8],
            [9, 10],
            [11, 12],
        ]
    )
    assert m1 * m2 == Matrix([[58, 64], [139, 154]])


def test_mul_3():
    m1 = Matrix(
        [
            [3, 4, 2],
        ]
    )
    m2 = Matrix(
        [
            [13, 9, 7, 15],
            [8, 7, 4, 6],
            [6, 4, 0, 3],
        ]
    )
    assert m1 * m2 == Matrix([[83, 63, 37, 75]])


def test_mul_4():
    m1 = Matrix(
        [
            [1, 2, 3],
        ]
    )
    m2 = Matrix(
        [
            [4],
            [5],
            [6],
        ]
    )
    assert m1 * m2 == Matrix([[32]])


def test_mul_5():
    m1 = Matrix(
        [
            [4],
            [5],
            [6],
        ]
    )
    m2 = Matrix(
        [
            [1, 2, 3],
        ]
    )
    assert m1 * m2 == Matrix([[4, 8, 12], [5, 10, 15], [6, 12, 18]])


def test_eq_1():
    m1 = Matrix(
        [
            [1, 2],
            [3, 4],
        ]
    )
    m2 = Matrix(
        [
            [1, 2],
            [3, 4],
        ]
    )
    assert m1 == m2


def test_eq_2():
    m1 = Matrix(
        [
            [1, 2],
            [3, 4],
        ]
    )
    m2 = Matrix(
        [
            [1, 2],
            [3, 5],
        ]
    )
    assert m1 != m2


def test_neg_1():
    m = Matrix(
        [
            [1, -2],
            [-3, 4],
        ]
    )
    assert -m == Matrix([[-1, 2], [3, -4]])


def test_transpose_1():
    m = Matrix(
        [
            [1, 2],
            [3, 4],
        ]
    )
    assert m.transpose() == Matrix([[1, 3], [2, 4]])


def test_row_matrix_1():
    m = Matrix(
        [
            [1, 2],
        ]
    )
    assert m.is_row_matrix()


def test_row_matrix_2():
    m = Matrix(
        [
            [1],
            [2],
        ]
    )
    assert not m.is_row_matrix()


def test_column_matrix_1():
    m = Matrix(
        [
            [1],
            [2],
        ]
    )
    assert m.is_column_matrix()


def test_column_matrix_2():
    m = Matrix(
        [
            [1, 2],
        ]
    )
    assert not m.is_column_matrix()


def test_rectangular_matrix_1():
    m = Matrix(
        [
            [1, 2],
        ]
    )
    assert m.is_rectangular_matrix()


def test_rectangular_matrix_2():
    m = Matrix(
        [
            [1, 2],
            [3, 4],
        ]
    )
    assert not m.is_rectangular_matrix()


def test_square_matrix_1():
    m = Matrix(
        [
            [1, 2],
            [3, 4],
        ]
    )
    assert m.is_square_matrix()


def test_square_matrix_2():
    m = Matrix(
        [
            [1, 2],
        ]
    )
    assert not m.is_square_matrix()


def test_zero_matrix_1():
    m = Matrix(
        [
            [0, 0],
            [0, 0],
        ]
    )
    assert m.is_zero_matrix()


def test_zero_matrix_2():
    m = Matrix(
        [
            [0],
            [0],
        ]
    )
    assert m.is_zero_matrix()


def test_zero_matrix_3():
    m = Matrix(
        [
            [1, 0],
            [0, 0],
        ]
    )
    assert not m.is_zero_matrix()


def test_symmetric_matrix_1():
    m = Matrix(
        [
            [3, 2],
            [2, 4],
        ]
    )
    assert m.is_symmetric_matrix()


def test_symmetric_matrix_2():
    m = Matrix(
        [
            [3, 2],
            [-2, 4],
        ]
    )
    assert not m.is_symmetric_matrix()


def test_skew_symmetric_matrix_1():
    m = Matrix(
        [
            [0, 2, 3],
            [-2, 0, 1],
            [-3, -1, 0],
        ]
    )
    assert m.is_skew_symmetric_matrix()


def test_skew_symmetric_matrix_2():
    m = Matrix(
        [
            [3, 2],
            [2, 4],
        ]
    )
    assert not m.is_skew_symmetric_matrix()


def test_diagonal_matrix_1():
    m = Matrix(
        [
            [1, 0, 0],
            [0, 2, 0],
            [0, 0, 3],
        ]
    )
    assert m.is_diagonal_matrix()


def test_diagonal_matrix_2():
    m = Matrix(
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 3],
        ]
    )
    assert m.is_diagonal_matrix()


def test_diagonal_matrix_3():
    m = Matrix(
        [
            [0, 0],
            [0, 1],
        ]
    )
    assert m.is_diagonal_matrix()


def test_diagonal_matrix_4():
    m = Matrix(
        [
            [0, 0],
            [1, 0],
        ]
    )
    assert not m.is_diagonal_matrix()


def test_diagonal_matrix_5():
    m = Matrix(
        [
            [0],
        ]
    )
    assert not m.is_diagonal_matrix()


def test_diagonal_matrix_6():
    with pytest.raises(NotSquareException):
        m = Matrix(
            [
                [1, 2, 3],
                [4, 5, 6],
            ]
        )
        m.is_diagonal_matrix()


def test_scalar_matrix_1():
    m = Matrix(
        [
            [2, 0],
            [0, 2],
        ]
    )
    assert m.is_scalar_matrix()


def test_scalar_matrix_2():
    m = Matrix(
        [
            [2],
        ]
    )
    assert m.is_scalar_matrix()


def test_scalar_matrix_3():
    m = Matrix(
        [
            [1, 0],
            [0, 1],
        ]
    )
    assert m.is_scalar_matrix()


def test_scalar_matrix_4():
    m = Matrix(
        [
            [1, 0],
            [0, 2],
        ]
    )
    assert not m.is_scalar_matrix()


def test_scalar_matrix_5():
    m = Matrix(
        [
            [0, 0],
            [0, 1],
        ]
    )
    assert not m.is_scalar_matrix()


def test_scalar_matrix_6():
    m = Matrix(
        [
            [0, 0],
            [0, 0],
        ]
    )
    assert not m.is_scalar_matrix()


def test_identity_matrix_1():
    m = Matrix(
        [
            [1, 0],
            [0, 1],
        ]
    )
    assert m.is_identity_matrix()


def test_identity_matrix_2():
    m = Matrix(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
    )
    assert m.is_identity_matrix()


def test_identity_matrix_3():
    m = Matrix(
        [
            [0, 0],
            [0, 1],
        ]
    )
    assert not m.is_identity_matrix()


def test_proof_1():
    m1 = Matrix(
        [
            [1, -2],
            [3, 4],
        ]
    )
    m2 = Matrix(
        [
            [0, 7],
            [-3, 8],
        ]
    )

    assert (m1 * m2).transpose() == m2.transpose() * m1.transpose()


def test_round_1():
    m1 = Matrix(
        [
            [1.1123, -2.982143],
            [3.21043, 4.4253],
        ]
    )
    assert round(m1) == Matrix([[1, -3], [3, 4]])


def test_round_2():
    m1 = Matrix(
        [
            [1.1123, -2.982143],
            [3.21043, 4.4253],
        ]
    )
    assert round(m1, 2) == Matrix([[1.11, -2.98], [3.21, 4.43]])
