#include "lists.h"

/**
 * check_cycle - Checks if there is a loop in a linked list.
 * @list: linked list
 * Return: 0 if there is not a cycle, return 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *tmp = list;

	while (tmp != NULL && head != NULL && head->next != NULL)
	{
		head = head->next->next;
		tmp = tmp->next;

		if (head == tmp)
			return (1);
	}

	return (0);
}
