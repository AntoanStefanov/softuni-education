import unittest

from project.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student('Joe')

    def test_init(self):
        self.assertEqual('Joe', self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_init_with_courses(self):
        self.a = Student('Joe', {'Python': ['great lang', 'amazing']})

        self.assertEqual('Joe', self.a.name)
        self.assertEqual({'Python': ['great lang', 'amazing']}, self.a.courses)

    def test_init_with_courses_and_last_param(self):
        self.a = Student('Joe', None)

        self.assertEqual('Joe', self.a.name)
        self.assertEqual({}, self.a.courses)

    def test_enroll_with_already_added_course(self):
        self.student.courses = {'Python': ['great lang', 'amazing']}
        res = self.student.enroll('Python', ['tremendous', 'phenomenal'])
        self.assertEqual("Course already added. Notes have been updated.", res)
        self.student.courses['Python'] = ['great lang', 'amazing', 'tremendous', 'phenomenal']

    def test_enroll_in_new_course_with_notes_no_last_arg(self):
        res = self.student.enroll('Python', ['tremendous', 'phenomenal'])
        self.assertEqual("Course and course notes have been added.", res)
        self.student.courses['Python'] = ['tremendous', 'phenomenal']

    # That case is tricky tricky, 90/100 test number 3
    def test_enroll_in_new_course_without_adding_notes(self):
        self.student.enroll('Python', ['a', 'b', 'c'], 'no')
        self.assertEqual([], self.student.courses['Python'])

    def test_enroll_in_new_course_with_notes_yes(self):
        res = self.student.enroll('Python', ['tremendous', 'phenomenal'], 'Y')
        self.assertEqual("Course and course notes have been added.", res)
        self.student.courses['Python'] = ['tremendous', 'phenomenal']

    def test_enroll_in_new_course_with_notes_yes_lower(self):
        res = self.student.enroll('Python', ['tremendous', 'phenomenal'], 'y')
        self.assertEqual("Course has been added.", res)
        self.student.courses['Python'] = ['tremendous', 'phenomenal']

    def test_enroll_in_new_course_with_notes_yes_which_means_the_old_ones_got_deleted(self):
        self.student.enroll('Python', ['tremendous', 'phenomenal'], 'Y')
        res = self.student.enroll('Python', ['great lang', 'amazing'], 'Y')
        self.assertEqual("Course already added. Notes have been updated.", res)
        self.student.courses['Python'] = ['great lang', 'amazing']

    def test_enroll_in_new_course_with_empty_notes(self):
        res = self.student.enroll('Python', [], 'no')
        self.assertEqual("Course has been added.", res)
        self.student.courses['Python'] = []

    def test_enroll_in_new_course_without_notes(self):
        res = self.student.enroll('Python', ['tremendous', 'phenomenal'], 'no')
        self.assertEqual("Course has been added.", res)
        self.student.courses['Python'] = []

    def test_add_notes(self):
        self.student.enroll('Python', [])
        res = self.student.add_notes('Python', 'tremendous')
        self.assertEqual("Notes have been updated", res)
        self.assertEqual(self.student.courses['Python'], ['tremendous'])

    def test_add_notes_unsuccessful(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Python', ['tremendous', 'phenomenal'])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course(self):
        self.student.enroll('Python', ['tremendous', 'phenomenal'], 'no')
        res = self.student.leave_course('Python')
        self.assertEqual("Course has been removed", res)
        self.assertEqual({}, self.student.courses)

    def test_leave_course_unsuccessful(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Python')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

