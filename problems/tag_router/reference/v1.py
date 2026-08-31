def route(article_tags, subscriptions):
    tags = set(article_tags)
    return sorted(user for user, subs in subscriptions.items() if tags & set(subs))
