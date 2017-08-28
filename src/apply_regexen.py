import os
import sys
import re

subs = (
    (
        r"\s{12}'\{([^}]*?)\}([^']*?)': \{([^}]*?)\},?",
        r"@attribute(namespace='\1', local_name='\2', \3)",
    ),
    (
        r"\s{12}'([^']*?)': \{([^}]*?)\},?",
        r"@attribute(local_name='\1', \2)",
    ),
    (
        r"\s{12}\{'xmlns': '([^']+)', 'tag_name': '(.*?)'(, .*?)?\},?",
        r"@element(namespace='\1', local_name='\2'\3)",
    ),
    (
        r"\s{12}\{'tag_name': '(.*?)'(, .*?)?\},?",
        r"@element(local_name='\1'\2)",
    ),
    (
        r"'(enum|default|min|max|list|dict|required|nillable|key)':\s",
        r'\1=',
    ),
    (
        r"'in':\s",
        r"into=",
    ),
    (
        r"'type': '([^']+)'",
        r"type=\1",
    ),
    (
        r"'class': '([^']+)'",
        r"cls=\1",
    ),
    (
        r"logger = logging.getLogger\(__name__\)",
        r"logger = logging.getLogger(__name__)\n",
    )
)

def regex_file(path):
    in_defs = False
    with open(path, 'r', encoding='utf-8') as f:
        with open(path+'.new', 'w', encoding='utf-8') as g:
            for line in f:
                if re.fullmatch('\s+def', line):
                    in_defs = True

                if not in_defs:
                    g_line = line
                    for pattern, repl in subs:
                        g_line = re.sub(pattern, repl, g_line)
                    g.write(g_line)
                else:
                    g.write(line)
    os.remove(path)
    os.rename(path+'.new', path)

def regex_path(path):
    for entry in os.scandir(path):
        if entry.is_file():
            regex_file(entry.path)
        else:
            regex_path(entry.path)

regex_path(sys.argv[1])
