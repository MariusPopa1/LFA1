import random
from lab1.grammar import Grammar
from lab1.finiteAutomaton import FiniteAutomata
from colorama import Fore


def generate_valid(grammar, strings):
    valid = []

    def generate_string(remaining, transition):
        if not remaining:
            return '', transition
        for index, char in enumerate(remaining):
            if char.isupper():
                current = char
                break
        else:
            return remaining, transition

        if current in grammar.terminal:
            current_str, transition = generate_string(remaining[index + 1:], transition)
            return current + current_str, transition
        else:
            product = random.choice(grammar.products[current])
            new_remaining = ''.join(reversed(product)) + remaining[index + 1:]
            transition.append((current, product))
            return generate_string(new_remaining, transition)

    for _ in range(strings):
        string, transitions = generate_string('S', [('S', 'S')])
        valid.append((string[::-1], transitions))

    return valid


def run():
    grammar = Grammar()

    print("Strings generated:")
    valid = generate_valid(grammar, 5)

    for result, transitions in valid:
        for transition in transitions:
            print(f"-> {transition[1]}", end=' ')
        print(f"-> {result} \n")

    check_strings = ["ab", "baba", "aaba", "cca", "aabcab"]
    finite_automata = FiniteAutomata(grammar)
    for input_str in check_strings:
        if finite_automata.check(input_str):
            print(Fore.GREEN, f" '{input_str}' is possible")
        else:
            print(Fore.RED, f" '{input_str}' is impossible")


run()
