def normalize_url(url):
    if url[:8] == 'https://':
        return url
    elif url[:7] == 'http://':
        return 'https://' + url[7:]
    else:
        return 'https://' + url
print(normalize_url('http://yandex.ru'))