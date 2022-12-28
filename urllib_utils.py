import urllib.request


def recu_down(url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
    except urllib.error.ContentTooShortError:
        print('Network conditions is not good. Reloading. .. ')
        recu_down(url, filename)
