class FiniteAutomata:
    def __init__(self, grammar):
        self.alphabet = {}
        self.state = {}
        self.transition = {}
        self.init_state = None
        self.final_state = {}

        self.convert_grammar(grammar)

    def convert_grammar(self, grammar):
        self.alphabet = grammar.terminal
        self.state = grammar.non_terminal
        for symbol in grammar.products:
            for product in grammar.products[symbol]:
                if len(product) == 1:
                    self.transition[(symbol, product)] = 'final'
                else:
                    self.transition[(symbol, product[0])] = product[1]

        self.init_state = 'S'
        self.final_state = {symbol for symbol in grammar.products if symbol.isupper()}

    def check(self, input_string):
        current_state = self.init_state
        for char in input_string:
            if not (current_state, char) in self.transition:
                return False
            current_state = self.transition[(current_state, char)]

        return True
