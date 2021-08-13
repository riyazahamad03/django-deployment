from django import template


register=template.Library()

def cut(value,arg):
    """ 
    cuts all value of arg from the strings
    """

    return value.replace(arg,'')

register.filter('cut',cut)
