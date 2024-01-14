import chess
import chess.engine

def display_board(board):
    return str(board)

def play_game():
    # Set the path to your Stockfish executable
    stockfish_path = r"C:\Users\hp\Desktop\stockfish\stockfish-windows-x86-64-avx2.exe"

    # Initialize the chess board
    board = chess.Board()

    # Get the strength of Stockfish from the user
    intel = 5
    # Set up the Stockfish engine with the specified strength
    with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
        while not board.is_game_over():
            # Display the current position
            display_board(board)

            # Get user move
# Get user move
            while True:
                try:
                    user_move = input("Enter your move (e.g., e2e4): ")
                    board.push_uci(user_move)
                    break
                except (chess.IllegalMoveError, chess.InvalidMoveError):
                    print("Sorry, this move can't be played. Try again.")
            
            # Display the updated position
            print("\n")
            display_board(board)


            # Get Stockfish move with the specified strength
            result = engine.play(board, chess.engine.Limit(time=2.0, depth=intel))
            stockfish_move = result.move
            print("\n")
            print("Stockfish played:", stockfish_move)
            board.push(stockfish_move)
			

        # Display the final position
        display_board("\n", board)

        # Print the game result
        print("Game Over. Result: ", board.result())

if __name__ == "__main__":
    play_game()