import pyautogui
from time import sleep

# my modules
import screen_coords
import ocr
import game_assets
import mk_functions


def get_round() -> str:
    screen_capture = pyautogui.screenshot(region=screen_coords.round_loc)
    round_two_x = screen_capture.crop(screen_coords.round_loc_two)
    game_round = ocr.get_text_image(image=round_two_x, whitelist="0123456789-")
    if game_round in game_assets.rounds:
        return game_round
    else:
        round_one_x = screen_capture.crop(screen_coords.round_loc_one)
        game_round = ocr.get_text_image(image=round_one_x, whitelist="0123456789-")
        return game_round


def pickup_items():
    print("\tPicking up items")
    for index, coords in enumerate(screen_coords.item_pickup):
        mk_functions.right_click(coords)
        if index == 0:
            sleep(1.2)
        if index % 2 == 0:
            sleep(2)
        else:
            sleep(1.2)


def get_champ_carousel(tft_round):
    mk_functions.right_click(screen_coords.carousel_pos)
    if tft_round == '1-1':
        sleep(9.5)
        mk_functions.right_click(screen_coords.carousel_pos)
    elif tft_round == '2-4':
        sleep(5)
        for _ in range(6):
            sleep(3)
            mk_functions.right_click(screen_coords.carousel_pos)
    else:
        for _ in range(6):
            sleep(3)
            mk_functions.right_click(screen_coords.carousel_pos)


def check_alive():
    if ocr.get_text(screenxy=screen_coords.exit_now_loc, scale=3, psm=7, whitelist='') == 'EXIT NOW':
        return False
    elif ocr.get_text(screenxy=screen_coords.victory_loc, scale=3, psm=7, whitelist='') == 'CONTINUE':
        return False
    return True


def exit_game():
    mk_functions.left_click(screen_coords.exit_now)


def default_pos():
    mk_functions.left_click(screen_coords.default_pos)