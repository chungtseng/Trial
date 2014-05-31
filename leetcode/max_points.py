# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)
        n = []
        for point in points:
            for p in [i for i in points if i.x != point.x or i.y != point.y]:
                

        return max(n)
raw = [(0,-12),(5,2),(2,5),(0,-5),(1,5),(2,-2),(5,-4),(3,4),(-2,4),(-1,4),(0,-5),(0,-8),(-2,-1),(0,-11),(0,-9)]
points = []
for t in raw:
    points.append(Point(t[0],t[1]))
print points[1].x
s = Solution()
print s.maxPoints(points)

#if __name__ == '__main__':
