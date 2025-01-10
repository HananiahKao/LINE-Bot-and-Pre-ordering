from pathlib import Path


class DBManager:
    dbpath = os.path.join(Path(__file__).resolve().parent.parent,"database/database.txt")
    def setValue(key,value):
        if dbpath.exists() and not key == '':
            dbpath.write_text('{}\n{}:{}'.format(dbpath.read_text(),key,value))
