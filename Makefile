CPP = g++
ECHO = echo
RM = rm -f

CPPFLAGS = -std=c++20 -Wall -Werror -ggdb3 -funroll-loops
GTKFLAGS = `pkg-config --cflags --libs gtk4`
OPENGLFLAGS = `sdl2-config --cflags --libs`

BIN = map
OBJS = map.o trapezoidal.o shapes.o

all: $(BIN) etags

$(BIN): $(OBJS)
	@$(ECHO) Linking $@
	@$(CXX) $^ -o $@
-include $(OBJS:.o=.d)

%.o: %.cpp
	@$(ECHO) Compiling $<
	@$(CPP) $(CPPFLAGS) $(OPENGLFLAGS) -MMD -MF $*.d -c $<

.PHONY: all clean clobber etags

clean:
	@$(ECHO) Removing all generated files
	@$(RM) *.o $(BIN) *.d TAGS

clobber: clean
	@$(ECHO) Removing backup files
	@$(RM) *~ \#*

etags:
	@$(ECHO) Updating TAGS