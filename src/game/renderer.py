def render(board):
    render_str = ''

    half = int(len(board) / 2)

    render_str += '\n'
    # Board top
    render_str += display_board_top(board, half)
    render_str += '\n'
    # Board bottom
    render_str += display_board_bottom(board, half)
    render_str += '\n'

    return render_str


def display_board_top(board, half):
    # Display with index
    render_str = ''
    for i in range(2*half-1, half-1, -1):
        render_str += '\t' + str(i) + ' [' + str(board[i]) + ']'
    return render_str


def display_board_bottom(board, half):
    # Display with index
    render_str = ''
    for i in range(0, half):
        render_str += '\t' + str(i) + ' [' + str(board[i]) + ']'
    return render_str


def render_score(score):
    score_str = "Score:\tPlayer 1: {}\tPlayer (2): {}\n"
    return score_str.format(score[0], score[1])
