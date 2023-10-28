#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop
 *
 * Return: Always returns 0, for success
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point, creates 5 zombie processes
 *
 * Return: Always returns 0, for success
 */

int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == -1)
		{
			perror("fork");
			return (1);
		}
		if (child_pid == 0)
		{
			return (0);
		}
		printf("Zombie process created, PID: %d\n", child_pid);
	}
	infinite_while();
	return (0);
}
