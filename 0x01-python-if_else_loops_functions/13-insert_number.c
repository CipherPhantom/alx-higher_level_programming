#include "lists.h"
#include "stdlib.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 *
 * @head: Pointer to head node pointer.
 * @number: New number.
 *
 * Return: Address of the new node, or Null if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *current, *previous;

	if (!head)
		return (NULL);

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;
	
	if (!*head)
	{
		*head = node;
		return (node);
	}
	current = *head;
	previous = NULL;
	while (current)
	{
		if (current->n > number && !previous)
		{
			node->next = current;
			*head = node;
			break;
		}
		if (current->n > number)
		{
			previous->next = node;
			node->next = current;
			break;
		}
		previous = current;
		current = current->next;
	}
	if (!current)
		previous->next = node;

	return (node);
}
