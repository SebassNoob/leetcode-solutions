class DefaultList(list):
    def __init__(self, fx):
        self._fx = fx
    def __setitem__(self, index, value):
        while len(self) <= index:
            self.append(self._fx())
        list.__setitem__(self, index, value)

class MyHashMap:

    def __init__(self):
        self.map = DefaultList(list)

    def put(self, key: int, value: int) -> None:
        self.map[key] = [key, value]
        

    def get(self, key: int) -> int:
        try:
            return self.map[key][1]
        except IndexError:
            return -1
        

    def remove(self, key: int) -> None:
        try:
            self.map[key] = []
        except IndexError:
            return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)