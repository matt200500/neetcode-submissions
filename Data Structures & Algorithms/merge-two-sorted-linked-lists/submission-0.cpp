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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* list1_current = list1;
        ListNode* list2_current = list2;
        ListNode* dummyhead = new ListNode(0);
        ListNode* current = dummyhead;

        while(list1_current != nullptr || list2_current != nullptr){
            int number1 = 200;
            int number2 = 200;
            if (list1_current != nullptr){
                number1 = list1_current->val;
            }
            if (list2_current != nullptr){
                number2 = list2_current->val;
            }

            if (number1 <= number2){
                current->next = new ListNode(number1);
                list1_current = list1_current->next;
                current = current->next;
            }else{
                current->next = new ListNode(number2);
                list2_current = list2_current->next;
                current = current->next;
            }
        }
        return dummyhead->next;
    }
};
