"""
Chords of Music
https://www.codeabbey.com/index/task_view/chords-of-music
"""

# ====== imports block ================================== #


# ====== function declaration =========================== #
def what_tone_are_there(chords):
    major_shift = 4
    minor_shift = 3
    out = []

    for chord in chords:
        if (chord[0] + major_shift) % steps in [el % steps for el in chord[1:]]:
            out.append('major')
        elif (chord[0] + minor_shift) % steps in [el % steps for el in chord[1:]]:
            out.append('minor')
        else:
            out.append('other')

    return out


def get_root_note(chords):
    octave = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    out = []

    for chord in chords:
        out.append(octave[chord[0] % steps])

    return out


# ====== main code ====================================== #
n_chords = int(input())
chords = [[int(key) for key in input().split()] for _ in range(n_chords)]
steps = 12

chord = get_root_note(chords)
tone = what_tone_are_there(chords)

[print(f'{chord[i]}-{tone[i]}', end=' ') if tone[i] != 'other' else print(tone[i], end=' ') for i in range(n_chords)]

# ====== end of code ==================================== #
