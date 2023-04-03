# Vim

## Basic

- Editor with **mode**. Default to normal mode. Press the following keys to change to the mode.

  - `i` -> insert mode
  - `v` -> visual mode: select a block of text

  Press `esc` to return to the normal mode.

- Vim's interface is a programming language.
- Configure vim: `vim ~/.vimrc`
- Quit a window: `:q`
- Save a file: `:w`

## Movement

- `:sp`: open a new window with the same file buffer.
- Moving the cursor by char
  - j moves down
  - k moves up
  - h moves left
  - L moves left
- Moving the cursor by word
  - w: moves forward a word
  - b: moves backward a word
- Moving the cursor by line
  - 0: moves to the beginning
  - $ moves to the end
  - Caret moves to the first non-empty char
- Moving by multiple lines: `ctrl+U`, `ctrl+D`

## Editing

- `O`: create a new line under the current line, normal -> insert
- `d+w`: delete a word under normal
- `c+w`: change a word, normal -> insert
- `d+d`: delete a whole line, normal
- `d+c`: delete a whole line, normal -> insert
- `x`: delete a single char, normal
- `r+<a>`: change the char to `<a>`, normal
- `u`: undo a change, normal
- `ctrl+r`: redo a change, normal
- `yy:` copy a whole line; `yw`: copy a word; normal/visual -> normal
- `p`: paste; normal
- `~`: change the case of selected chars

## Counts

Count + operation

- `4j`: move down 4 lines
- `v3e`: select three words in visual mode

## Modifiers

