if __name__ == '__main__':
    n = int(input('Digite um valor: '))
    
    student_marks = {}
    for _ in range(n):
        name, *line = input('Digite o nome e as notas: ').split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input('Digite o nome para visualizar a media: ')
    if query_name in student_marks.keys():
        l = student_marks[query_name]
        media = sum(l)/len(l)
        print(f'{"A media é {:.2f}".format(media)}')