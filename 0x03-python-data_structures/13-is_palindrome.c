#include "lists.h"

/**
 * is_palindrome - checks  palindrome
 * @head: head
 * Return: 0 else 1
 */
int is_palindrome(listint_t **head)
{
    unsigned int len = 0, i;
    int values[10000]; /* Assuming a maximum of 10000 elements, adjust as needed */
    listint_t *temp;

    if (head == NULL || *head == NULL)
        return (1);

    temp = *head;
    while (temp) /* get len of list and store values */
    {
        values[len++] = temp->n;
        temp = temp->next;
    }

    for (i = 0; i < len / 2; i++)
    {
        if (values[i] != values[len - 1 - i])
            return (0);
    }

    return (1);
}
