## =================================================================================================
## Python 3.6+
## =================================================================================================
import Example as ex_cy
import numpy as np

## -------------------------------------------------------------------------------------------------
def main():
    x = 3
    A = np.array([[1, 2 ,3], [4, 5, 6]], dtype=np.int64)
    result = ex_cy.cython_function(A, x)
    print(f'cython_function(A, x) = {result}')
    print(f'np.sum(A) * x         = {np.sum(A) * x}')


## =================================================================================================
if __name__ == '__main__':
    main()