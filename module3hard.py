data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(structure):
    summ = 0
    if isinstance(structure, (int, float)):
        summ += structure
    elif isinstance(structure, str):
        summ += len(structure)
    elif isinstance(structure, (list, tuple, set)):
        for i in structure:
            summ += calculate_structure_sum(i)
    elif isinstance(structure, dict):
        for key, value in structure.items():
            summ += calculate_structure_sum(key)
            summ += calculate_structure_sum(value)
    return summ


result = calculate_structure_sum(data_structure)
print(result)