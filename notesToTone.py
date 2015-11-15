# notesToTone.py
# Created by: Nick Usoff
# Created on: 11-14-15

# Purpose: to convert a string in the form: "N-N, N-N-N, NN,..." where N is a note,
#   	   such as B4, or F#5 into a javascript array of the type [[0, 4], [6, -2]
#   	   ...] where each number corresponds to that notes distance from middle
#		   C


def getLetDif(letter):
	if(letter == 'A'): return -3
	if(letter == 'B'): return -1
	if(letter == 'C'): return 0
	if(letter == 'D'): return 2
	if(letter == 'E'): return 4
	if(letter == 'F'): return 5
	if(letter == 'G'): return 7



def convertToArray(str_arr):
	for str in str_arr:
		arrInp = str.split(", ")
		chords = []
		for chord in arrInp:
			notes = chord.split("-")
			# print(notes)

			num_chord = []
			for note in notes:
				noteNum = getLetDif(note[0])
				if (note[1] == "#"):
					noteNum += 1
					noteNum += (int(note[2]) - 4) * 12
				else:
					noteNum += (int(note[1]) - 4) * 12
				note = noteNum
				num_chord.append(note)
			chords.append(num_chord)
		print(chords)


testString = "B4-C#5-D#3, B4-B5-B6-A#4"


convertToArray(["D#4-F#4, A#4-F#4, B4-D5, B4-F#5",
				"C4, G4, E4, D4-F4, E4, C4-G4",
				"C4-G4, E4, B4, D4, C4, C4-G4"
			    ])


# print("expected output: [[-1, 13, -9], [-1, 11, 23, -2]]")
# convertToArray(convertToArray)

