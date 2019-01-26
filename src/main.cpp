
#include "game.hpp"

int main(int argc, char * argv[])
{

	Game *game = nullptr;

	game = new Game("Robattle X", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 800, 600, false);
	game->run();

	delete game;

	game = NULL;

	return 0;
}
