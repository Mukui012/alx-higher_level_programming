#include "lists.h"

/**
 * check_palindrome - checks for palindrome
 * @first: pointer to node
 * @last: pointer to node
 * Return: 1 if is a palindrome, 0 otherwise
 */
int check_palindrome(listint_t **first, listint_t *last)
{
	int n;

	if (last == NULL)
		return (1);
	n = check_palindrome(first, last->next);
	if (n == 0)
		return (0);
	if ((*first)->n == last->n)
		n = 1;
	else
		n = 0;
	*first = (*first)->next;
	return (n);
}

/**
 * is_palindrome - checks if linked list is palindrome
 * @head: pointer to pointer
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t **tmp, *curr;

	tmp = head;
	curr = *head;

	if (*head == NULL)
		return (1);
	return (check_palindrome(tmp, curr));
}
