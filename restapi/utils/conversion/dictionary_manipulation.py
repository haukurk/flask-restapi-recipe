__author__ = 'Haukur Kristinsson'


def convert_keys_to_string(dictionary):
    """Recursively converts dictionary keys to strings."""
    if not isinstance(dictionary, dict):
        return dictionary
    return dict((str(k), convert_keys_to_string(v))
                for k, v in dictionary.items())


def etree_to_dict(t):
    d = {t.tag : map(etree_to_dict, t.iterchildren())}
    d.update(('@' + k, v) for k, v in t.attrib.iteritems())
    d['text'] = t.text
    return d