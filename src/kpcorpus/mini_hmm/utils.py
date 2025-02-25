import numpy as np

def get_chord_tones_12(X, y):
		"""
		X :	4D List
			X[:]			= songs
			X[:][:] 		= frames (varying size)
			X[:][:][:]		= notes
			X[:][:][:][:]	= components
		y :	sequences of chords
			rows	= songs
			columns = chord at each time step
		Return
		chord_tones : 3D
			t[:] 		= songs
			t[:][:] 	= frames
			t[:][:][:] 	= 1 if note is chord tone, 0 otherwise
		"""

		chord_tones = []

		for i, song in enumerate(y):
			ith_song_tones = []
			for j, chord in enumerate(song):
				# Mode = 1 if maj, 0 if min
				chord_tpc = chord - 1
				jth_chord_tones = []
				for k, note in enumerate(X[i][j]):
					# TPC (Tonal Pitch Class, [0:11]) of note stored as first component (already normalised by key)
					tpc = note[0]
					# root
					if tpc == chord_tpc:
						jth_chord_tones.append(1)
					# 5th
					elif tpc == (chord_tpc + 7) % 12:
						jth_chord_tones.append(1)
					# 3rd (maj or min)
					elif tpc == (chord_tpc + 3) % 12:
						jth_chord_tones.append(1)
					elif tpc == (chord_tpc + 4) % 12:
						jth_chord_tones.append(1)
					else:
						jth_chord_tones.append(0)
				ith_song_tones.append(jth_chord_tones)
			chord_tones.append(ith_song_tones)

		return chord_tones

def get_chord_tones(X, y):
		"""
		X :	4D List
			X[:]			= songs
			X[:][:] 		= frames (varying size)
			X[:][:][:]		= notes
			X[:][:][:][:]	= components
		y :	sequences of chords
			rows	= songs
			columns = chord at each time step
		Return
		chord_tones : 3D
			t[:] 		= songs
			t[:][:] 	= frames
			t[:][:][:] 	= 1 if note is chord tone, 0 otherwise
		"""

		chord_tones = []

		for i, song in enumerate(y):
			ith_song_tones = []
			for j, chord in enumerate(song):
				# Mode = 1 if maj, 0 if min
				if chord % 2 == 0:
					# Minor
					chord_tpc = (chord / 2) - 1
					mode = 0
				else:
					# Major
					chord_tpc = ((chord + 1) / 2) - 1
					mode = 1
				jth_chord_tones = []
				for k, note in enumerate(X[i][j]):
					# TPC (Tonal Pitch Class, [0:11]) of note stored as first component (already normalised by key)
					tpc = note[0]
					# root
					if tpc == chord_tpc:
						jth_chord_tones.append(1)
					# 5th
					elif tpc == (chord_tpc + 7) % 12:
						jth_chord_tones.append(1)
					# 3rd (maj or min)
					elif tpc == (chord_tpc + 3 + mode) % 12:
						jth_chord_tones.append(1)
					else:
						jth_chord_tones.append(0)
				ith_song_tones.append(jth_chord_tones)
			chord_tones.append(ith_song_tones)

		return chord_tones

def get_chord_tones_states(X, y):
		"""
		X :	4D List
			X[:]			= songs
			X[:][:] 		= frames (varying size)
			X[:][:][:]		= notes
			X[:][:][:][:]	= components
		y :	sequences of chords
			rows	= songs
			columns = chord at each time step
		Return
		chord_tones : 3D
			t[:] 		= songs
			t[:][:] 	= frames
			t[:][:][:] 	= 1 if note is chord tone, 0 otherwise
		"""

		chord_tones = []

		for i, song in enumerate(y):
			ith_song_tones = []
			for j, chord in enumerate(song):
				# Mode = 1 if maj, 0 if min
				if chord % 2 == 0:
					# Minor
					chord_tpc = (chord / 2) - 1
					mode = 0
				else:
					# Major
					chord_tpc = ((chord + 1) / 2) - 1
					mode = 1
				jth_chord_tones = []
				for k, note in enumerate(X[i][j]):
					# TPC (Tonal Pitch Class, [0:11]) of note stored as first component (already normalised by key)
					tpc = note[0]
					# root
					if tpc == chord_tpc:
						jth_chord_tones.append(2)
					# 5th
					elif tpc == (chord_tpc + 7) % 12:
						jth_chord_tones.append(2)
					# 3rd (maj or min)
					elif tpc == (chord_tpc + 3 + mode) % 12:
						jth_chord_tones.append(2)
					else:
						jth_chord_tones.append(1)
				ith_song_tones.append(jth_chord_tones)
			chord_tones.append(ith_song_tones)

		return chord_tones

def get_chord_tones_cpc(X, y):
		"""
		X :	4D List
			X[:]			= songs
			X[:][:] 		= frames (varying size)
			X[:][:][:]		= notes
			X[:][:][:][:]	= components
		y :	sequences of chords
			rows	= songs
			columns = chord at each time step
		Return
		chord_tones : 3D
			t[:] 		= songs
			t[:][:] 	= frames
			t[:][:][:] 	= 1 if note is chord tone, 0 otherwise
		"""

		chord_tones = []

		for i, song in enumerate(y):
			ith_song_tones = []
			for j, chord in enumerate(song):
				# Mode = 1 if maj, 0 if min
				if chord % 2 == 0:
					# Minor
					chord_tpc = (chord / 2) - 1
					mode = 0
				else:
					# Major
					chord_tpc = ((chord + 1) / 2) - 1
					mode = 1
				jth_chord_tones = []
				for k, note in enumerate(X[i][j]):
					# TPC (Tonal Pitch Class, [0:11]) of note stored as first component (already normalised by key)
					tpc = note[0]
					jth_chord_tones.append(((tpc - chord_tpc) % 12) + 1)
				ith_song_tones.append(jth_chord_tones)
			chord_tones.append(ith_song_tones)

		return chord_tones


def get_chord_tones_states_more(X, y):
		"""
		X :	4D List
			X[:]			= songs
			X[:][:] 		= frames (varying size)
			X[:][:][:]		= notes
			X[:][:][:][:]	= components
		y :	sequences of chords
			rows	= songs
			columns = chord at each time step
		Return
		chord_tones : 3D
			t[:] 		= songs
			t[:][:] 	= frames
			t[:][:][:] 	= 1 if note is chord tone, 0 otherwise
		"""

		chord_tones = []

		for i, song in enumerate(y):
			ith_song_tones = []
			for j, chord in enumerate(song):
				# Mode = 1 if maj, 0 if min
				if chord % 2 == 0:
					# Minor
					chord_tpc = (chord / 2) - 1
					mode = 0
				else:
					# Major
					chord_tpc = ((chord + 1) / 2) - 1
					mode = 1
				jth_chord_tones = []
				for k, note in enumerate(X[i][j]):
					# TPC (Tonal Pitch Class, [0:11]) of note stored as first component (already normalised by key)
					tpc = note[0]
					# root
					if tpc == chord_tpc:
						jth_chord_tones.append(3)
					# 5th
					elif tpc == (chord_tpc + 7) % 12:
						jth_chord_tones.append(2)
					# 3rd (maj or min)
					elif tpc == (chord_tpc + 3 + mode) % 12:
						jth_chord_tones.append(2)
					else:
						jth_chord_tones.append(1)
				ith_song_tones.append(jth_chord_tones)
			chord_tones.append(ith_song_tones)

		return chord_tones

def get_chord_tones_states_majmin(X, y):
		"""
		X :	4D List
			X[:]			= songs
			X[:][:] 		= frames (varying size)
			X[:][:][:]		= notes
			X[:][:][:][:]	= components
		y :	sequences of chords
			rows	= songs
			columns = chord at each time step
		Return
		chord_tones : 3D
			t[:] 		= songs
			t[:][:] 	= frames
			t[:][:][:] 	= 1 if note is chord tone, 0 otherwise
		"""

		chord_tones = []

		for i, song in enumerate(y):
			ith_song_tones = []
			for j, chord in enumerate(song):
				# Mode = 1 if maj, 0 if min
				jth_chord_tones = []
				for k, note in enumerate(X[i][j]):
					# TPC (Tonal Pitch Class, [0:11]) of note stored as first component (already normalised by key)
					jth_chord_tones.append(1)
				ith_song_tones.append(jth_chord_tones)
			chord_tones.append(ith_song_tones)

		return chord_tones

def get_chord_tones_states_met(X, y):
		"""
		X :	4D List
			X[:]			= songs
			X[:][:] 		= frames (varying size)
			X[:][:][:]		= notes
			X[:][:][:][:]	= components
		y :	sequences of chords
			rows	= songs
			columns = chord at each time step
		Return
		chord_tones : 3D
			t[:] 		= songs
			t[:][:] 	= frames
			t[:][:][:] 	= 1 if note is chord tone, 0 otherwise
		"""

		chord_tones = []

		for i, song in enumerate(y):
			ith_song_tones = []
			for j, chord in enumerate(song):
				# Mode = 1 if maj, 0 if min
				if chord % 2 == 0:
					# Minor
					chord_tpc = (chord / 2) - 1
					mode = 0
				else:
					# Major
					chord_tpc = ((chord + 1) / 2) - 1
					mode = 1
				jth_chord_tones = []
				for k, note in enumerate(X[i][j]):
					# TPC (Tonal Pitch Class, [0:11]) of note stored as first component (already normalised by key)
					tpc = note[0]
					met = note[1]
					jth_chord_tones.append(met + 1)
				ith_song_tones.append(jth_chord_tones)
			chord_tones.append(ith_song_tones)

		return chord_tones

def get_chord_tones_states_dom(X, y):
		"""
		X :	4D List
			X[:]			= songs
			X[:][:] 		= frames (varying size)
			X[:][:][:]		= notes
			X[:][:][:][:]	= components
		y :	sequences of chords
			rows	= songs
			columns = chord at each time step
		Return
		chord_tones : 3D
			t[:] 		= songs
			t[:][:] 	= frames
			t[:][:][:] 	= 1 if note is chord tone, 0 otherwise
		"""

		chord_tones = []

		for i, song in enumerate(y):
			ith_song_tones = []
			for j, chord in enumerate(song):
				# Mode = 1 if maj, 0 if min

				chord = chord - 1

				if chord % 3 == 0:
					# Major
					chord_tpc = chord / 3
					mode = 4
				elif (chord - 1) % 3 == 0:
					# Minor
					chord_tpc = (chord - 1) / 3
					mode = 3
				else:
					# Dominant
					chord_tpc = (chord - 2) / 3
					mode = 10
				jth_chord_tones = []
				for k, note in enumerate(X[i][j]):
					# TPC (Tonal Pitch Class, [0:11]) of note stored as first component (already normalised by key)
					tpc = note[0]
					# root
					if tpc == chord_tpc:
						jth_chord_tones.append(2)
					# 5th
					elif tpc == (chord_tpc + 7) % 12:
						jth_chord_tones.append(3)
					# 3rd (maj or min)
					elif tpc == (chord_tpc + mode) % 12:
						jth_chord_tones.append(4)
					else:
						jth_chord_tones.append(1)
				ith_song_tones.append(jth_chord_tones)
			chord_tones.append(ith_song_tones)

		return chord_tones

def get_chord_tones_states_relmin(X, y):
		"""
		X :	4D List
			X[:]			= songs
			X[:][:] 		= frames (varying size)
			X[:][:][:]		= notes
			X[:][:][:][:]	= components
		y :	sequences of chords
			rows	= songs
			columns = chord at each time step
		Return
		chord_tones : 3D
			t[:] 		= songs
			t[:][:] 	= frames
			t[:][:][:] 	= 1 if note is chord tone, 0 otherwise
		"""

		chord_tones = []

		for i, song in enumerate(y):
			ith_song_tones = []
			for j, chord in enumerate(song):
				# Mode = 1 if maj, 0 if min

				chord_tpc = chord - 1

				jth_chord_tones = []
				try:
					test = X[i][j]
				except IndexError as e:
					error_str = """
								Index error with {0}th song, {1}th chord:
								X contains {2} songs.
								X[{0}] contains {3} frames/chords
								""".format(i, j, len(X), len(X[i]))
					print len(song)
					print len(X[i])
					raise Exception(error_str)
				for k, note in enumerate(X[i][j]):
					# TPC (Tonal Pitch Class, [0:11]) of note stored as first component (already normalised by key)
					tpc = note[0]
					# root
					if tpc == chord_tpc:
						jth_chord_tones.append(1)
					# 5th
					elif tpc == (chord_tpc + 7) % 12:
						jth_chord_tones.append(2)
					# 3rd (maj or min)
					elif tpc == (chord_tpc + 4) % 12:
						jth_chord_tones.append(3)
					else:
						jth_chord_tones.append(1)
				ith_song_tones.append(jth_chord_tones)
			chord_tones.append(ith_song_tones)

		return chord_tones

def get_chord_tones_states_nomode(X, y):
		"""
		X :	4D List
			X[:]			= songs
			X[:][:] 		= frames (varying size)
			X[:][:][:]		= notes
			X[:][:][:][:]	= components
		y :	sequences of chords
			rows	= songs
			columns = chord at each time step
		Return
		chord_tones : 3D
			t[:] 		= songs
			t[:][:] 	= frames
			t[:][:][:] 	= 1 if note is chord tone, 0 otherwise
		"""

		chord_tones = []

		for i, song in enumerate(y):
			ith_song_tones = []
			for j, chord in enumerate(song):
				# Mode = 1 if maj, 0 if min
				chord_tpc = chord - 1
				jth_chord_tones = []
				for k, note in enumerate(X[i][j]):
					# TPC (Tonal Pitch Class, [0:11]) of note stored as first component (already normalised by key)
					tpc = note[0]
					# root
					if tpc == chord_tpc:
						jth_chord_tones.append(2)
					# 5th
					elif tpc == (chord_tpc + 7) % 12:
						jth_chord_tones.append(2)
					else:
						jth_chord_tones.append(1)
				ith_song_tones.append(jth_chord_tones)
			chord_tones.append(ith_song_tones)

		return chord_tones

def get_ct_features(X, y, chord_tones):

		X_ct = []
		y_ct = []


		for i, song in enumerate(X):
			for j, frame in enumerate(song):
				x_ij = np.zeros(12)
				for k, note in enumerate(frame):
					if chord_tones[i][j][k] == 1:
						x_ij[int(note[0])] = 1
				X_ct.append(x_ij)
				y_ct.append(y[i][j])

		X_ct = np.asarray(X_ct)
		y_ct = np.asarray(y_ct)

		return X_ct, y_ct

def get_concat_ct_X(X, ct):

	a = [1,2,4,5,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

	ct_np = []
	X_np = []
	for i, song in enumerate(ct):
		for j, frame in enumerate(song):
			ct_np += frame
			for note in X[i][j]:
				X_np.append(np.delete(note, a))

	X_np = np.asarray(X_np)
	ct_np = np.asarray(ct_np)

	return X_np, ct_np

def get_concat_ct_X_kp(X, ct):

	ct_np = []
	X_np = []
	for i, song in enumerate(ct):
		for j, frame in enumerate(song):
			ct_np += frame
			for note in X[i][j]:
				X_np.append(note)

	X_np = np.asarray(X_np)
	ct_np = np.asarray(ct_np)

	return X_np, ct_np
