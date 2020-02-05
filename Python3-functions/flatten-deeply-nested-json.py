'''
  this function is for dynamiclly flatten deeply nested JSON files, it based on:
  https://towardsdatascience.com/how-to-flatten-deeply-nested-json-objects-in-non-recursive-elegant-python-55f96533103d
'''
def flatten_json(nested_json):
    res = {}

    def flatten(x, name=''):
        if isinstance(x,dict):
            if not x:
                res[name[:-1]] = None
            else:
                for a in x:
                    flatten(x[a], name + a + '_')
        elif isinstance(x,list):
            if len(x)==0:
                res[name[:-1]] = None
            else:    
                i = 0
                for a in x:
                    flatten(a, name + str(i) + '_')
                    i += 1
        else:
            res[name[:-1]] = x

    flatten(nested_json)
    return res
