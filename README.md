## What is `matops`?

`matops` is a lightweight pure Python package to do basic matrix operations like addition, multiplication etc. as well as to check some properties of matrices e.g. whether a matrix is scalar or not.

## What is a matrix?

In mathematics, a matrix is a set of numbers arranged in rows and columns so as to form a rectangular array. The numbers are called the elements, or entries, of the matrix.

## Installation:

You can use `pip` to install `matops` with the following command:

```
pip install matops
```

## Examples:

### Addition:

```py
from matops import Matrix

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

m3 = m1 + m2

print(m3)
```

```
[[6, 8], [10, 12]]
```

You can use `prettify()` method to print it in a more readable format.

```py
m3.prettify()
```

```
[6, 8]
[10, 12]
```

### Transpose:

```py
from matops import Matrix

m = Matrix(
    [
        [1, 2],
        [3, 4],
    ]
)

m.transpose().prettify()

```

```
[1, 3]
[2, 4]
```

## The `Matrix` class

The `Matrix` class is at the heart of `matops`. You can import it as follows to use it in your code:

```py
from matops import Matrix
```

## Instantiation

```py
m = Matrix(
    [
        [1, 2],
        [3, 4],
    ]
)
```

## Supported operations and methods:

### Addition

```py
from matops import Matrix

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

m3 = m1 + m2

m3.prettify()
```

```
[6, 8]
[10, 12]
```

### Subtraction

```py
from matops import Matrix

m1 = Matrix(
    [
        [7, 9],
        [1, 5],
    ]
)

m2 = Matrix(
    [
        [3, 1],
        [0, 2],
    ]
)

m3 = m1 - m2

m3.prettify()
```

```
[4, 8]
[1, 3]
```

### Multiplication

Multiplication can be performed either with an `int`, `float` or another `Matrix`.

#### With an `int` or a `float`

When multiplying a `Matrix` with an `int` or a `float`, make sure that `Matrix` is on the left side of the `*` operator.

```py
from matops import Matrix

m1 = Matrix(
    [
        [4, 0],
        [1, -9],
    ]
)

m2 = m1 * 2

m2.prettify()
```

```
[8, 0]
[2, -18]
```

#### With another `Matrix`

When multiplying a `Matrix` with another `Matrix`, make sure that the `Matrix` on the left side of the `*` operator has the same number of columns as the rows of the `Matrix` on the right side. If that's not the case, you might get an error.

```py
from matops import Matrix

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

m3 = m1 * m2

m3.prettify()
```

```
[83, 63, 37, 75]
```

### Negative

Negative of a `Matrix` basically flips the sign of every element from `+` to `-` and vice versa. It is essentially the same as multiplying the `Matrix` by `-1`.

```py
from matops import Matrix

m1 = Matrix(
    [
        [1, -2],
        [-3, 4],
    ]
)

m2 = -m1

m2.prettify()
```

```
[-1, 2]
[3, -4]
```

### Transpose

The transpose of a matrix is an operator which flips a matrix over its diagonal. We essentially convert rows into columns (or columns into rows). The `.transpose()` method can be used to find the transpose of a `Matrix`.

```py
from matops import Matrix

m = Matrix(
    [
        [1, 2],
        [3, 4],
    ]
)

m.transpose().prettify()
```

```
[1, 3]
[2, 4]
```

### Equality

We can check whether two `Matrix` are equal or not using `==` and `!=` operators.

```py
from matops import Matrix

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

m3 = Matrix(
    [
        [1, 0],
        [0, 1],
    ]
)

print(m1 == m2)
print(m1 == m3)
print(m1 != m3)
```

```
True
False
True
```

### Row Matrix

If a matrix has only one row, it's called a row matrix. We can use `.is_row_matrix()` method to check whether a `Matrix` is a row matrix or not.

```py
from matops import Matrix

m1 = Matrix(
    [
        [1, 2],
    ]
)

m2 = Matrix(
    [
        [1],
        [2],
    ]
)

print(m1.is_row_matrix())
print(m2.is_row_matrix())
```

```
True
False
```

### Column Matrix

If a matrix has only one column, it's called a column matrix. We can use `.is_column_matrix()` method to check whether a `Matrix` is a column matrix or not.

```py
from matops import Matrix

m1 = Matrix(
    [
        [1],
        [2],
    ]
)

m2 = Matrix(
    [
        [1, 2],
    ]
)

print(m1.is_column_matrix())
print(m2.is_column_matrix())
```

```
True
False
```

In this case, `m1` is a column matrix while `m2` is not.

### Rectangular Matrix

If the number of rows in a matrix are not equal to the number of columns, that matrix is callled a rectangular matrix. We can use `.is_rectangular_matrix()` method to check whether a `Matrix` is a rectangular matrix or not.

```py
from matops import Matrix

m = Matrix(
    [
        [1],
        [2],
    ]
)

print(m.is_rectangular_matrix())
```

```
True
```

In this case `m` is a rectangular matrix because the number of rows (2) are not equal to the number of columns (1).

### Square Matrix

As opposed to a rectangular matrix, if the number of rows in a matrix are equal to the number of columns, that matrix is callled a square matrix. We can use `.is_square_matrix()` method to check whether a `Matrix` is a square matrix or not.

```py
from matops import Matrix

m = Matrix(
    [
        [1, 2],
        [3, 4],
    ]
)

print(m.is_square_matrix())
```

```
True
```

In this case, `m` is a square matrix because the number of rows (2) are equal to the number of columns (2).

### Zero Matrix

If all the elements of a matrix are zero, it is callled zero matrix. We can use `.is_zero_matrix()` method to check whether a `Matrix` is a zero matrix or not.

```py
from matops import Matrix

m = Matrix(
    [
        [0, 0],
        [0, 0],
    ]
)

print(m.is_zero_matrix())
```

```
True
```

In this case, `m` is a zero matrix because all of its elements are equal to zero.

### Symmetric Matrix

If the transpose of a matrix is equal to the original matrix itself, then that matrix is called a symmetric matrix. We can use `.is_symmetric_matrix()` method to check whether a `Matrix` is a symmetric matrix or not. Consider the following example:

```py
from matops import Matrix

m = Matrix(
    [
        [3, 2],
        [2, 4],
    ]
)

m.transpose().prettify()
```

```
[3, 2]
[2, 4]
```

As you can see we are printing the transpose of the matrix `m` but it is again equal to `m` itself. So `m` is a symmetric matrix and we can verify that as follows:

```py
from matops import Matrix

m = Matrix(
    [
        [3, 2],
        [2, 4],
    ]
)

print(m.is_symmetric_matrix())
```

```
True
```

### Skew-symmetric Matrix

If the transpose of a matrix is equal to the negative of the original matrix, then that matrix is called a skew-symmetric matrix. We can use `.is_skew_symmetric_matrix()` method to check whether a `Matrix` is a skew-symmetric matrix or not. Consider the following example:

```py
from matops import Matrix

m = Matrix(
    [
        [0, 2, 3],
        [-2, 0, 1],
        [-3, -1, 0],
    ]
)

m.transpose().prettify()
```

```
[0, -2, -3]
[2, 0, -1]
[3, 1, 0]
```

If you look closely, you'll see that the transpose of matrix `m` is actually negative of the matrix `m`. So `m` is a skew-symmetric matrix and we can verify that as follows:

```py
from matops import Matrix

m = Matrix(
    [
        [0, 2, 3],
        [-2, 0, 1],
        [-3, -1, 0],
    ]
)

print(m.is_skew_symmetric_matrix())
```

```
True
```

### Diagonal Matrix

A diagonal matrix is a square matrix whose:

- Off-diagonal entries are all equal to zero.
- At least one of the diagonal entries is non-zero

We can use `is_diagonal_matrix()` method to check whether a `Matrix` is a diagonal matrix or not.

```py
from matops import Matrix

m = Matrix(
    [
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 3],
    ]
)

print(m.is_diagonal_matrix())
```

```
True
```

If any off-diagonal element is non-zero, it won't be a diagonal matrix.

```py
from matops import Matrix

m = Matrix(
    [
        [1, 1, 0],
        [0, 2, 0],
        [0, 0, 3],
    ]
)

print(m.is_diagonal_matrix())
```

```
False
```

If all the diagonal entries are zero too then it won't be a diagonal matrix either. Instead, it will become a zero matrix.

```py
from matops import Matrix

m = Matrix(
    [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
)

print(m.is_diagonal_matrix())
```

```
False
```

### Scalar Matrix

A diagonal matrix is called a scalar matrix if all the diagonal entries are equal and non-zero. We can use `is_scalar_matrix()` method to check whether a `Matrix` is a scalar matrix or not.

```py
from matops import Matrix

m = Matrix(
    [
        [7, 0, 0],
        [0, 7, 0],
        [0, 0, 7],
    ]
)

print(m.is_scalar_matrix())
```

```
True
```

If any off-diagonal element is non-zero, it won't be a diagonal matrix and hence it won't be a scalar matrix either.

```py
from matops import Matrix

m = Matrix(
    [
        [7, 1, 0],
        [0, 7, 0],
        [0, 0, 7],
    ]
)

print(m.is_scalar_matrix())
```

```
False
```

If all the diagonal entries are not equal and non-zero then it won't be a scalar matrix.

```py
from matops import Matrix

m = Matrix(
    [
        [1, 0, 0],
        [0, 7, 0],
        [0, 0, 7],
    ]
)

print(m.is_scalar_matrix())
```

```
False
```

### Identity Matrix

A scalar matrix is called an identity matrix if all the diagonal entries are equal to `1`. We can use `is_identity_matrix()` method to check whether a `Matrix` is an identity matrix or not.

```py
from matops import Matrix

m = Matrix(
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]
)

print(m.is_identity_matrix())
```

```
True
```
