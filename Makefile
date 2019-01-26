LDFLAGS = -lSDL2main -lSDL2 -lSDL2_image
FILES = src/main.cpp src/game.cpp

ifeq ($(OS), Windows_NT)
	LDFLAGS += -lmingw32
endif

all: bin
	g++ -o bin/game.exe $(FILES) $(LDFLAGS)

bin:
	mkdir bin

clean:
	rm -r bin
