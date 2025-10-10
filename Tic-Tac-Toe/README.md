## Goals
### Board (3×3): Manages the board state and win/loss determination.
- Player: Encapsulates player information and move input.
- Game: Coordinates the game flow, switches players, handles invalid input, and checks end conditions.
Classes & Methods

### Board
- place_mark(row, col, mark) -> bool: Places a mark on an empty spot (includes legality check).
- is_full() -> bool: Checks for a draw (board full with no winner).
- check_winner() -> str | None: Returns 'X' / 'O' or None.
- valid_move(row, col) -> bool: Checks if the position is valid and empty.
- reset(), __str__() / display(): Display the board.

### Player
- name, mark ('X' / 'O')
- get_move(input_fn) -> tuple[int, int]: Gets a move from an input function (facilitates manual testing and injection).

### Game
- play(): Main loop.
- _switch_player(): Switches the active player.
- _handle_turn(): Handles a single turn, including invalid input handling.

``` bash
tic_tac_toe/
│
├── board.py
├── player.py
├── game.py
├── main.py
├── requirements.txt

```


