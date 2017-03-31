def transform(old):
    results = {}
    for point, values in old.items():
        for letter in values:
            results[letter.lower()] = point
    return results
