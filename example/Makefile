CC      := winegcc
CFLAGS  += -mno-cygwin -mabi=ms -I../src
LDFLAGS += -mno-cygwin -mabi=ms -lnvml

example: example.o

clean:
	rm -f example.exe example.exe.so example.o

.PHONY: clean