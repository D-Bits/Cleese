"""
Run this script to do LAMP installation on Debian, 
or a Debian-based (Ubuntu, Mint, etc.) distro.
Based on Digital Ocean's tutorial:
https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04 
"""
from subprocess import call


# Install and configure an Apache2 server
def apache():

    # Prompt the user to login as root, since all following cmds 
    # will require root privledges 
    call('su')
    call('apt update')
    call('apt install apache2')
    # Whitelist Apache in UFW
    call('ufw allow in "Apache Full"')


# Install and configure a MySQL server
def mysql():

    call('apt install mysql-server')
    call('mysql_secure_installation')


# Install and configure PHP to work w/ Apache and MySQL
def php():

    call('apt install php libapache2-mod-php php-mysql')
    # Prompt the user to do appropriate directory configs w/ Nano
    call('nano /etc/apache2/mods-enabled/dir.conf')


def main():

    apache()
    mysql()
    php()


main()