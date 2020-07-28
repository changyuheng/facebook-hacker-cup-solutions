#!/usr/bin/env python

import os
import sys
from typing import List


class Case():

    def __init__(self, case_idx: int):
        self.idx: int = case_idx
        self.n: int = int(input())
        self.incomings: List[str] = list(input())
        self.outgoings: List[str] = list(input())
        self.table: List[List[str]] = list()

    def left(self, row_idx: int):
        column_idx: int
        for column_idx in range(row_idx - 1, -1, -1):
            if self.table[row_idx][column_idx+1] != "Y":
                continue
            if self.outgoings[column_idx+1] != "Y":
                continue
            if self.incomings[column_idx] != "Y":
                continue
            self.table[row_idx][column_idx] = "Y"

    def right(self, row_idx: int):
        column_idx: int
        for column_idx in range(row_idx + 1, self.n):
            if self.table[row_idx][column_idx-1] != "Y":
                continue
            if self.outgoings[column_idx-1] != "Y":
                continue
            if self.incomings[column_idx] != "Y":
                continue
            self.table[row_idx][column_idx] = "Y"

    def solve(self) -> str:
        row_idx: int
        for row_idx in range(self.n):
            self.table.append(["N"] * row_idx + ["Y"] + ["N"] * (self.n - row_idx - 1))
        for row_idx in range(self.n):
            self.left(row_idx)
            self.right(row_idx)
        row: List[str]
        return os.linesep.join([f"Case #{self.idx}:"] + ["".join(row) for row in self.table])


def main() -> int:
    i: int
    for i in range(int(input())):
        print(Case(i+1).solve())
    return os.EX_OK


if __name__ == '__main__':
    sys.exit(main())
