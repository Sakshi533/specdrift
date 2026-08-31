def route(article_tags, subscriptions):
    tags = set(article_tags)
    out = []
    for user, subs in subscriptions.items():
        muted = {t[1:] for t in subs if t.startswith("-")}
        positive = {t for t in subs if not t.startswith("-")}
        if not tags & muted and tags & positive:
            out.append(user)
    return sorted(out)
