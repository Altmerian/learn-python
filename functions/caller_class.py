# Calling a class as a function
class Dept:
    def __init__(self):
        self.depts = {
            'hr': 'Human Resources',
            'acc': 'Accounting',
            'ops': 'Operations',
            'sd': 'Sales and Distribution',
            'mkt': 'Marketing',
        }

    def __call__(self, dept):
        return self.depts[dept]


d = Dept()
s = d('sd')
print(s)
print(d('mkt'))


# The same code as a Closure
def dept():
    depts = {
        'hr': 'Human Resources',
        'acc': 'Accounting',
        'ops': 'Operations',
        'sd': 'Sales and Distribution',
        'mkt': 'Marketing',
    }

    def get_dept(dept):
        return depts[dept]

    return get_dept


d1 = dept()
s = d1('sd')
print(s)
print(d1('mkt'))
