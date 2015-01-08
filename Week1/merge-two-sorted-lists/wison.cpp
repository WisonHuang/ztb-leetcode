 ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
  {
    ListNode *result=new ListNode(0);
    ListNode *p1=l1;
    ListNode *p2=l2;
    ListNode *r=result;
    if(p1==NULL && p2==NULL)
        return NULL;
    if(p1==NULL)
        return p2;
    if(p2==NULL)
        return p1;
    while (p1!=NULL && p2!=NULL){
            //r=(ListNode *)malloc(sizeif(ListNode));
            if(p1->val > p2->val){
                result->next=p2;
                p2=p2->next;
            }
            else{
                result->next=p1;
                p1=p1->next;
            }
            result=result->next;
    }
    if(p1!=NULL){
        result->next=p1;
    }
    if(p2!=NULL){
        result->next=p2;
    }
    return r->next;
  }
