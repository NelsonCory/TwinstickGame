from core.game import *
import sys


def main(argv):
	game = Game(argv[0])
	return game.run()


if __name__ == '__main__':
	sys.exit(main(sys.argv))
