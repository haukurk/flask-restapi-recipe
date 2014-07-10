__author__ = 'haukurk'

import copy

def filter_strings_nested_dict(node, search_term):
    if isinstance(node, basestring):
        print node
        if node == search_term:
            return node
        else:
            return None
    else:
        dupe_node = {}
        for key, val in node.iteritems():
            cur_node = filter_strings_nested_dict(val, search_term)
            if cur_node:
                dupe_node[key] = cur_node
        return dupe_node or None


def filter_nested_dicts_values(node, vals):
    if isinstance(node, dict):
        retVal = {}
        for key in node:
            if key in vals:
                retVal[key] = copy.deepcopy(node[key])
            elif isinstance(node[key], list) or isinstance(node[key], dict):
                child = filter_nested_dicts_values(node[key], vals)
                if child:
                    retVal[key] = child
        if retVal:
             return retVal
        else:
             return None
    elif isinstance(node, list):
        retVal = []
        for entry in node:
            child = filter_nested_dicts_values(entry, vals)
            if child:
                retVal.append(child)
        if retVal:
            return retVal
        else:
            return None


def filter_nested_dicts_keys(node, vals):
    if isinstance(node, dict):
        retVal = {}
        for key in node:
            if key in vals:
                retVal[key] = copy.deepcopy(node[key])
            elif isinstance(node[key], list) or isinstance(node[key], dict):
                child = filter_nested_dicts_values(node[key], vals)
                if child:
                    retVal[key] = child
        if retVal:
             return retVal
        else:
             return None
    elif isinstance(node, list):
        retVal = []
        for entry in node:
            child = filter_nested_dicts_values(entry, vals)
            if child:
                retVal.append(child)
        if retVal:
            return retVal
        else:
            return None