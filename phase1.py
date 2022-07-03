import time
from fstpy import (
    add_state, add_transition, add_set_transition,
    Machine, Progress,
    transitions, states, machine
)

if __name__ == '__main__':
    q_0 = add_state('q0', False)
    q_1 = add_state('q1', False)
    q_final = add_state('q_final', True)

    add_transition(q_0, 's', 's', q_1)
    add_transition(q_1, 'λ', 'λ', q_final)
    add_transition(q_1, 's', 'λ', q_final)

    add_set_transition(q_0, "abcdefghijklmnopqrstuvwxyz", q_0)
    add_set_transition(q_0, "abcdefghijklmnopqrtuvwxyz", q_final)

    input_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output_alphabet = 'abcdefghijklmnopqrstuvwxyz'

    machine = Machine(transitions, input_alphabet, output_alphabet, q_0, states)
    # machine.parse_input('sun')
    # machine.parse_input('samsung')
    # machine.parse_input('buss')
    # machine.parse_input('chess')

    with Progress() as progress:
        task = progress.add_task('[green]Parsing...', total=80)
        while not progress.finished:
            time.sleep(0.003)
            progress.update(task, advance=0.9)
    machine.parse_input('sun')
