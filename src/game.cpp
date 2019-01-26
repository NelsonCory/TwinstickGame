#include "game.hpp"

Game::Game(const char * title, int xPos, int yPos, int width, int height, bool fullscreen)
{
	int flags = 0;
	if(fullscreen == true) {
		flags = SDL_WINDOW_FULLSCREEN;
	}

	if(SDL_Init(SDL_INIT_EVERYTHING) == 0) {
		std::cout << "SDL Initialized!" << "\n";

		SDL_version compiled;
		SDL_version linked;

		SDL_VERSION(&compiled);
		SDL_GetVersion(&linked);
		printf("We compiled against SDL version %d.%d.%d ...\n", compiled.major, compiled.minor, compiled.patch);
		printf("But we are linking against SDL version %d.%d.%d.\n", linked.major, linked.minor, linked.patch);

		_window = SDL_CreateWindow(title, xPos, yPos, width, height, flags);

		if(_window) {
			std::cout << "Window is created!" << "\n";
		}

		_buffer = SDL_CreateRenderer(_window, -1, 0);
		if(_buffer)
		{
			std::cout << "Render is a success!" << "\n";
		}
		_isRunning = true;
	} else {
		_isRunning = false;
	}
}

Game::~Game()
{
	SDL_DestroyWindow(_window);
	SDL_DestroyRenderer(_buffer);
	SDL_Quit();
}

void Game::handleEvents() {
	SDL_Event event;
	SDL_PollEvent(&event);

	switch (event.type) {
		case SDL_QUIT:
			_isRunning = false;
			break;
	}
}

void Game::update() {

}

void Game::render() {
	SDL_RenderClear(_buffer);

	SDL_RenderPresent(_buffer);
}

bool Game::running() {
	return _isRunning;
}

void Game::run() {
	while (running()) {
		handleEvents();
		update();
		render();
	}
}
