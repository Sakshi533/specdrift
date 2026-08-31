def table(results):
    stats = {}

    def team(name):
        return stats.setdefault(name, {"pts": 0, "gd": 0, "gf": 0, "games": 0})

    for home, away, hg, ag in results:
        if home == away:
            raise ValueError(f"team {home!r} cannot play itself")
        if hg < 0 or ag < 0:
            raise ValueError("goals must be non-negative")
        h, a = team(home), team(away)
        h["games"] += 1
        a["games"] += 1
        h["gf"] += hg
        a["gf"] += ag
        h["gd"] += hg - ag
        a["gd"] += ag - hg
        if hg > ag:
            h["pts"] += 3
        elif hg < ag:
            a["pts"] += 3
        else:
            h["pts"] += 1
            a["pts"] += 1

    fallback = lambda n: (-stats[n]["gd"], -stats[n]["gf"], stats[n]["games"], n)
    order = sorted(stats, key=lambda n: (-stats[n]["pts"],) + fallback(n))

    def h2h_points(x, y):
        px = py = 0
        for home, away, hg, ag in results:
            if {home, away} != {x, y}:
                continue
            winner = home if hg > ag else away if ag > hg else None
            if winner is None:
                px += 1
                py += 1
            elif winner == x:
                px += 3
            else:
                py += 3
        return px, py

    out = []
    i = 0
    while i < len(order):
        j = i
        while j < len(order) and stats[order[j]]["pts"] == stats[order[i]]["pts"]:
            j += 1
        group = order[i:j]
        if len(group) == 2:
            px, py = h2h_points(group[0], group[1])
            if py > px:
                group = [group[1], group[0]]
        out.extend(group)
        i = j
    return out
