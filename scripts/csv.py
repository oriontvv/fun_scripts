import csv
from collections import namedtuple


# use pandas.read_csv() for huge csv files

def read_rows(csv_fname, types=()):
    with open(csv_fname) as f:
        f_csv = csv.reader(f)
        header = next(f_csv)
        assert len(types) == len(header), "Bad header"

        Row = namedtuple('Row', header)
        for line in f_csv:
            row = (convert(value) for convert, value in zip(types, line))
            yield Row(*row)


def example_write_tuples():
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [
        ('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
    ]
    with open('stocks.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


def example_write_dict():
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [
        {
            'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
            'Time': '9:36am', 'Change': -0.18, 'Volume': 181800
        },
        {
            'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
            'Time': '9:36am', 'Change': -0.15, 'Volume': 195500
        },
        {
            'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
            'Time': '9:36am', 'Change': -0.46, 'Volume': 935000
        },
    ]
    with open('stocks.csv', 'w') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)
