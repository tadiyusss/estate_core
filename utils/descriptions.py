import re
def to_slug(text):
    """
    Converts a given text to a URL-friendly slug.
    """
    text = text.lower()
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'[^a-z0-9-]', '', text)
    text = text.strip('-')
    return text