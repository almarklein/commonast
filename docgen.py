"""
Small script to create the node specification in markdown.
"""

# import commonast
from flexx.pyscript import commonast

docs = '*(this document is auto-generated, do not edit)*\n\n'

docs += """
# Node specifications\n\n

Each node has a number of attributes as specified below. Each node also
has a `lineno` and `col_offset` property. Further it has a `tojson()`
method, and a tree can be reconstructed using `Node.fromjson()`. Running
`print(node)` will print a node's json.
\n
"""

docs += '## Enums\n\n'

docs += '`Node.OPS` - %s\n\n' % commonast.Node.OPS.__doc__
docs += '`Node.COMP` - %s\n\n' % commonast.Node.COMP.__doc__

code = open(commonast.__file__, 'rb').read().decode()

status = 0
for line in code.splitlines():
    if status == 0:
        if line.startswith('## --'):
            status = 1
    elif status == 1:
        if line.startswith('## --'):
            break
        elif line.startswith('## '):
            title = line[3:].strip()
            docs += '## %s\n\n' % title
        elif line.startswith('class '):
            clsname = line[6:].split('(')[0]
            docs += '#### class %s\n\n'% clsname
            cls = getattr(commonast, clsname)
            doc = '    ' + cls.__doc__.strip()
            lines = []
            for line in [line[4:] for line in doc.splitlines()]:
                indent = len(line) - len(line.lstrip())
                if indent == 4:  # new attribute
                    word, _, des = line.strip().partition(':')
                    line = '* ``%s``: %s' % (word, des)
                elif indent > 4:  # continuation
                    line = '  ' + line.strip()
                if line.startswith('Attributes:'):
                    continue
                lines.append(line)
            docs += '\n'.join(lines) + '\n\n'

open('nodes.md', 'wb').write(docs.encode())
