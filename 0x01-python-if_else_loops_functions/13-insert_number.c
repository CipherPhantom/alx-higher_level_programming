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

	if (!head || !*head)
		return (NULL);

	current = *head;
	previous = NULL;
	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;

	while (number > current->n)
	{
		previous = current;
		current = current->next;
	}
	node->next = current;
	if (previous)
		previous->next = node;
	if (!previous)
		*head = node;
	return (node);
}
