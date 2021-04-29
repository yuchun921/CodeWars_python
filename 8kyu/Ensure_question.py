def ensure_question(s):
    if len(s) > 0:
        if s[-1] == '?':
            return s
    return f'{s}?'
