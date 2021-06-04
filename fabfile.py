from datetime import datetime
from fabric.api import local
from fabric.colors import green as _green, yellow as _yellow, red as _red
from os.path import exists


def makemigrations(app):
    local("python manage.py makemigrations {app}".format(app=app))


def migrations():
    local("python manage.py makemigrations")
    local("python manage.py migrate")


def run(port=8000):
    local("python manage.py runserver {port}".format(port=port))


def fix(name):
    local("python manage.py fix_{name}".format(name=name))


def drop_db():
    # local("python manage.py flush --noinput")
    local("python manage.py reset_db --noinput")


def dev():
    # drop_db()
    migrations()  # importante rodar nesta ordem, dados de producao
    fix("superuser")
    fix("questions")


def backup_db():
    today_label = datetime.now().strftime("%Y-%m-%d_%H-%M")
    local("mkdir -p _backups_db")
    local("python manage.py dumpdata --exclude contenttypes --indent=1 > _backups_db/backup_db_{}.json".format(today_label))


def rm_sqlite():
    local("rm project/db.sqlite3")


def shell():
    local("python manage.py shell_plus")


def test(modulo=None, clazz=None):
    if modulo and not clazz:
        local("python manage.py test {modulo}".format(modulo=modulo))
    elif modulo and clazz:
        local("python manage.py test {modulo}:{clazz}".format(modulo=modulo,
                                                              clazz=clazz))
    else:
        local("python manage.py test")


def run():
    local("python manage.py runserver 192.168.1.13:8000")

def fix_history():
    # Apenas use este metodo quando quiser o historico de uma base de dados que foi populada 
    # sem que a classe models tenha history = HistoricalRecords()
    local("python manage.py populate_history --auto")
