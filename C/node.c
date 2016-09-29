#include <stdlib.h>

struct Node{
void* data
struct Node* next
}

void CreateNode(void* data)
{
	newNode=(*struct Node)malloc(sizeof(&data))
	newNode.data=data
	return newNode
}
