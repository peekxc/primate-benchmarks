import numpy as np
import primate
import os
import sys
from pathlib import Path

DATA_DIR = os.path.join(Path(__file__).parent.parent.absolute(), "data")


class PkgSuite:
	def setup(self):
		pass

	def time_pkg_import(self):
		import primate

	def time_trace_import(self):
		from primate.trace import hutch, hutchpp, xtrace

		assert callable(hutch)
		assert callable(hutchpp)
		assert callable(xtrace)

	def time_diagonal_import(self):
		from primate.diagonal import diag, xdiag

		assert callable(diag)
		assert callable(xdiag)

	def time_lanczos_import(self):
		from primate.lanczos import lanczos, rayleigh_ritz

		assert callable(lanczos)
		assert callable(rayleigh_ritz)


class TraceSuite:
	def setup(self):
		from primate.random import symmetric

		self.d = {}
		self.d["sym50"] = symmetric(50)

	def time_hutch(self):
		from primate.trace import hutch

		# for os.listdir(DATA_DIR)
		matrix_npz = np.load(os.path.join(DATA_DIR, "dw1024.npz"), allow_pickle=True)
		A = matrix_npz["matrix"].item()
		meta = matrix_npz["meta"].item()

		tr = hutch(A, converge="count", count=100)

	def time_hutch(self):
		from primate.trace import hutch

		# for os.listdir(DATA_DIR)
		matrix_npz = np.load(os.path.join(DATA_DIR, "dw1024.npz"), allow_pickle=True)
		A = matrix_npz["matrix"].item()
		meta = matrix_npz["meta"].item()

		tr = hutch(A, converge="count", count=100)
