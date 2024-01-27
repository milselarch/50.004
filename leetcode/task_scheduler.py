from collections import deque
from typing import List, Dict


SHOW = False


def log(*args, **kwargs):
    if SHOW:
        print(*args, **kwargs)


class Solution:
    @staticmethod
    def getBestFreeTask(
        tasks: set[str], task_counts: Dict[str, int]
    ) -> str:
        best_task = None
        best_count = float('-inf')

        for task in tasks:
            if task_counts[task] > best_count:
                best_count = task_counts[task]
                best_task = task

        return best_task

    def leastInterval(self, tasks: List[str], n: int) -> int:
        steps = 0
        last_add_step = 0
        running_tasks = deque()
        task_counts = {}

        for task in tasks:
            if task not in task_counts:
                task_counts[task] = 0

            task_counts[task] += 1

        free_tasks = set(task_counts.keys())

        while True:
            if len(free_tasks) > 0:
                # insert task into queue
                best_task = self.getBestFreeTask(free_tasks, task_counts)
                free_tasks.remove(best_task)
                running_tasks.append((best_task, steps))
                log('INSERT', best_task)
                last_add_step = steps

            steps += 1
            log('WAIT')

            # check if running tasks are done
            while len(running_tasks) > 0:
                task, insert_step = running_tasks[0]

                if steps - insert_step > n:
                    # check if task is done
                    running_tasks.popleft()
                    free_tasks.add(task)
                    task_counts[task] -= 1
                    log('CLEAR_TASK', task)

                    if task_counts[task] == 0:
                        # check if there are no more tasks of same type
                        # left to be done
                        del task_counts[task]
                        free_tasks.remove(task)
                else:
                    break

            log('----------------')
            if (len(task_counts) == 0) and (len(running_tasks) == 0):
                break

        return last_add_step + 1


if __name__ == '__main__':
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 2

    soln = Solution()
    duration = soln.leastInterval(tasks, n)
    print(duration)