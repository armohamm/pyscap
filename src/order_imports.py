import os
import sys
import re

def do_file(path):
    in_imports = False
    lib_imports = []
    from_imports = []
    one_dot_imports = []
    two_dot_imports = []
    in_class = False

    with open(path, 'r', encoding='utf-8') as f:
        with open(path+'.new', 'w', encoding='utf-8') as g:
            for line in f:
                if in_class:
                    g.write(line)
                elif line.startswith('import '):
                    in_imports = True
                    lib_imports.append(line)
                elif line.startswith('from ..'):
                    in_imports = True
                    two_dot_imports.append(line)
                elif line.startswith('from .'):
                    in_imports = True
                    one_dot_imports.append(line)
                elif line.startswith('from'):
                    in_imports = True
                    from_imports.append(line)
                elif in_imports and line.strip() == '':
                    pass
                else:
                    if in_imports:
                        if len(lib_imports) > 0:
                            g.write(''.join(sorted(lib_imports)))
                            g.write('\n')
                        if len(from_imports) > 0:
                            g.write(''.join(sorted(from_imports)))
                            g.write('\n')
                        if len(two_dot_imports) > 0:
                            g.write(''.join(sorted(two_dot_imports)))
                            g.write('\n')
                        if len(one_dot_imports) > 0:
                            g.write(''.join(sorted(one_dot_imports)))
                            g.write('\n')
                        in_imports = False

                        g.write(line)
                    elif line.startswith('class '):
                        in_class = True
                        g.write(line)
                    else:
                        g.write(line)
    os.remove(path)
    os.rename(path+'.new', path)

def do_path(path):
    for entry in os.scandir(path):
        if entry.is_file():
            do_file(entry.path)
        else:
            do_path(entry.path)

do_path(sys.argv[1])
