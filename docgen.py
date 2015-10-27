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
            docs += '### %s\n\n'% clsname
            cls = getattr(commonast, clsname)
            #cls.__doc__ = '%s(%s)\n%s' % (clsname, ', '.join(cls.__slots__), cls.__doc__) 
            #cls.__doc__ = '%s()\n%s' % (clsname, cls.__doc__)
            docs += cls.__doc__.rstrip() + '\n\n'

open('nodes.md', 'wb').write(docs.encode())
