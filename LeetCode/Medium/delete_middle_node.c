int list_size(struct ListNode* head){
    int size = 0;
    struct ListNode* pos = head;
    while (pos != NULL){
        size++;
        pos = pos->next;
    }
    return size;
}


struct ListNode* deleteMiddle(struct ListNode* head) {
    int n = list_size(head) / 2;
    if (n == 0){
        return head->next;
    }
    int iter = 0;
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
