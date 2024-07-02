class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        n1 = len(students)
        n2 = len(sandwiches)

        s1 = students.count(0)
        s2 = students.count(1)

        sw1 = sandwiches.count(0)
        sw2 = sandwiches.count(1)

        if s1 == sw1 and s2 == sw2:
            return 0
            
        count = 0
        for i in range(n1):
            if students[i] == sandwiches[i]:
                count += 1
        return n2 - count