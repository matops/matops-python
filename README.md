`matops` is a Python package to perform basic matrix operations.

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

### List of available methods in `Matrix` class:

- `prettify()`
- `transpose()`
- `is_row_matrix()`
- `is_column_matrix()`
- `is_rectangular_matrix()`
- `is_square_matrix()`
- `is_zero_matrix()`
- `is_symmetric_matrix()`
- `is_skew_symmetric_matrix()`
- `is_diagonal_matrix()`
- `is_scalar_matrix()`
- `is_identity_matrix()`
