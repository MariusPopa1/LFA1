""""
Variant 21:
VN={S, B, C, D},
VT={a, b, c},
P={
    S → aB
    B → bS
    B → aC
    B → b
    C → bD
    D → a
    D → bC
    D → cS
}
"""
class Grammar:
    def __init__(self):
        self.non_terminal = {'S', 'B', 'C', 'D'}
        self.terminal = {'a', 'b', 'c'}
        self.products = {
            'S': ['aB'],
            'B': ['bS', 'aC', 'b'],
            'C': ['bD'],
            'D': ['a', 'bC', 'cS']
        }
