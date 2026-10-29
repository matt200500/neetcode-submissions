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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* current = head;
        int i = 0;
        while(current != nullptr){
            current = current->next;
            ++i;
        }
        int removed_node = i - n;
        if (n > i){
            return head;
        }
        if (n == i){
            return head->next;
        }

        ListNode* dummy = head;
        ListNode* previous = nullptr;
        for (int y = 0; y < removed_node; ++y){
            previous = dummy;
            dummy = dummy->next;
        }
        previous->next = dummy->next;
        return head;
    }
};
