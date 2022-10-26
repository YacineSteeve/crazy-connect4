<h1 align="center">Crazy Connect 4</h1>

![Repo-size](https://img.shields.io/github/repo-size/YacineSteeve/crazy-connect4?style=flat-square)
![wakatime](https://wakatime.com/badge/user/c9625662-7df7-4bc4-b9f0-a23294301053/project/9c92a071-c5b4-4832-adf4-53439b843a79.svg?style=flat-square)

Crazy Connect 4 is a two-player game based on [Connect 4](https://en.wikipedia.org/wiki/Connect_Four).

The main features of this implementation are:
- Human VS Human mode
- Human VS AI mode
- Choice between different AIs:
    - with random-moves
    - with minimax algorithm, optimized with alpha-beta pruning *(Coming soon)*
    - with supervised machine learning *(Coming soon)*

## Setup and play

1. Open your terminal and **clone** the repository in a location of your choice by running:
    ```commandline
    git clone https://github.com/YacineSteeve/crazy-connect4
    ```

    > Or download the [zip file](https://github.com/YacineSteeve/crazy-connect4/archive/refs/heads/master.zip) 
   > if you don't have `git` installed, then extract and rename the folder into `crazy-connect4` .

2. Move to the **project directory**:
    ```bash
    cd crazy-connect4
    ```
   
3. Then **install** and **launch** the game:
    
    * ### Linux / MacOS
    Simply execute this command in your terminal:
    ```bash
    ./run.sh
    ```

    * ### Windows
        * Using the "geek way", and assuming you are using Windows PowerShell, execute:
            ```powershell
            .\run.ps1
            ```
        * Or click on `cc4.exe` in the project directory.


   > &#9888;&#65039; After exiting the game, you can **open it again just by running the same command** `./run.sh` ,
   > `.\run.ps1` , or `cc4.exe` according to your OS.

## Acknowledgement

This project is highly inspired from the beautiful job of [Merchrist KIKI](https://github.com/chrichri17).
Thank you again for your help and advice.

## License

[MIT](https://github.com/YacineSteeve/crazy-connect4/blob/master/LICENSE)
