import heapq


class PriorityOrder:
    def __init__(self):
        self._index = 0
        self._queue = []

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


if __name__ == '__main__':
    
    a = PriorityOrder()
    
    a.push("Facebook", 60)
    a.push("Apple", 100)
    a.push("Amazon", 70)
    a.push("Google", 80)

    for _ in range(4):
        print(a.pop())
