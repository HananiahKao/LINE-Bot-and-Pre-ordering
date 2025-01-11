from pathlib import Path
import os


class DBManager:
    dbpath = Path(__file__).resolve().parent/'database'/'database.txt'
    def write_value(self,key,value):
        if not self.dbpath.read_text() == '' and not key == '' and not self.keyExists(key):
            content = self.dbpath.read_text()
            if content.endswith('\n'):
                newlineOrNothing = ''
            else:
                newlineOrNothing = '\n'
            self.dbpath.write_text(f'{content}{newlineOrNothing}{key}:{value}')
        elif self.dbpath.read_text() == '':
            self.dbpath.write_text('{}:{}'.format(key,value))
        elif self.keyExists(key):
            file_content = self.dbpath.read_text()
            lines = file_content.splitlines(keepends=True)
            index = 0
            found = False
            for line in lines:
                if line.startswith(f'{key}:'):
                    if found:
                        lines[index] = ''
                    else:
                        lines[index] = '{}:{}\n'.format(key,value)
                        found = True
                index = index + 1
            self.dbpath.write_text("".join(lines))


    def key_exists(self,key):
        import re
        pattern = fr"^{key}:"
        file_content = self.dbpath.read_text()
        found = re.search(pattern, file_content, re.MULTILINE)
        if found:
            return True
        else:
            return False

    def read_value(self,key,default):
        if self.keyExists(key):
            file_content = self.dbpath.read_text()
            lines = file_content.splitlines(keepends=True)
            index = 0
            lineOfKey = ''
            for line in lines:
                if line.startswith(f'{key}:'):
                    lineOfKey = line
                    break
            if not lineOfKey == '':
                return lineOfKey[lineOfKey.index(':')+1:].replace('\n','')
            else:
                return default
        else:
            return default
