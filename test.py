from midi_notes import *

for pitch in range(128):
	note = Note(pitch)
	for note.incidentals_style in [ Note.INCIDENTAL_ASCII, Note.INCIDENTAL_UNICODE, Note.INCIDENTAL_NAMES]:
		for note.prefer_flats in [ False, True]:
			print(f'{note:10s} {note.pitch:3d}')
			assert note.pitch == pitch
			interpreted_note = Note(str(note))
			print(f'{interpreted_note:10s} {interpreted_note.pitch:3d}')
			assert interpreted_note.pitch == pitch
