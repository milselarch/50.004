import random

def trace_reqs(reqs, index, chain=()):
    for pre_req in reqs[index]:
        assert pre_req not in chain
        new_chain = chain + (pre_req,)
        trace_reqs(reqs, pre_req, new_chain)

    return True


def make_reqs(n=10):
    subjects = list(range(1, n+1))
    reqs = {k: [] for k in subjects}
    rand_subject_nos = subjects[::]
    random.shuffle(rand_subject_nos)

    for k in rand_subject_nos:
        while True:
            num_deps = random.randrange(0, n - 1)

            deps = subjects[::]
            random.shuffle(deps)
            deps = deps[:num_deps]
            reqs[k] = deps

            try:
                # print(reqs)
                trace_reqs(reqs, k)
            except AssertionError as e:
                continue
            else:
                break

    trace_reqs(reqs, 1)
    return reqs

# question 4 python code
def get_sems(reqs, target_mods=None, sem_map=None):
    if sem_map is None:
        sem_map = {}
    if target_mods is None:
        target_mods = list(reqs.keys())

    sems_total = 0

    for mod in target_mods:
        pre_reqs = reqs[mod]
        sems_needed = 0

        if len(pre_reqs) == 0:
            sem_map[mod] = 1
            continue

        if mod in sem_map:
            sems_total = max(sem_map[mod], sems_total)
            continue

        for pre_req in pre_reqs:
            if pre_req not in sem_map:
                get_sems(
                    reqs, target_mods=[pre_req],
                    sem_map=sem_map
                )

            sems_needed = max(sem_map[pre_req], sems_needed)

        sems = sems_needed + 1
        if mod not in sem_map:
            sem_map[mod] = 0

        sem_map[mod] = max(sem_map[mod], sems)
        sems_total = max(sems, sems_total)

    return sems_total


if __name__ == '__main__':
    random.seed(6)
    reqs = make_reqs()
    print(reqs)
    total = get_sems(reqs)
    print(total)