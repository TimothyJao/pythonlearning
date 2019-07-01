midterms = [80, 91, 78]
finals = [98, 89, 54]
students = ['dan', 'ang', 'kate']

final_grades = {pair[0]: max(pair[1], pair[2]) for pair in zip(students, midterms, finals)}
print(final_grades)

scores = zip(
    students,
    map(
        lambda pair: ((pair[0]+pair[1])/2),
        zip(midterms, finals)
    )   
)


print(dict(scores))