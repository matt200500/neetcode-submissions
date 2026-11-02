class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dictionary:
            array = self.dictionary[key]
            return str(self.binary_search(array,timestamp,0,len(array)-1))
        else:
            return ""
    
    def binary_search(self,array,timestamp,left,right):
        if left > right:
            if array[right][0] < timestamp:
                return array[right][1]
            else:
                return ""
        
        middle = left + (right - left) // 2
        current_timestamp = array[middle][0]
        
        if current_timestamp == timestamp:
            return array[middle][1]
        elif current_timestamp > timestamp:
            return self.binary_search(array,timestamp,left,middle-1)
        else:
            return self.binary_search(array,timestamp,middle+1,right)
        
