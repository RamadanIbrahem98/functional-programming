import collections


def gross_salary_calculator(basic_salary: float):
    tax = 0.2 * basic_salary

    def segment_gross_salary(bonus: float) -> float:
        bonus + tax + basic_salary
    return segment_gross_salary


Segment = collections.namedtuple('Segment', [
    'segment',
    'basic_salary'
])

segments = (
    Segment(segment='a', basic_salary=1000),
    Segment(segment='b', basic_salary=2000),
    Segment(segment='c', basic_salary=3000)
)

gross_salary_calculators = dict(
    map(lambda a: (f'{a.segment}_gross_salary_calculator', gross_salary_calculator(a.basic_salary)), segments))


print(gross_salary_calculators['a_gross_salary_calculator'](200))
print(gross_salary_calculators['b_gross_salary_calculator'](200))
print(gross_salary_calculators['c_gross_salary_calculator'](200))
