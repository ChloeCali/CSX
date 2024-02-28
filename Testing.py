'''
Created on Dec 1, 2023

@author: CCaliboso24
'''

import MatrixLover

def main():

    trixie = MatrixLover.Matrix(3,4)
    alice = MatrixLover.Matrix(3,4)
    chloe = MatrixLover.Matrix(4,3)
    christian = MatrixLover.Matrix(3,3)
    
    MatrixLover.Matrix.randomize(trixie,0,9)
    MatrixLover.Matrix.randomize(alice,0,9)
    MatrixLover.Matrix.randomize(chloe,0,9)
    MatrixLover.Matrix.randomize(christian,0,9)

    print("trixie:")
    trixie.print()
    print("alice:")
    alice.print()
    print("chloe:")
    chloe.print()

    added = trixie.plus(alice)
    print("sum of trixie and alice:")
    added.print()

    multiplied = trixie.times(chloe)
    print("product of trixie and chloe:")
    multiplied.print()

    print("chloe with row 1 multiplied by 5:")
    MatrixLover.Matrix.scalarTimesRow(chloe,0,5)
    chloe.print()

    print("chloe with row 1 switched with row 2:")
    MatrixLover.Matrix.switchRows(chloe,0,1)
    chloe.print()

    print("chloe with row 1 multiplied by 5 added to row 2:")
    MatrixLover.Matrix.linearCombRows(chloe,5,0,1)
    chloe.print()

    alice = MatrixLover.Matrix(3,6)
    MatrixLover.Matrix.randomize(alice,0,9)

    alice.set(0,0,0)
    alice.set(1,0,0)
    alice.set(2,0,0)

    print("alice:")
    alice.print()

    print("alice RREF:")
    MatrixLover.Matrix.rowreduce(alice)
    alice.print()

    print("christian:")
    christian.print()

    print("christian inverted:")
    inverted = MatrixLover.Matrix.invert(christian)
    inverted.print()



if __name__ == "__main__":
    main()