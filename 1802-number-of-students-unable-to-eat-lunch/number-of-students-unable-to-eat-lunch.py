
class Solution:
    def countStudents(self, students: List[int], sandwiche: List[int]) -> int:
        stud=deque(students)
        sandwiches=deque(sandwiche)
        count0,count1,length=0,0,len(students)
        for v in students:
            if v==0:
                count0+=1
            else:
                count1+=1
        while stud:
            if stud[0]==0 and stud[0]==sandwiches[0]:
                sandwiches.popleft()
                stud.popleft()
                count0-=1
            elif stud[0]==1 and stud[0]==sandwiches[0]:
                sandwiches.popleft()
                stud.popleft()
                count1-=1
            else:
                stud.append(stud.popleft())

            if sandwiches and sandwiches[0]==0:
                if count0==0:
                    return count0+count1
            if sandwiches and sandwiches[0]==1:
                if count1==0:
                    return count0+count1

        return 0
    