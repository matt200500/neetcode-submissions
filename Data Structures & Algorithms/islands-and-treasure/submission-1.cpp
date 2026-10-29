class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        for (int row = 0; row < grid.size(); ++row){
            for (int column = 0; column < grid[0].size(); ++column){
                if (grid[row][column] == 0){
                    BFS(row, column, grid, 0);
                }
            }
        }
    }

private:
    void BFS(int row, int column, vector<vector<int>>& grid, int current_distance){
        queue<tuple<int,int, int>> q;
        q.push({row,column, current_distance});

        while(!q.empty()){
            int current_row = get<0>(q.front());
            int current_column = get<1>(q.front());
            int current_distance = get<2>(q.front());
            q.pop();

            if (current_row < 0 || current_row > grid.size() - 1){
                continue;
            }
            if (current_column < 0 || current_column > grid[0].size() - 1){
                continue;
            }

            if (grid[current_row][current_column] != 0){
                if (grid[current_row][current_column] != -1){
                    if (grid[current_row][current_column] <= current_distance){
                        continue;
                    }
                }else{
                    continue;
                }
            }

            if (grid[current_row][current_column] != 0) {
                grid[current_row][current_column] = current_distance;
            }

            q.push({current_row+1, current_column, current_distance+1});
            q.push({current_row-1, current_column, current_distance+1});
            q.push({current_row, current_column-1, current_distance+1}) ;
            q.push({current_row, current_column+1, current_distance+1});
        }
    }
};
