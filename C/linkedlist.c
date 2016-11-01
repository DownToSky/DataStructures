#include <stdlib.h>
#include "node.c"

typedef struct linkedlist{
node_t *head;
node_t *tail;
void (*freefunc)(void *);
int elementSize
int size;
}LL_t;

LL_t * LL_Create(int elemSize,void (*fn)(void *))
{
	LL_t * newList=malloc(sizeof(LL_t));
	if (LL_t == NULL)
		return NULL;
	newList->head=newList->tail=NULL;
	newList->size=0;
	newList->freefunc=fn;
	newList->elementSize=elemSize;
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
