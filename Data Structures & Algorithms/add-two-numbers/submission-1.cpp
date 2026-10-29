/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int l1_size = 0;
        int l2_size = 0;
        ListNode* l1_current = l1;
        ListNode* l2_current = l2;

        int l1_integer = 0;
        int l2_integer = 0;

        while(l1_current != nullptr || l2_current != nullptr){ // get numbers in both
            if (l1_current != nullptr){
                l1_integer += l1_current->val * pow(10, l1_size);
                l1_current = l1_current-> next;
                ++l1_size;
            }
            if(l2_current != nullptr){
                l2_integer += l2_current->val * pow(10, l2_size);
                l2_current = l2_current -> next;
                ++l2_size;
            }
        }

        int combined = l1_integer + l2_integer;
        string combined_string = to_string(combined);

        int current_int = combined_string[combined_string.size() -1] - '0';
        ListNode* new_head = new ListNode(current_int);
        ListNode* first_head = new_head;
        for (int i = combined_string.size() -2; i >= 0; --i){
            current_int = combined_string[i] - '0';
            new_head->next = new ListNode(current_int);
            new_head = new_head->next;
            
        }
        
        return first_head;
    }
};
