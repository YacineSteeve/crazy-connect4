#! /usr/bin/pwsh

if ($(python3 --version) | Select-String ".*3.10.*") {
    if (Test-Path -Path venv) {
        Clear-Host
        venv\Scripts\python main.py
    } else {
        python3 -m venv venv
        venv\Scripts\activate
        if (venv\Scripts\pip3 install -r requirements.txt) {
            $VLC_IS_OK = "False"
            if (powershell.exe -ExecutionPolicy Bypass .\Deploy-VLCMediaPlayer.ps1 -DeploymentType "Install" -DeployMode "NonInteractive") {
                $VLC_IS_OK = "True"
            }
            New-Item .env
            "VLC_IS_OK=$VLC_IS_OK" >> .env
            pytest --cov=src --cache-clear --verbosity=1
            Remove-Item -Recurse .\.pytest_cache
            Remove-Item .coverage
            Write-Host "`nCrazy Connect 4 have been installed successfully" -ForegroundColor green
            Write-Host "Thank for your trust and enjoy ! `n" -ForegroundColor green
            venv\Scripts\python main.py
        }
    }
} else {
    Write-Host "`nInstallation failed ! Your Python version is too old to run the app." -ForegroundColor red
    Write-Host "Version found: $(python3 --version) , required: >= 3.10 `n" -ForegroundColor red
}
