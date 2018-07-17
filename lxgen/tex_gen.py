import re
import os.path
import tempfile
import subprocess
import shutil

from typing import Dict, Any

REGEX = re.compile(r'%[ \t]*([a-zA-Z_][a-zA-Z_\d]*)[ \t]*%')


def tex_gen(template: str, pdf: str, data: Dict[str, Any], **kwargs):
    """
    :param template:
    :param pdf:
    :param data:
    :param kwargs:
    :return:
    """
    source_dst = kwargs.pop('source_dst', None)

    dst = tempfile.NamedTemporaryFile('w', suffix='.tex', delete=False)
    with open(template, 'r') as src:
        for s in src:
            dst.write(REGEX.sub(lambda match: str(data[match.group(1)]), s))
    dst.close()
    tex_compile(dst.name, pdf, **kwargs)
    if source_dst:
        shutil.copy(dst.name, source_dst)
    os.unlink(dst.name)


def tex_compile(src, dst, **kwargs):
    """
    :param src:
    :param dst:
    :param kwargs:
    :return:
    """
    latex_engine = kwargs.get('latex_engine', 'pdflatex')
    latex_options = kwargs.get('latex_options', [])

    with tempfile.TemporaryDirectory() as build_dir:
        subprocess.run(['latexmk',
                        '-f',
                        {'pdflatex': '-pdf', 'xelatex': '-xelatex', 'lualatex': '-lualatex'}[latex_engine],
                        '-interaction=nonstopmode',
                        '-synctex=1',
                        '-jobname=dst',
                        '--output-directory="{}"'.format(build_dir),
                        '--aux-directory="{}"'.format(build_dir),
                        *[''.join(['-latexoption=', s]) for s in latex_options],
                        src
                        ], check=True, shell=True, encoding='utf8')
        shutil.copy(os.path.join(build_dir, 'dst.pdf'), dst)
