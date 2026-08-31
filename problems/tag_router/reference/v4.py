def route(article_tags, subscriptions):
    def norm(tag):
        return tag.strip().lower()

    tags = {n for n in map(norm, article_tags) if n}
    out = []
    for user, subs in subscriptions.items():
        positive = {n for n in map(norm, subs) if n and not n.startswith("-")}
        if tags & positive:
            out.append(user)
    return sorted(out)
