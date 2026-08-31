def order(jobs):
    idx = sorted(range(len(jobs)), key=lambda i: (-jobs[i][1], i))
    return [jobs[i][0] for i in idx]
