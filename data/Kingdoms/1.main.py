def main():
    mode = input("1 - Player Mode, 2 - Autogame. Your choose:")
    if mode == "1":
        start_player_game()
    else:
        start_auto_game()

if __name__ == "__main__":
    main()