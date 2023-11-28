#include "lists.h"
/**
 * insert_node - adds a node in a sorted list
 * @head: pointer to  list
 * @number: add new node
 * Return: NULL or head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp, *prev;

	tmp = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}
	while (tmp)
	{
		if (tmp->n > number)
		{
			break;
		}
		prev = tmp;
		tmp = tmp->next;
	}
	new->next = tmp;
	prev->next = new;
	return (*head);
}
