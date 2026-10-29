class TimeMap {
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        timeMap[key].push_back({timestamp, value});
        cout << "ppppppp\n";
    }
    
    string get(string key, int timestamp) {
        cout << "size of "<<key << " is: " << timeMap[key].size() << " \n\n";
        return binary_search(key, 0, timeMap[key].size() -1, timestamp, -1);
    }
private:
    unordered_map<string, vector<pair<int, string>>> timeMap;

    std::string binary_search(string key, int start, int end, int target, int next_largest) {
    if (timeMap[key].size() == 0) {
        return "";
    }

    if (start > end) {
        // Return the closest timestamp <= target if it exists
        return (next_largest != -1) ? timeMap[key][next_largest].second : "";
    }

    int middle = start + (end - start) / 2;
    cout << "middle is " << middle << "\n";
    cout << "timestamp at middle: " << timeMap[key][middle].first << "\n";

    if (timeMap[key][middle].first == target) {
        return timeMap[key][middle].second;
    }

    if (timeMap[key][middle].first < target) {
        // Update next_largest since it's a valid candidate
        return binary_search(key, middle + 1, end, target, middle);
    } else {
        // Search the left half without updating next_largest
        return binary_search(key, start, middle - 1, target, next_largest);
    }
}

};
