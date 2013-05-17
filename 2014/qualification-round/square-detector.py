#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class QuizzesParser:
    def __init__(self, src):
        self.src = src
        with open(src) as f:
            self.raw = f.read().splitlines()
        self.amount = int(self.raw[0])
    def quizpool(self):
        cur_line = 1
        for i in range(self.amount):
            offset = int(self.raw[cur_line])
            prev_line = cur_line
            cur_line = prev_line + offset + 1
            yield self.raw[prev_line:cur_line]

class QuizSolver:
    def __init__(self, quiz):
        self.quiz = quiz
    def solve(self):
        N = int(self.quiz[0])
        started = False
        start_line = -1
        mask = list()
        length = 0
        for i in range(N):
            line = self.quiz[i]
            if not started and '#' not in line:
                continue
            if not started:
                if line.count('#') > N - i:
                    return 'NO'
                for j in range(len(line)):
                    if len(line) > 2 and j > 0 and j < len(line) - 1 \
                            and line[j] != '#' and '#' in line[:j] \
                            and '#' in line[j:]:
                        return 'NO'
                    mask.append(1 if line[j] == '#' else 0)
                start_line = i
                length = line.count('#')
                started = True
                continue
            if i - start_line >= length:
                if '#' in line:
                    return 'NO'
                else:
                    continue
            mask_pair = list()
            for j in range(len(line)):
                mask_pair.append(1 if line[j] == '#' else 0)
            if any(map(lambda x, y: x ^ y, mask, mask_pair)):
                return 'NO'
        return 'YES'

def main():
    qsparser = QuizzesParser(sys.argv[1])
    with open(sys.argv[2], 'w') as f:
        for i, quiz in enumerate(qsparser.quizpool()):
            qsolver = QuizSolver(quiz)
            f.write('Case #{num}: {ans}\n'.format(num=i+1, ans=qsolver.solve()))

if __name__ == '__main__':
    main()
