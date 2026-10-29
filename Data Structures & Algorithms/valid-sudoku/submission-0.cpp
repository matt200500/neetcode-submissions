class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        std::unordered_map<int,unordered_set<char>> rows;
        std::unordered_map<int,unordered_set<char>> columns;
        std::unordered_map<int,unordered_set<char>> subgrids;

        for (int i = 0; i < board.size(); ++i){
            for (int y = 0; y < board.size(); ++y){
                if (board[i][y] == '.'){
                    continue;
                }
                auto result1 = rows[i].insert(board[i][y]);
                if (!result1.second){
                    return false;
                }
                auto result2 = columns[y].insert(board[i][y]);
                if (!result2.second){
                    return false;
                }

                int subgrid_index = (i / 3) * 3 + (y / 3);
                auto result3 = subgrids[subgrid_index].insert(board[i][y]);
                if (!result3.second){
                    return false;
                }
            }
        }

        return true;
    }
};
