#include "lists.h"

/**
 * check_cycle - check if linked list has a cycle in it
 * @list: head pointer of node
 * Return: 0 if there is no cycle else return 1
 */

int check_cycle(listint_t *list)
{
	listint_t *temp_p = list;
	listint_t *ptr_p = list;

	if (list == NULL)
		return (0);
	while (temp_p && ptr_p && ptr_p->next)
	{
		temp_p = temp_p->next;
		ptr_p = ptr_p->next->next;

		if (temp_p == ptr_p)
		{
			return (1);
		}
	}

	return (0);
}
