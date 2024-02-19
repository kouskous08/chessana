import cv2
import chess
import time
import chess.engine
import numpy as np
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def bege_en_rouge(image_name):
    image = cv2.imread(image_name)
    image = image[1480:1480+1230, 870:870+1250]
    couleur_source = np.array([72, 155, 194])
    nouvelle_couleur = np.array([0, 0, 255])
    tolerance = 50
    masque = np.all(np.abs(image - couleur_source) < tolerance, axis=-1)
    image[masque] = nouvelle_couleur
    return image

def presence_rouge(square):
    couleur_a_detecter = np.array([0, 0, 255]) 
    tolerance = 10
    couleur_basse = couleur_a_detecter - tolerance
    couleur_haute = couleur_a_detecter + tolerance    
    masque = cv2.inRange(square, couleur_basse, couleur_haute)
    nombre_pixels_rouges = np.sum(masque > 0)
    return nombre_pixels_rouges > 3000


def chessboard_to_table(image):
    if image is not None:
        square_height = image.shape[0] // 8
        square_width = image.shape[1] // 8

        squares_results = {}

        for row in range(8):
            for col in range(8):
                x1, y1 = col * square_width, row * square_height
                x2, y2 = x1 + square_width, y1 + square_height
                square = image[y1:y2, x1:x2]
                label = f"{chr(ord('h') - row)}{8 - col}"
                red_present = presence_rouge(square)
                squares_results[label] = red_present
        
        return squares_results
    else:
        return None

def get_chessboard_table(image):# ma sta3meltachi
    image_path = image
    image = bege_en_rouge(image_path)
    squares = chessboard_to_table(image)
    return squares


def get_mvmnt(image1, image2):
    global stk
    chesstable1 = get_chessboard_table(image1)
    chesstable2 = get_chessboard_table(image2)
    mvm = []

    print("Chessboard 1:", chesstable1)
    print("Chessboard 2:", chesstable2)

    full_to_empty = [pos for pos, is_full in chesstable1.items() if is_full and not chesstable2[pos]]
    empty_to_full = [pos for pos, is_full in chesstable1.items() if not is_full and chesstable2[pos]]
    mvm.append(full_to_empty)
    mvm.append(empty_to_full)
    if len(stk) > 0 :
        if stk[-1][-2:] in mvm[0] and not chesstable2[stk[-1][-2:]] :
            mvm[0].remove(stk[-1][-2:])
            chesstable1[stk[-1][-2:]] = False
            stk.clear()
        else :
            mvm[1].append(stk[-1][-2:])
    return mvm


def form_stockfish(var):
    var2 = var[0][0]
    var3 = var[1][0]
    var = f"{var2}{var3}"
    return var

def check_file_exists(file_path):
    return os.path.exists(file_path)

class ChessboardHandler(FileSystemEventHandler):
    def __init__(self, engine, initial_image_path):
        self.engine = engine
        self.initial_image_path = initial_image_path
        self.current_image_path = None
        self.board = chess.Board()
        self.intel = 10

    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".jpg"):
            self.current_image_path = event.src_path
            self.process_image()

    def process_image(self):
            global board
            user_move = get_mvmnt(self.initial_image_path, self.current_image_path)
            if len(user_move[0]) > 0 :
                user_move = form_stockfish(user_move)
                print("User played:", user_move)
                self.board.push_uci(user_move)
                result = self.engine.play(self.board, chess.engine.Limit(time=2.0, depth=self.intel))
                stockfish_move = result.move
                if self.board.is_capture(stockfish_move) :
                    stk.append(stockfish_move.uci())
                    print("stockfish move : ", stockfish_move, "\n stk : ", stk)
                print("Stockfish played:", stockfish_move)
                self.board.push(stockfish_move)
                self.initial_image_path = self.current_image_path
            else :
                time.sleep(2)
stk = []

def start_watchdog(engine, initial_image_path):
    event_handler = ChessboardHandler(engine, initial_image_path)
    observer = Observer()
    observer.schedule(event_handler, path=r"C:\Users\hp\Desktop\connectmobile\img", recursive=False)
    observer.start()

def main():
    stockfish_path = r"C:\Users\hp\Desktop\stockfish\stockfish-windows-x86-64-avx2.exe"
    initial_image_path = r"C:\Users\hp\Desktop\connectmobile\img\nocha.jpg"
    board = chess.Board()

    with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
        start_watchdog(engine, initial_image_path)

        while not board.is_game_over():
            time.sleep(5)

if __name__ == "__main__":
    main()