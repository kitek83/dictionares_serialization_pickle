def main():
    nr_class = {'CS101': '3004', 'CS102':'4501',
                'CS103':'6755', 'NT110':'1244',
                'CM241':'1411'}
    instructor = {'CS101': 'Huzar', 'CS102':'Abramowski',
                'CS103':'Romanowski', 'NT110':'Blady',
                'CM241':'Lewandowski'}
    hours = {'CS101': '8.00', 'CS102':'9.00',
                'CS103':'10.00', 'NT110':'11.00',
                'CM241':'13.00'}
    nr_course = input('Enter nr of the course:')
    if nr_course in nr_class:
        print('number of the class:', nr_class[nr_course])
    if nr_course in instructor:
        print('name of instructor:',instructor[nr_course])
    if nr_course in hours:
        print('start time:',hours[nr_course])
    else:
        print('course nr was not found!')
main()