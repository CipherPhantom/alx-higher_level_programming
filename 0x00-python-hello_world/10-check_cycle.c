#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: Pointer to first node
 *
 * Return: 1, if cycle present and 0 if not.
 */

int check_cycle(listint_t *list)
{
	listint_t *current, *temp = NULL;
	int cycle = 0;

	current = list;

	while (current)
	{

		if (!current || !current->next || !current->next->next)
			break;

		if (!temp)
			temp = current->next->next;

		if (temp == current)
		{
			cycle = 1;
			break;
		}

		current = current->next;
		if (!temp->next || !temp->next->next)
			break;
		temp = temp->next->next;
	}
	return (cycle);
}
