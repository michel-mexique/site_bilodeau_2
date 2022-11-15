# GUIDES SERVEUR LAUNCHING SCRIPT
import os
cmd = os.system

import requests

def show(text):
    string_ = ''.join([
        '\033[96m', # START OF ANSI SEQUENCE FOR CYAN COLOR
        '#' * 50,
        '\n',
        text,
        '\n',
        '#' * 50,
        '\033[0m', # END OF ANSI SEQUENCE FOR CYAN COLOR
    ])
    print(string_)

def wait():
    input(show('waiting for KEY PRESS'))

domains = [
    requests.get('https://api.ipify.org').text,
    'bilodeau.co'
]

if __name__ == '__main__':
    nom_site = 'site_bilodeau_2'

    show('UPDATE')
    cmd('sudo apt-get update')
    wait()
    
    cmd('sudo apt-get install libpq-dev python-dev')
    
    show('INSTALLATION DE PIP')
    cmd('sudo apt install python3-pip -y')
    wait()

    show('INSTALLATION DES PACKAGES')
    cmd('pip install -r requirements.txt')
    
    # TEST-RESOURCES
    cmd('sudo apt install python3-testresources')
    # INSTALL WAND AND IMAGEMAGICK TO HANDLE GIF IMAGES IN WAGTAIL
    cmd('pip install Wand')
    cmd('sudo apt-get install libmagickwand-dev')
    wait()

    show('ARRIMAGE AU DISQUE LIGHTSAIL POUR LE STOCKAGE DES GUIDES (DANS db.sqlite3')
    cmd('sudo mkdir ../guides_disk')
    cmd('sudo mount ../../../dev/xvdf ../guides_disk')
    cmd('sudo chmod 777 ../guides_disk')
    wait()
    
    show('AJOUT DE L\'IP PUBLIC DU SERVEUR AU FICHIER settings.py')
    ip = requests.get('https://api.ipify.org').text
    with open("site_bilodeau_2/site_bilodeau_2/settings.py", "a+") as f:
        # Append at the end of file
        f.write("\n")
        f.write("".join([
            "ALLOWED_HOSTS += ['", domains[0], "', '", domains[1],"']"
            ]))
        f.close()
    wait()

    show('INSTALLATION DE NGINX')
    cmd('sudo apt install nginx -y')
    nginx_site_content = ''.join(["""server {
    listen 80;
    server_name """, domains[0] + " " + domains[1],""";
        location / {
            include proxy_params;
            proxy_pass http://localhost:8000/;
            client_max_body_size 20M;
        }
    }
    """])
    cmd('sudo touch /etc/nginx/sites-available/site_bilodeau_2')
    cmd('sudo chmod -R 777 /etc/nginx/sites-available/site_bilodeau_2')
    cmd('sudo printf "' + nginx_site_content + '" >  /etc/nginx/sites-available/site_bilodeau_2')

    wait()

    cmd('sudo ln -s /etc/nginx/sites-available/site_bilodeau_2 /etc/nginx/sites-enabled')
    cmd('sudo systemctl restart nginx')
    wait()

    show('INSTALLING GUNICORN')
    cmd('sudo pip install gunicorn')
    wait()

    show('MIGRATION DE LA BASE DE DONNEES DJANGO ET COLLECTE'+
         'DES FICHIERS STATIQUES')
    cmd('python3 site_bilodeau_2/manage.py makemigrations')
    cmd('python3 site_bilodeau_2/manage.py migrate')
    
    #DEMMARAGE MANUELLE
    show("""
    FIN DE L'INITIALISATION DU SERVEUR
    POUR DEMARRER LE SITE, VEUILLEZ ENTRER LES TROIS COMMANDES SUIVANTES
    1. python3 site_bilodeau_2/manage.py collectstatic
    2. cd site_bilodeau_2
    3. gunicorn site_bilodeau_2.wsgi --bind 0.0.0.0:8000  --workers 1
    """)
    
    # DEMMARAGE AUTOMATIQUE
    # TODO NON-FONCTIONNEL POUR collectstatic
    # A RETRAVAILLER

    #cmd('python3 siteguides/manage.py collectstatic')
    #wait()

    #show('LANCEMENT DU SERVEUR')
    #cmd("""sh -c 'cd siteguides && gunicorn siteguides.wsgi --bind 0.0.0.0:8000  --workers 1'""")
    #wait()
