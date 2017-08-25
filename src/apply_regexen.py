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
        r"'(enum|default|min|max|list|dict|required|nillable)':\s",
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
    with open(path, 'r') as f:
        with open(path+'.new', 'w') as g:
            for line in f:
                g_line = line
                for pattern, repl in subs:
                    g_line = re.sub(pattern, repl, g_line)
                g.write(g_line)
    os.remove(path)
    os.rename(path+'.new', path)

def regex_path(path):
    for entry in os.scandir(path):
        if entry.is_file():
            regex_file(entry.path)
        else:
            regex_path(entry.path)

regex_path(sys.argv[1])
