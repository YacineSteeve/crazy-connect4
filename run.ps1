#! /usr/bin/pwsh

# This script is an all-in-one that helps to setup, run and rerun the app on Windows.

if ($(python3 --version) | Select-String ".*3.10.*") {
    # Python version needed to run the app is 3.10
    # (lower or higher not supported)

    if (Test-Path -Path venv) {
        # A virtual environment exists (that is to say that the app has already been installed).
        Clear-Host
        venv\Scripts\python main.py  # Launch the app, assuming the virtualenv is active.
    } else {
        python3 -m venv venv
        venv\Scripts\activate
        if (venv\Scripts\pip3 install -r requirements.txt) {
            $VLC_IS_OK = "False"
            if (powershell.exe -ExecutionPolicy Bypass .\Deploy-VLCMediaPlayer.ps1 -DeploymentType "Install" -DeployMode "NonInteractive") {
                # Install VLC MediaPlayer, used to play background music in the app
                $VLC_IS_OK = "True"
            }

            # --- The .env file will be used in the program to check if vlc is installed ---
            New-Item .env
            "VLC_IS_OK=$VLC_IS_OK" >> .env
            # ------------------------------------------------------------------------------

            # --- Run tests and clear the generated files ---
            pytest --cov=src --cache-clear --verbosity=1
            Remove-Item -Recurse .\.pytest_cache
            Remove-Item .coverage
            # -------------------------------------------

            Write-Host "`nCrazy Connect 4 have been installed successfully" -ForegroundColor green
            Write-Host "Thank for your trust and enjoy ! `n" -ForegroundColor green

            venv\Scripts\python main.py
        }
    }
} else {
    Write-Host "`nInstallation failed ! Your Python version is too old to run the app." -ForegroundColor red
    Write-Host "Version found: $(python3 --version) , required: >= 3.10 `n" -ForegroundColor red
}
