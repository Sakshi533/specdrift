def table(results):
    stats = {}

    def team(name):
        return stats.setdefault(name, {"pts": 0, "gd": 0, "gf": 0})

    for home, away, hg, ag in results:
        h, a = team(home), team(away)
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

    return sorted(stats, key=lambda n: (-stats[n]["pts"], -stats[n]["gd"],
                                        -stats[n]["gf"], n))
