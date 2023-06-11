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
	reversed = reverse_listint(head);

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
	return (isPalindrome);
}
