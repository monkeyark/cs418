CXX = g++
ECHO = echo
RM = rm -f

CXXLAGS = -std=c++20 -Wall -Werror -ggdb3 -funroll-loops
GTKFLAGS = `pkg-config --cflags --libs gtk4`
OPENGLFLAGS = `sdl2-config --cflags --libs`
CPPFLAGS=$(shell sdl2-config --cflags) $(CXXLAGS)
LDLIBS=$(shell sdl2-config --libs) -lGLEW $(EXTRA_LDLIBS)
EXTRA_LDLIBS?=-lGL

BIN = main
OBJS = main.o

all: $(BIN) etags

$(BIN): $(OBJS)
	@$(ECHO) Linking $@
	@$(CXX) $^ -o $@
-include $(OBJS:.o=.d)

%.o: %.cpp
	@$(ECHO) Compiling $<
	@$(CXX) $(CPPFLAGS) $(LDLIBS) -MMD -MF $*.d -c $<

.PHONY: all clean clobber etags

clean:
	@$(ECHO) Removing all generated files
	@$(RM) *.o $(BIN) *.d TAGS

clobber: clean
	@$(ECHO) Removing backup files
	@$(RM) *~ \#*

etags:
	@$(ECHO) Updating TAGS