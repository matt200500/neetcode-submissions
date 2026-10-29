class LRUCache {
public:
    LRUCache(int capacity) {
        max = capacity;
    }
    
    int get(int key) {
        auto it = cache.find(key);
        if (it != cache.end()){
            cacheorder.erase(it->second);
            cacheorder.push_back({key, it->second->second});
            it->second = --cacheorder.end();  
            return it->second->second;
        }
        return -1; 
    }
    
    void put(int key, int value) {
        auto it = cache.find(key);
        if (it != cache.end()) {
            cacheorder.erase(it->second);
            cacheorder.push_back({key, value});
            it->second = --cacheorder.end();
        } else {
            if (cacheorder.size() == max) {
                auto removed_item = cacheorder.front();
                cacheorder.pop_front();
                cache.erase(removed_item.first);
            }
            cacheorder.push_back({key, value});
            cache[key] = --cacheorder.end();
        }
    }
private:
    std::unordered_map<int,std::list<std::pair<int, int>>::iterator> cache;
    std::list<std::pair<int, int>> cacheorder;  // stores pairs of {key, value}
    int max = 0;
};
