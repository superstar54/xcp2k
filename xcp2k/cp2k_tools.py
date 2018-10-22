class InputSection(object):
    """Represents a section of a CP2K input file"""
    def __init__(self, name, params=None):
        self.name = name.upper()
        self.params = params
        self.keywords = []
        self.subsections = []

    def write(self):
        """Outputs input section as string"""
        output = []
        for k in self.keywords:
            output.append(k)
        for s in self.subsections:
            if s.params:
                output.append('&%s %s' % (s.name, s.params))
            else:
                output.append('&%s' % s.name)
            for l in s.write():
                output.append('   %s' % l)
            output.append('&END %s' % s.name)
        return output

    def add_keyword(self, path, line, unique=True):
        """Adds a keyword to section."""
        parts = path.upper().split('/', 1)
        candidates = [s for s in self.subsections if s.name == parts[0]]
        if len(candidates) == 0:
            s = InputSection(name=parts[0])
            self.subsections.append(s)
            candidates = [s]
        elif len(candidates) != 1:
            raise Exception('Multiple %s sections found ' % parts[0])

        key = line.split()[0].upper()
        if len(parts) > 1:
            candidates[0].add_keyword(parts[1], line, unique)
        elif key == '_SECTION_PARAMETERS_':
            if candidates[0].params is not None:
                msg = 'Section parameter of section %s already set' % parts[0]
                raise Exception(msg)
            candidates[0].params = line.split(' ', 1)[1].strip()
        else:
            old_keys = [k.split()[0].upper() for k in candidates[0].keywords]
            if unique and key in old_keys:
                msg = 'Keyword %s already present in section %s'
                raise Exception(msg % (key, parts[0]))
            candidates[0].keywords.append(line)

    def get_subsection(self, path):
        """Finds a subsection"""
        parts = path.upper().split('/', 1)
        candidates = [s for s in self.subsections if s.name == parts[0]]
        if len(candidates) > 1:
            raise Exception('Multiple %s sections found ' % parts[0])
        if len(candidates) == 0:
            s = InputSection(name=parts[0])
            self.subsections.append(s)
            candidates = [s]
        if len(parts) == 1:
            return candidates[0]
        return candidates[0].get_subsection(parts[1])


def parse_input(inp):
    """Parses the given CP2K input string"""
    root_section = InputSection('CP2K_INPUT')
    section_stack = [root_section]

    for line in inp.split('\n'):
        line = line.split('!', 1)[0].strip()
        if len(line) == 0:
            continue

        if line.upper().startswith('&END'):
            s = section_stack.pop()
        elif line[0] == '&':
            parts = line.split(' ', 1)
            name = parts[0][1:]
            if len(parts) > 1:
                s = InputSection(name=name, params=parts[1].strip())
            else:
                s = InputSection(name=name)
            section_stack[-1].subsections.append(s)
            section_stack.append(s)
        else:
            section_stack[-1].keywords.append(line)

    return root_section


# return upper form of a dict
def capitalize_keys(d):
    result = {}
    for key, value in d.items():
        if isinstance(value, str):
            upper_key = key.upper()
            result[upper_key] = value.upper()
        else:
            upper_key = key.upper()
            result[upper_key] = value
    return result

