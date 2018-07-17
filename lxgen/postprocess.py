from sympy import latex, sympify


def to_latex(obj, **kwargs):
    transform_str = kwargs.pop('transform_str', False)

    if transform_str:
        return str(latex(sympify(obj), **kwargs))
    else:
        return str(latex(sympify(obj), **kwargs)) if not isinstance(obj, str) else obj
