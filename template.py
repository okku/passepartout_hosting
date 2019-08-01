import jinja2
import os

class LaxUndefined(jinja2.Undefined):
    __slots__ = ()

    def _do_nothing(self, *args, **kwargs):
        """Regular callback function for undefined objects that returns self on call
        """
        try:
            self._fail_with_undefined_error(self, *args, **kwargs)
        except self._undefined_exception:
            pass

        return self

    __add__ = __radd__ = __mul__ = __rmul__ = __div__ = __rdiv__ =\
    __truediv__ = __rtruediv__ = __floordiv__ = __rfloordiv__ =\
    __mod__ = __rmod__ = __pos__ = __neg__ = __call__ =\
    __getattr__ = __getitem__ = __lt__ = __le__ = __gt__ = __ge__ =\
    __int__ = __float__ = __complex__ = __pow__ = __rpow__ =\
    _do_nothing

    def __repr__(self):
        return '<Undefined: %s>' % self._undefined_hint

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), undefined=LaxUndefined)

def render(template, template_values):
    t = jinja_environment.get_template(template)
    return t.render(template_values)
