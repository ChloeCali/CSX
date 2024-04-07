import MatrixLover


def main():


    #creating matrices
    trixie = MatrixLover.Matrix(3,4)                                
    alice = MatrixLover.Matrix(3,4)
    chloe = MatrixLover.Matrix(3,2)
    christian = MatrixLover.Matrix(2,1)


     #row 1
    MatrixLover.Matrix.set(christian, 0, 0, 2)

    #row 2
    MatrixLover.Matrix.set(christian, 1, 0, 4)

    

    #row 1
    MatrixLover.Matrix.set(chloe, 0, 0, 1)
    MatrixLover.Matrix.set(chloe, 0, 1, 2)

    #row 2
    MatrixLover.Matrix.set(chloe, 1, 0, 3)
    MatrixLover.Matrix.set(chloe, 1, 1, 4)

    #row 3
    MatrixLover.Matrix.set(chloe, 2, 0, 5)
    MatrixLover.Matrix.set(chloe, 2, 1, 1)
    

    #times function test
    multiplied = christian.times(chloe)
    print("product of christian and chloe:")
    multiplied.print()
    





if __name__ == "__main__":
    main()

'''
    110
    220
    123

    rref check, if there is a row of zeros, then no inverse

    '''