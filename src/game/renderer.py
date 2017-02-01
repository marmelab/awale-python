def render(board):
    render_str = ''

    half = int(len(board) / 2)

    render_str += '\n'
    # Board top
    render_str += display_row(board[:half])
    render_str += '\n'
    # Board bottom
    render_str += display_row(board[half:], half)
    render_str += '\n'

    return render_str


def display_row(board, start_index=0):
    # Display with index

    render_str = ''

    for index, row in enumerate(board):
        render_str += '{}({}) '.format(index + start_index, row)

    return render_str
