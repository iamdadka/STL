lessons_dict = {}

with open('subjects.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        subject, lessons = line.split(':')
        lesson_types = lessons.split()
        total_lessons = 0
        for lesson_type in lesson_types:
            lesson_count = int(lesson_type.split('(')[0])
            total_lessons += lesson_count
        lessons_dict[subject] = total_lessons

print("Словарь с количеством занятий по предметам:")
print(lessons_dict)