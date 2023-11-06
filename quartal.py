"""
Draws a fretboard with Dorian quartal chord voicings.

Uses <https://github.com/dmpayton/python-fretboard>

Requirements:

pip install fretboard

"""

import fretboard

fb = fretboard.Fretboard(frets=(0, 24), style={
    'drawing': {
        'height': 750,
        'width': 200,
    },
})

chords = [
    { 'label': 'A', 'color': 'red',    'markers': [(1,  0), (2,  0), (3,  0), (4,  1)] },
    { 'label': 'B', 'color': 'orange', 'markers': [(1,  2), (2,  2), (3,  2), (4,  3)] },
    { 'label': 'C', 'color': 'brown',  'markers': [(1,  3), (2,  3), (3,  4), (4,  5)] },
    { 'label': 'D', 'color': 'green',  'markers': [(1,  5), (2,  5), (3,  5), (4,  6)] },
    { 'label': 'E', 'color': 'blue',   'markers': [(1,  7), (2,  7), (3,  7), (4,  8)] },
    { 'label': 'F', 'color': 'indigo', 'markers': [(1,  9), (2, 10), (3, 10), (4, 11)] },
    { 'label': 'G', 'color': 'violet', 'markers': [(1, 11), (2, 11), (3, 11), (4, 13)] },
]

# Render in reverse order so that when chords overlap, the higher chord's color
# takes precedence.
chords.reverse()

for chord in chords:
    label, color, markers = chord['label'], chord['color'], chord['markers']
    for (string, fret) in markers:
        note_label = label if string == 1 else None
        fb.add_marker(label=note_label, string=string, fret=fret, color=color)
        if fret < 12:
            fb.add_marker(label=note_label, string=string, fret=fret+12, color=color)

fb.save('quartal.svg')
