import time

from rich import print
from rich.console import Console
from rich.console import Console
from rich.theme import Theme
from rich.progress import Progress
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})
console = Console(theme=custom_theme)


class Machine(object):
    def __init__(self, transitions, input_alphabet, output_alphabet, startstate, states):
        self.states = states
        self.inalphabet = input_alphabet
        self.outalphabet = output_alphabet
        self.startstate = startstate
        self.transitions = transitions
        self.currstate = startstate
        self.final_states = [x for x in self.states if x.is_final]

    def find_transition_by_state(self, state):
        return [x for x in self.transitions if state == x.src]

    def find_transition_by_inputstate(self, state, char):
        return [x for x in self.transitions if state == x.src and (x.in_symbol == char or x.in_symbol == 'λ')]

    def find_lambda_transition(self, state):
        return [x for x in self.transitions if state == x.src and x.in_symbol == 'λ']

    def parse_input(self, string):
        state = self.currstate
        char = string[0]
        trans = self.find_transition_by_inputstate(state, char)
        if len(string) == 1:
            if len(trans) == 0:
                print(' /end_of_states')
            else:
                for tran in trans:
                    if tran.in_symbol != 'λ':
                        # console.print(tran.out_symbol, style='blue on white', end='')
                        # self.currstate = tran.dest
                        # self.parse_input(string)
                        # if srting has ended but we have lambda erxpression yet
                        trs = self.find_lambda_transition(tran.dest)
                        if len(trs) != 0:
                            for tr in trs:
                                console.print(tr.out_symbol, style='warning')
                                self.currstate = tran.dest
                                self.parse_input(string)
                        else:
                            console.print(tran.out_symbol + ' /end_of_string', style='warning')
                    else:
                        console.print('λ', style='blue on white', end='')
                        self.currstate = tran.dest
                        self.parse_input(string)
        else:
            if len(trans) == 0:
                print(' /end_of_states')
            else:
                for tran in trans:
                    if tran.in_symbol != 'λ':
                        console.print(tran.out_symbol, style='warning', end='')
                        self.currstate = tran.dest
                        self.parse_input(string[1:])
                    else:
                        console.print('λ', style='blue on white', end='')
                        self.currstate = tran.dest
                        self.parse_input(string)

    @property
    def final_states(self):
        return self._final_states

    @final_states.setter
    def final_states(self, value):
        self._final_states = value


class Transition(object):
    def __init__(self, src, in_symbol, out_symbol, dest):
        self.src = src
        self.dest = dest
        self.in_symbol = in_symbol
        self.out_symbol = out_symbol


class State:
    def __init__(self, name, is_final):
        self.name = name
        self.is_final = is_final
        self.transitions = []
        self.dictionary = {}


transitions = []
states = []
machine = None


def add_state(statename, isfinal):
    states.append(State(statename, isfinal))
    return State(statename, isfinal)


def add_transition(in_state_name, insymbol, outsymbol, out_state_name):
    transitions.append(Transition(in_state_name, insymbol, outsymbol, out_state_name))
    return Transition(in_state_name, insymbol, outsymbol, out_state_name)


def add_set_transition(in_state_name, inputs_set, out_state_name):
    return [add_transition(in_state_name, ch, ch, out_state_name) for ch in inputs_set]
