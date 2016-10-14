#include <stdlib.h>
#include "node.c"

typedef struct linkedlist{
node_t *head;
node_t *tail;
int size;
}LL_t;

LL_t * LL_Create(void)
{
	LL_t * newList=malloc(sizeof(LL_t));
	newList->head=NULL;
	newList->tail=NULL;
	newList->size=0;
	return newList;
}

void LL_Destroy(LL_t * list)
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

void * LL_find(LL_t * ll,void * data)
{
  node_t * ptr=ll->head;
  while(ptr!=NULL)
    {
      if (ptr->data==data)
	return ptr;
      ptr=ptr->next;
    }
  return NULL;
}
