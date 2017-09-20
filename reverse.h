struct Node{
    int val;
    Node* next;
}

Node* reverseList(Node* head){
    Node* pre;
    Node* after;
    Node* nHead;
    if(head == NULL || head -> next == NULL)
        return head;
    pre = head;
    after = head -> next;
    head -> next = NULL;
    while(after){
        nHead = after -> next;
        after -> next = pre;
        pre = after;
        after = nHead;
    }
    head = pre;
    return head;
}

