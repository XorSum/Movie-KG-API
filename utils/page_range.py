

def get_range(requests):
    start = max(int(requests.GET.get('start', 0)), 0)
    end = min(int(requests.GET.get('end', start + 20)), start + 20)
    return start,end