from collections import defaultdict

class School():
    def __init__(self, school_name):

        self.school_name = school_name
        self._grade_levels = defaultdict(list)


    def sort(self):
        return ((key, tuple(self.grade(key))) for key in sorted(self._grade_levels.keys()))


    def grade(self, grade_level):
        return sorted(self._grade_levels[grade_level])


    def add(self, student, grade_level):
        self._grade_levels[grade_level].append(student)
