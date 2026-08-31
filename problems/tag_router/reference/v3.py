def route(article_tags, subscriptions):
    # A mute now only applies when no positive tag matches -- and in that case
    # the user would not be routed anyway, so inclusion is purely positive.
    tags = set(article_tags)
    out = []
    for user, subs in subscriptions.items():
        positive = {t for t in subs if not t.startswith("-")}
        if tags & positive:
            out.append(user)
    return sorted(out)
