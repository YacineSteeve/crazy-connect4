#!/usr/bin/sh

# This script is an all-in-one that helps to setup, run and rerun the app on Linux and MacOS.

if [ $(python3 --version | grep -c '3.10') -eq 1 ];
# Python version needed to run the app is 3.10
# (lower or higher not supported)
then
    if [ -d venv ];
    # A virtual environment exists (that is to say that the app has already been installed).
    then
        clear;
        venv/bin/python3 main.py; # Launch the app, assuming the virtualenv is active.
    else
        if sudo apt install -y python3.10-venv;
        then
            python3 -m venv venv;
            . venv/bin/activate;
            if venv/bin/pip3 install -r requirements.txt;
            then
                VLC_IS_OK=False
                if sudo apt-get install -y vlc;
                # Install the vlc package for Linux, used to play background music in the app
                then
                    VLC_IS_OK=True;
                fi

                # --- The .env file will be used in the program to check if vlc is installed ---
                touch .env
                echo "VLC_IS_OK=$VLC_IS_OK" >> .env
                # ------------------------------------------------------------------------------

                # --- Run tests and clear the generated files ---
                pytest --cov=src --cache-clear --verbosity=1;
                rm -rf __pycache__;
                rm -rf ./.pytest_cache;
                rm .coverage;
                # -------------------------------------------

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
