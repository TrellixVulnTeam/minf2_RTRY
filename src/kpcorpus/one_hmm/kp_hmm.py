import numpy as np
import math
import copy

class HMM(object):
	"""
	Baseline Hidden Markov Model
	"""
	def __init__(self, number_of_states=12, dim=12):
		self.number_of_states = number_of_states
		self.transition_model = TransitionModel(number_of_states)
		self.emission_model = EmissionModel(number_of_states, dim)
		self.trained = False

	def train(self,X,Y):
		"""
		Method used to train HMM
		X :	4D Matrix
			X[:]			= songs
			X[:][:] 		= notes
		Y :	Labels
			Y[:]			= songs
			Y[:][:]			= notes
		"""

		self.emission_model.train(X,Y)
		self.transition_model.train(Y)
		self.trained = True

	def test(self, X, Y):
		"""
		Method for testing whether the predictions for XX match Y.
		X :	4D Matrix
			X[:]			= songs
			X[:][:] 		= notes
		Y :	Labels
			Y[:]			= songs
			Y[:][:]			= notes
		"""

		if not self.trained:
			raise Exception('Model not trained')

		Y_pred = []
		for song in X:
			Y_pred_i = self.viterbi(song)
			Y_pred.append(Y_pred_i)

		# Compare
		count = 0
		correct = 0
		for i, song in enumerate(Y):
			for j, frame in enumerate(song):
				count += 1
				if (frame == Y_pred[i][j]):
					correct += 1


		accuracy = float(correct) / float(count)
		return accuracy, Y_pred

	def viterbi(self, X):
		"""
		Viterbi forward pass algorithm
		determines most likely state (chord) sequence from observations
		X :	1D
		Returns state (chord) sequence
		Notes:
		State 0 	= starting state
		State N+1	= finish state
		X here is different from X in self.train(X,y), here it is 2D
		"""

		T = len(X)
		N = self.number_of_states

		# Create path prob matrix
		vit = np.zeros((N+2, T))
		# Create backpointers matrix
		backpointers = np.empty((N+2, T))

		# Note: t here is 0 indexed, 1 indexed in Jurafsky et al (2014)

		# Initialisation Step
		for s in range(1,N+1):
			vit[s,0] = self.transition_model.logprob(0,s) + self.emission_model.logprob(s,X[0])
			backpointers[s,0] = 0

		# Main Step
		for t in range(1,T):
			for s in range(1,N+1):
				vit[s,t] = self._find_max_vit(s,t,vit,X)
				backpointers[s,t] = self._find_max_back(s,t,vit,X)

		# Termination Step
		vit[N+1,T-1] = self._find_max_vit(N+1,T-1,vit,X,termination=True)
		backpointers[N+1,T-1] = self._find_max_back(N+1,T-1,vit,X,termination=True)

		return self._find_sequence(vit,backpointers,N,T)

	def _find_max_vit(self,s,t,vit,X,termination=False):

		N = self.number_of_states

		if termination:
			v_st_list = [vit[i,t] + self.transition_model.logprob(i,s) \
						for i in range(1,N+1)]
		else:
			v_st_list = [vit[i,t-1] + self.transition_model.logprob(i,s) \
						* self.emission_model.logprob(s,X[t]) for i in range(1,N+1)]

		return max(v_st_list)

	def _find_max_back(self,s,t,vit,X,termination=False):

		N = self.number_of_states

		if termination:
			b_st_list = np.array([vit[i,t] + self.transition_model.logprob(i,s) \
						for i in range(1,N+1)])
		else:
			b_st_list = np.array([vit[i,t-1] + self.transition_model.logprob(i,s) \
						for i in range(1,N+1)])

		return np.argmax(b_st_list) + 1

	def _find_sequence(self,vit,backpointers,N,T):

		seq = [None for i in range(T)]

		state = backpointers[N+1,T-1]
		seq[-1] = state

		for i in range(1,T):
			state = backpointers[state,T-i]
			seq[-(i+1)] = state

		return seq

class TransitionModel(object):
	"""
	Transition Model
	n :	Numer of states
	model[i][j] = probability of transitioning to j in i
	"""

	def __init__(self, n):
		"""
		Note for transition model states include start and end (0 and n+1)
		"""
		self.number_of_states = n
		self._model = None
		self.states = range(self.number_of_states+2)

	def train(self, y):
		"""
		Supervised training of transition model
		Y :	sequences of chords
			rows	= songs
			columns = chord at each time step
		TODO: augmented sequences with start and end state
		"""

		# Augment data with start and end states for training
		Y = copy.deepcopy(y)
		for i in range(len(y)):
			Y[i].insert(0,0)
			Y[i].append(self.number_of_states + 1)

		self._model = self._get_normalised_bigram_counts(Y)

	def _get_normalised_bigram_counts(self,y):

		model = dict()

		for state in self.states:
			model[state] = np.zeros(self.number_of_states + 2)

		for sequence in y:
			lasts = None
			for state in sequence:
				if lasts is not None:
					model[lasts][state] += 1
				lasts = state

		# Smooth and Normalise
		for state in self.states:
			model[state] += 1
			model[state] = model[state] / np.sum(model[state])

		return model

	# def doesnt_work(self,y):
	# 	"""
	# 	Code adapted from NLTK implementation of supervised training in HMMs
	# 	"""
	#
	# 	estimator = lambda fdist, bins: MLEProbDist(fdist)
	#
	# 	transitions = ConditionalFreqDist()
	# 	outputs = ConditionalFreqDist()
	# 	for sequence in y:
	# 		lasts = None
	# 		for state in sequence:
	# 			if lasts is not None:
	# 				transitions[lasts][state] += 1
	# 			lasts = state
	#
	# 	N = self.number_of_states + 2
	# 	model = ConditionalProbDist(transitions, estimator, N)
	#
	# 	return model

	def logprob(self, state, next_state):
		prob = self._model[state][next_state]
		return math.log(prob,2)

class EmissionModel(object):
	"""
	Gaussian Emission Model
	Different Gaussian parameters for each state
	"""
	def __init__(self,number_of_states,dim=12):
		self.number_of_states = number_of_states 	# can change
		self.dim = dim
		self.states = range(1,number_of_states+1)
		self._model = None

	def train(self,X,Y):
		"""
		Supervised training of emission model
		X :	2D
			X[:]			= songs
			X[:][:] 		= notes
		y :	2D
			rows	= songs
			columns = chords
		"""

		self._model = self._get_nb_estimates(X,Y)

	def logprob(self, state, obv):
		prob = self._model[state][obv]
		return math.log(prob,2)


	def _get_nb_estimates(self, X, Y):

		model = dict()

		for state in self.states:
			model[state] = np.zeros(self.dim)
		for i, song in enumerate(X):
			for j, note in enumerate(song):
				state = Y[i][j]
				model[state][note] += 1

		# Smooth and Normalise
		for state in self.states:
			model[state] += 1
			model[state] = model[state] / np.sum(model[state])
		return model

def get_one_hot_vector(note, dim):
	vec = np.zeros(dim)
	vec[note] = 1.0
	return vec
