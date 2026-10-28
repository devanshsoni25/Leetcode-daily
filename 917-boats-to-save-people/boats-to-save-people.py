class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        n = len(people)
        count = 0
        people.sort()

        low = 0
        high = n-1

        if n == 1:
            return 1

        while low<=high:

            if people[low] == limit:
                count+=1
                low+=1

            if people[high] == limit:
                count+=1
                high-=1

            if people[low]+people[high] <= limit:
                count +=1
                low+=1
                high-=1

            else:
                high-=1
                count+=1

        return count
            