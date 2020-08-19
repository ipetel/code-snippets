# This folder conations usful Bash commands
you can find in this folder few useful code snippets in Bash

## Install Python From Source 

https://docs.rstudio.com/resources/install-python-source/

## Fix Ubuntu locale error

the error:
_____________________________________________________________________
WARNING! Your environment specifies an invalid locale.
 The unknown environment variables are:
   LC_CTYPE=UTF-8 LC_ALL=
 This can affect your user experience significantly, including the
 ability to manage packages. You may install the locales by running:

   sudo apt-get install language-pack-UTF-8
     or
   sudo locale-gen UTF-8

To see all available language packs, run:
   apt-cache search "^language-pack-[a-z][a-z]$"
To disable this message for all users, run:
   sudo touch /var/lib/cloud/instance/locale-check.skip
_____________________________________________________________________

the fix:

1) sudo locale-gen "en_US.UTF-8"
1) sudo dpkg-reconfigure locales
1) a package configuration will be open - click on "all locales"
1) click on "en_US.UTF-8"
1) check the new configuration with "locale" command
