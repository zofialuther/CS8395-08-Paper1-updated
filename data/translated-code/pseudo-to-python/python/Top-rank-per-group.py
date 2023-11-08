import collections
import itertools

N = 2

database_info = "example database information"
rows = database_info.split('\n')

DBRecord = collections.namedtuple('DBRecord', rows[0].split(','))

records = [DBRecord(*row.split(',')) for row in rows[1:]]

records.sort(key=lambda x: (x.Department, x.Salary), reverse=True)

grouped_records = itertools.groupby(records, key=lambda x: x.Department)

for key, group in grouped_records:
    print('\n'.join(str(record) for record in itertools.islice(group, N)))