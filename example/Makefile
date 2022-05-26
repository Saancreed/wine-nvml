CC     := winegcc -b x86_64-w64-mingw32
CFLAGS += -I../src
LDLIBS += -lnvml

example: example.o

clean:
	rm -f example.exe example.exe.so example.o

.PHONY: clean