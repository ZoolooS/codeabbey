"""
Chords of Music
https://www.codeabbey.com/index/task_view/chords-of-music
"""

# ====== imports block ================================== #


# ====== function declaration =========================== #
def what_tone_are_there(chords):
    major_shift = 4
    minor_shift = 3
    full_shift = 7
    out = []

    for chord in chords:
        for note in chord:
            is_right_chord = (note + full_shift) % steps in chord
            if ((note + major_shift) % steps in chord) and is_right_chord:
                out.append(f'{get_note(note)}-major')
                break
            elif ((note + minor_shift) % steps in chord) and is_right_chord:
                out.append(f'{get_note(note)}-minor')
                break
            elif note == chord[-1]:
                out.append('other')

    return out


def get_note(note_num):
    octave = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    return octave[note_num]


# ====== main code ====================================== #
n_chords = int(input())
steps = 12
chords = [list(set([int(note) % steps for note in input().split()])) for _ in range(n_chords)]

print(*what_tone_are_there(chords))

# ====== end of code ==================================== #
