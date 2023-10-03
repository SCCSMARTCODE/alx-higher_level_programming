#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If then memory allocation fails - NULL.
 * Otherwise - then a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new_node;

	/* Allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	/* Initialize the value of the new node */
	new_node->n = number;

	/* Handle insertion at the beginning or for an empty list */
	if (current == NULL || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	/* Find the appropriate position for insertion */
	while (current && current->next && current->next->n < number)
		current = current->next;

	/* Perform the insertion */
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}

