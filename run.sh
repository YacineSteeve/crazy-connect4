#!/usr/bin/sh

if [ $(python3 --version | grep -c '3.10') -eq 1 ];
then
  if [ -d venv ];
  then
    clear;
    venv/bin/python3 main.py;
  else
    if sudo apt install -y python3.10-venv;
    then
      python3 -m venv venv;
      . venv/bin/activate;
      if venv/bin/pip3 install -r requirements.txt;
      then
        VLC_IS_OK=False
        if sudo apt-get install -y vlc;
        then
            VLC_IS_OK=True;
        fi
        touch .env
        echo "VLC_IS_OK=$VLC_IS_OK" >> .env
        pytest --cov=src --cache-clear --verbosity=1;
        rm -rf __pycache__;
        rm -rf ./.pytest_cache;
        rm .coverage;
        printf '\n\t\033[0;32m Crazy Connect 4 have been installed successfully !'
        printf 'Thanks for your trust and enjoy ! \033[0m\n\n';
        venv/bin/python3 main.py;
      fi
    fi
  fi
else
  printf '\n\t\033[0;31mInstallation failed ! Your Python version is too old to run the app.';
  printf '\n\tVersion found: %s , required: >= 3.10 \033[0m' "$(python3 --version)";
fi