#ifndef Game_hpp
#define Game_hpp
#include "SDL2/SDL.h"
#include "SDL2/SDL_image.h"
#include <iostream>

class Game {
public:
	Game(const char * title, int xPos, int yPos, int width, int height, bool fullscreen);
	~Game();

	void handleEvents();
	void update();
	void render();

	bool running();

	void run();

private:

	bool _isRunning;
	SDL_Window * _window;
	SDL_Renderer * _buffer;

	const int maxFps = 60;

};
#endif
