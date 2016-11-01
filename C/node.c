#include <stdlib.h>

typedef struct node_t{
	void* data;
	struct node_t* next;
	void (*freefunc)(void *);
} node_t;

node_t * CreateNode(void * data,int elemSize,void (*fn)(void *))
{
	node_t *newNode=malloc(sizeof(node_t));
	if (newNode == NULL)
		return NULL;
	void * dat=malloc(sizeof(elemSize));
	newNode->data=data;
	newNode->next = NULL;
	newNode->freefunc=fn;
	return newNode;
}

void DestroyNode(node_t * node)
{
	(* node->freefunc(node->data));
	free(node);
}
