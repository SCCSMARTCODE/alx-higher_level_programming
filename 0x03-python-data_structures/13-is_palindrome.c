/*
 * File: 100-is_palindrome.c
 * Auth: Your Name
 */

#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current_node = *head, *next_node, *prev_node = NULL;

	while (current_node)
	{
		next_node = current_node->next;
		current_node->next = prev_node;
		prev_node = current_node;
		current_node = next_node;
	}

	*head = prev_node;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *reversed, *middle;
	size_t length = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	current = *head;
	while (current)
	{
		length++;
		current = current->next;
	}
	current = *head;
	for (i = 0; i < (length / 2) - 1; i++)
		current = current->next;

	if ((length % 2) == 0 && current->n != current->next->n)
		return (0);
	current = current->next->next;
	reversed = reverse_listint(&current);
	middle = reversed;
	current = *head;
	while (reversed)
	{
		if (current->n != reversed->n)
			return (0);
		current = current->next;
		reversed = reversed->next;
	}
	reverse_listint(&middle);
	return (1);
}

