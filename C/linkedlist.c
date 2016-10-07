#include <stdlib.h>
#include "node.c"

typedef struct linkedlist{
node_t *head;
node_t *tail;
int size;
}LL_t;

LL_t * CreateLinkedList(void)
{
	LL_t * newList=malloc(sizeof(LL_t));
	newList->head=NULL;
	newList->tail=NULL;
	newList->size=0;
	return newList;
}

void DestroyLinkedList(LL_t * list)
{
	node_t * ptr= list->head;
	while(ptr!=NULL)
	{
		node_t * tmpPtr = ptr;
		ptr=ptr->next;
		DestroyNode(tmpPtr);
	}
	free(list);
}


