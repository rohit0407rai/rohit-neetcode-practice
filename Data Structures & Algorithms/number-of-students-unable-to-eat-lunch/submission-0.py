class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        consecutive_failures = 0
        while students and sandwiches and consecutive_failures != len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                consecutive_failures = 0
            else:
                popItem = students.pop(0)
                students.append(popItem)
                consecutive_failures +=1
        return len(students)