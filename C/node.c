#include <stdlib.h>

typedef struct node_t{
	void* data;
	struct node_t* next;
} node_t;

node_t * CreateNode(void * data)
{
	node_t *newNode=malloc(sizeof(node_t));
	if (newNode == NULL)
		return NULL;
	newNode->data=data;
	newNode->next = NULL;
	return newNode;
}

void DestroyNode(node_t * node)
{
	free(node);
}
