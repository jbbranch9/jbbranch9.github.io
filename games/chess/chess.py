import pygame
pygame.init()

#initial values
frame_rate = 60
screen_width = 500
screen_height = 500
board_color = 1
player1_color = 1
player2_color = 1
piece_size_scalar = 2
board_grid = (((79, 79, 43, 43), (122, 79, 43, 43), (165, 79, 43, 43), (208, 79, 43, 43), (251, 79, 43, 43), (294, 79, 43, 43), (337, 79, 43, 43), (380, 79, 43, 43)),
              ((79, 122, 43, 43), (122, 122, 43, 43), (165, 122, 43, 43), (208, 122, 43, 43), (251, 122, 43, 43), (294, 122, 43, 43), (337, 122, 43, 43), (380, 122, 43, 43)),
              ((79, 165, 43, 43), (122, 165, 43, 43), (165, 165, 43, 43), (208, 165, 43, 43), (251, 165, 43, 43), (294, 165, 43, 43), (337, 165, 43, 43), (380, 165, 43, 43)),
              ((79, 208, 43, 43), (122, 208, 43, 43), (165, 208, 43, 43), (208, 208, 43, 43), (251, 208, 43, 43), (294, 208, 43, 43), (337, 208, 43, 43), (380, 208, 43, 43)),
              ((79, 251, 43, 43), (122, 251, 43, 43), (165, 251, 43, 43), (208, 251, 43, 43), (251, 251, 43, 43), (294, 251, 43, 43), (337, 251, 43, 43), (380, 251, 43, 43)),
              ((79, 294, 43, 43), (122, 294, 43, 43), (165, 294, 43, 43), (208, 294, 43, 43), (251, 294, 43, 43), (294, 294, 43, 43), (337, 294, 43, 43), (380, 294, 43, 43)),
              ((79, 337, 43, 43), (122, 337, 43, 43), (165, 337, 43, 43), (208, 337, 43, 43), (251, 337, 43, 43), (294, 337, 43, 43), (337, 337, 43, 43), (380, 337, 43, 43)),
              ((79, 380, 43, 43), (122, 380, 43, 43), (165, 380, 43, 43), (208, 380, 43, 43), (251, 380, 43, 43), (294, 380, 43, 43), (337, 380, 43, 43), (380, 380, 43, 43)))

#pygame infrastructure
window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()

#load images and audio
board = [pygame.transform.scale(pygame.image.load('images/chess_bw/board_alt.png'), (screen_width,screen_height)), pygame.transform.scale(pygame.image.load('images/chess_green/board_alt.png'), (screen_width,screen_height)), pygame.transform.scale(pygame.image.load('images/chess_pink/board_alt.png'), (screen_width,screen_height))]
player1_piece_sprites = [[pygame.transform.scale(pygame.image.load('images/chess_bw/white_pawn.png'), (pygame.image.load('images/chess_bw/white_pawn.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_bw/white_pawn.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_bw/white_knight.png'), (pygame.image.load('images/chess_bw/white_knight.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_bw/white_knight.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_bw/white_bishop.png'), (pygame.image.load('images/chess_bw/white_bishop.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_bw/white_bishop.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_bw/white_rook.png'), (pygame.image.load('images/chess_bw/white_rook.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_bw/white_rook.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_bw/white_queen.png'), (pygame.image.load('images/chess_bw/white_queen.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_bw/white_queen.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_bw/white_king.png'), (pygame.image.load('images/chess_bw/white_king.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_bw/white_king.png').get_height() * piece_size_scalar))],
                        [pygame.transform.scale(pygame.image.load('images/chess_green/white_pawn.png'), (pygame.image.load('images/chess_green/white_pawn.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_green/white_pawn.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_green/white_knight.png'), (pygame.image.load('images/chess_green/white_knight.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_green/white_knight.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_green/white_bishop.png'), (pygame.image.load('images/chess_green/white_bishop.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_green/white_bishop.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_green/white_rook.png'), (pygame.image.load('images/chess_green/white_rook.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_green/white_rook.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_green/white_queen.png'), (pygame.image.load('images/chess_green/white_queen.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_green/white_queen.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_green/white_king.png'), (pygame.image.load('images/chess_green/white_king.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_green/white_king.png').get_height() * piece_size_scalar))],
                        [pygame.transform.scale(pygame.image.load('images/chess_pink/white_pawn.png'), (pygame.image.load('images/chess_pink/white_pawn.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_pink/white_pawn.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_pink/white_knight.png'), (pygame.image.load('images/chess_pink/white_knight.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_pink/white_knight.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_pink/white_bishop.png'), (pygame.image.load('images/chess_pink/white_bishop.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_pink/white_bishop.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_pink/white_rook.png'), (pygame.image.load('images/chess_pink/white_rook.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_pink/white_rook.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_pink/white_queen.png'), (pygame.image.load('images/chess_pink/white_queen.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_pink/white_queen.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_pink/white_king.png'), (pygame.image.load('images/chess_pink/white_king.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_pink/white_king.png').get_height() * piece_size_scalar))]]
player2_piece_sprites = [[pygame.transform.scale(pygame.image.load('images/chess_bw/black_pawn.png'), (pygame.image.load('images/chess_bw/black_pawn.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_bw/black_pawn.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_bw/black_knight.png'), (pygame.image.load('images/chess_bw/black_knight.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_bw/black_knight.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_bw/black_bishop.png'), (pygame.image.load('images/chess_bw/black_bishop.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_bw/black_bishop.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_bw/black_rook.png'), (pygame.image.load('images/chess_bw/black_rook.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_bw/black_rook.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_bw/black_queen.png'), (pygame.image.load('images/chess_bw/black_queen.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_bw/black_queen.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_bw/black_king.png'), (pygame.image.load('images/chess_bw/black_king.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_bw/black_king.png').get_height() * piece_size_scalar))],
                        [pygame.transform.scale(pygame.image.load('images/chess_green/black_pawn.png'), (pygame.image.load('images/chess_green/black_pawn.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_green/black_pawn.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_green/black_knight.png'), (pygame.image.load('images/chess_green/black_knight.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_green/black_knight.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_green/black_bishop.png'), (pygame.image.load('images/chess_green/black_bishop.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_green/black_bishop.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_green/black_rook.png'), (pygame.image.load('images/chess_green/black_rook.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_green/black_rook.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_green/black_queen.png'), (pygame.image.load('images/chess_green/black_queen.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_green/black_queen.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_green/black_king.png'), (pygame.image.load('images/chess_green/black_king.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_green/black_king.png').get_height() * piece_size_scalar))],
                        [pygame.transform.scale(pygame.image.load('images/chess_pink/black_pawn.png'), (pygame.image.load('images/chess_pink/black_pawn.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_pink/black_pawn.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_pink/black_knight.png'), (pygame.image.load('images/chess_pink/black_knight.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_pink/black_knight.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_pink/black_bishop.png'), (pygame.image.load('images/chess_pink/black_bishop.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_pink/black_bishop.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_pink/black_rook.png'), (pygame.image.load('images/chess_pink/black_rook.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_pink/black_rook.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_pink/black_queen.png'), (pygame.image.load('images/chess_pink/black_queen.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_pink/black_queen.png').get_height() * piece_size_scalar)),
                         pygame.transform.scale(pygame.image.load('images/chess_pink/black_king.png'), (pygame.image.load('images/chess_pink/black_king.png').get_width() * piece_size_scalar, pygame.image.load('images/chess_pink/black_king.png').get_height() * piece_size_scalar))]]


def render_at_tile(tile_x, tile_y, piece):
    x = board_grid[tile_y][tile_x][0] + ((43 - piece.get_width())//2)
    y = board_grid[tile_y][tile_x][1] + ((43 - piece.get_height())//2)
    window.blit(piece, (x, y))

def draw_game_window():
    #draws background and sprites
    window.blit(board[board_color], (0, 0))
    for i in range(6):
        render_at_tile(i, 3, player1_piece_sprites[player1_color][i])
        render_at_tile(i+1, 4, player2_piece_sprites[player2_color][i])

    pygame.display.update()

run = True
while run:
    clock.tick(frame_rate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    draw_game_window()

pygame.quit()