def executor(runnable):
    print("Führe Aktion aus")
    runnable(4711)
    print("Fertig")


def aktion1(v):
    print("aktion 1", v)


def aktion2(v):
    print("aktion 2", v)



executor(aktion1)
executor(aktion2)

student_tuples = [
    ('john', 'A', 12),
    ('jane', 'B', 16),
    ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[2])  ) # sort by age
print(student_tuples)
print("-"*10)
def sort_key(values):
    return values[2]

print(sorted(student_tuples, key=sort_key)  ) # sort by age
print(student_tuples)