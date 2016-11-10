import csv
from collections import namedtuple

# todo add types
def read_rows(csv_fname):
	with open(csv_fname) as f:
		f_csv = csv.reader(f)
		header = next(f_csv)
		Row = namedtuple('Row', header)
		for row in f_csv:
			yield Row(*row)
