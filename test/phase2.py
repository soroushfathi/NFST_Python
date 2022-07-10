import time

from sfst.__init__ import (
    add_state, add_transition, add_set_transition, console, Machine, Progress,
    transitions, states, )

if __name__ == '__main__':
    console.rule('[bold red]🚀Start Parsing FST')
    q_0 = add_state('q_0', False)
    q_1 = add_state('q_1', False)
    q_2 = add_state('q_2', False)
    q_3 = add_state('q_3', False)
    q_4 = add_state('q_4', False)
    q_5 = add_state('q_5', False)
    q_6 = add_state('q_6', False)
    q_7 = add_state('q_7', False)
    q_final = add_state('q_final', True)

    # begining of word
    add_set_transition(q_0, "abcdefghijklmnopqrstuvwxyz", q_0)

    # if end with {x, z} -> add 'es' to the end
    add_set_transition(q_0, "xz", q_1)
    add_transition(q_1, 'λ', 'e', q_7)

    # if end with {s, sh, ss}, then three situation happen
    add_transition(q_0, 's', 's', q_2)
    add_transition(q_2, 'λ', 'e', q_7)
    add_set_transition(q_2, 'sh', q_1)

    # if end with {ch}
    add_transition(q_0, 'c', 'c', q_3)
    add_transition(q_3, 'h', 'h', q_1)

    # if end with {by, cy, dy, ey, fy, gy, hy, jy, ky, ly, my, ny, py, qy, ry, sy, ty, vy, wy, xy, yy, zy}
    add_set_transition(q_0, 'bcdfghjklmnpqrstvwxyz', q_4)
    add_transition(q_4, 'y', 'i', q_1)

    # if ends with {ay, ey, iy, oy, uy}
    add_set_transition(q_0, 'aeiou', q_5)
    add_transition(q_5, 'y', 'y', q_7)

    # fi ends with {fe, f} ->
    add_transition(q_0, 'f', 'v', q_6)
    add_transition(q_6, 'λ', 'e', q_7)
    add_transition(q_6, 'e', 'e', q_7)

    # final
    add_transition(q_7, 'λ', 's', q_final)

    input_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output_alphabet = 'abcdefghijklmnopqrstuvwxyz'

    machine = Machine(transitions, input_alphabet, output_alphabet, q_0, states)
    # machine.parse_input('house')
    # machine.parse_input('cat')

    with Progress() as progress:
        task = progress.add_task('[green]Parsing...', total=100)
        while not progress.finished:
            progress.update(task, advance=0.8)
            time.sleep(0.003)
    machine.parse_input('wolf')
    # machine.parse_input('cat')
    # machine.parse_input('house')
