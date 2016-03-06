def extract(item, container, morekeys=None):
    from jinja2.runtime import Undefined

    value = container[item]

    if value is not Undefined and morekeys is not None:
        if not isinstance(morekeys, list):
            morekeys = [morekeys]

        value = reduce(lambda d, k: d[k], morekeys, value)

    return value


class FilterModule(object):

    def filters(self):
        return {'extract': extract,
                }
