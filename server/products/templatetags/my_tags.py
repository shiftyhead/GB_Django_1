from django.template import Library

register = Library()

@register.filter(name='cat_name')
def cat_name(self):
    return self.category.name
