import commonast

docs = '# Node specifications\n\n'

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
            docs += '**%s**\n\n'% clsname
            cls = getattr(commonast, clsname)
            #cls.__doc__ = '%s(%s)\n%s' % (clsname, ', '.join(cls.__slots__), cls.__doc__) 
            #cls.__doc__ = '%s()\n%s' % (clsname, cls.__doc__)
            doc = '    ' + cls.__doc__.strip()
            lines = []
            for line in [line[4:] for line in doc.splitlines()]:
                indent = len(line) - len(line.lstrip())
                if indent == 4:  # new attribute
                    word, _, des = line.strip().partition(':')
                    line = '* ``%s``: %s' % (word, des)
                elif indent > 4:
                    line = '  ' + line.strip()  # continuation
                if line.startswith('Attributes:'):
                    continue
                lines.append(line)
            docs += '\n'.join(lines) + '\n\n'

open('nodes.md', 'wb').write(docs.encode())
