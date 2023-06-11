#include "lists.h"

/**
 * reverse_listint - Reverses a listint_t linked list.
 * @head: Pointer to the head pointer if the listint_t list
 *
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *next;

	if (!head)
		return (NULL);

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;
	return (*head);
}

/**
 * copy_listint - Cops a listint_t linked list.
 * @head: Pointer to the head pointer if the listint_t list
 *
 * Return: a pointer to the first node of the copied list
 */
listint_t *copy_listint(listint_t **head)
{
	listint_t *node, *newHead = NULL, *tmp = NULL, *current;

	if (!head)
		return (NULL);

	current = *head;
	while (current)
	{
		node = malloc(sizeof(listint_t));
		if (!node)
			return (NULL);
		node->n = current->n;
		node->next = NULL;
		if (!newHead)
		{
			newHead = node;
			tmp = newHead;
		}
		else
		{
			tmp->next = node;
			tmp = tmp->next;
		}
		current = current->next;

	}
	return (newHead);

}
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head pointer if the listint_t list
 *
 * Return: 1 if a palindrome and 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed, *current;
	int isPalindrome = 1;

	if (!head || !*head)
		return (isPalindrome);

	current = *head;
	reversed = copy_listint(head);
	reversed = reverse_listint(&reversed);

	while (current && reversed)
	{
		if (current->n != reversed->n)
		{
			isPalindrome = 0;
			break;
		}
		current = current->next;
		reversed = reversed->next;
	}
	free_listint(reversed);
	return (isPalindrome);
}
