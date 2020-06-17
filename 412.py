class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        myList = []
        if n == 1:
            myList.append("%d" % n)
            return myList
        for i in range(1,n+1):
            if i % 15 == 0:
                myList.append("FizzBuzz")
            elif i % 3 == 0:
                myList.append("Fizz")
            elif i % 5 == 0:
                myList.append("Buzz")
            else:
                myList.append("%d" % i)
        return myList
