int list_size(struct ListNode* head){
    int size = 0;
    struct ListNode* pos = head;
    while (pos != NULL){
        size++;
        pos = pos->next;
    }
    return size;
}

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    n = list_size(head) - (n - 1);
    if (n == 1){
        return head->next;
    }
    int iter = 1;
    struct ListNode* pos = head;
    while (pos != NULL){
        if (iter + 1 == n){
            pos->next = pos->next->next;
        }
        iter++;
        pos = pos->next;
    }
    return head;
}
