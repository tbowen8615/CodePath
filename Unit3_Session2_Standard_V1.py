"""
def manage_stage_changes(changes):
    scheduled_stack = []
    canceled_stack = []

    for change in changes:
        if "Schedule" in change:
            scheduled_stack.append(change.split()[1])
        elif "Reschedule" in change:
            scheduled_stack.append(canceled_stack.pop())
        elif "Cancel" in change:
            canceled_stack.append(scheduled_stack.pop())
    
    return scheduled_stack

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) "
"""

"""
from collections import deque
def process_performance_requests(requests):
    request_queue = deque(sorted(requests, reverse = True))

    result = []

    for i, j in request_queue:
        result.append(j)

    return result

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))"
"""

def next_greater_event(schedule1, schedule2):
    ans = []

    
    return

print(next_greater_event([4, 1, 2], [1, 3, 4, 2])) 
print(next_greater_event([2, 4], [1, 2, 3, 4]))