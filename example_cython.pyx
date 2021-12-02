## =================================================================================================
## Example cython file
## =================================================================================================
## Python imports
import numpy as np
np.import_array()

## Cython imports
cimport cython
cimport numpy as np

## Define types
ctypedef np.int64_t INT64_t

## -------------------------------------------------------------------------------------------------
@cython.boundscheck(False)
@cython.wraparound(False)
def cython_function(np.ndarray[INT64_t, ndim=2] A, INT64_t x):
    cdef INT64_t b, h, w

    print('This function is implemented in cython!')

    h = A.shape[0]
    w = A.shape[1]
    b = 0

    for i in range(h):
        for j in range(w):
            b = b + A[i, j] * x

    return b