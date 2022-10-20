# Crazy Connect 4

Crazy Connect 4 is a two-player game based on [Connect 4](https://en.wikipedia.org/wiki/Connect_Four).

The main features of this implementation are:
- Human VS Human mode
- Human VS AI mode
- Choice between different AIs:
    - with random-moves
    - with minimax algorithm, optimized with alpha-beta pruning *(Coming soon)*
    - with supervised machine learning *(Coming soon)*

## Setup and play

### Linux / MacOS

1. Open your terminal and **clone** the repository in a location of your choice by running
    ```commandline
    git clone https://github.com/YacineSteeve/crazy-connect4
    ```

2. Move to the **project directory**:
    ```commandline
    cd crazy-connect4
    ```
   
3. Then **install** and **launch** the game by simply execute:
    ```commandline
    ./run
    ```

> &#9888;&#65039; After exiting the game, your can **open it again just by running the same command** `./run`.

--- 

### Windows

*(Automation coming soon)*

If you want to install it manually, follow the steps below:

- Make sure that the Python version installed on your computer is minimum **`3.10`**
- Create and activate a virtual environment named `venv`
- Install the dependencies from `requirements.txt` using `pip`
- Install VLC Media Player (optional)
- Create a file named `.env` in the project's root directory
- Add this exact line in the file : 
    * if VLC is installed: `VLC_IS_OK=True`
    * else: `VLC_IS_OK=False`
- Run the script `main.py` 

## Acknowledgement

This project is highly inspired from the beautiful job of [Merchrist KIKI](https://github.com/chrichri17).
Thank you again for your help and advice.

## License

[MIT](https://github.com/YacineSteeve/crazy-connect4/blob/master/LICENSE)
