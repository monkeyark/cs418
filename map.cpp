// #include <iostream>
// #include "shapes.hpp"
// #include "trapezoidal.hpp"

// #include <cstdlib>

// /* Use glew.h instead of gl.h to get all the GL prototypes declared */
// #include <GL/glew.h>
// /* Using SDL2 for the base window and OpenGL context init */
// #include <SDL2/SDL.h>

// using std::cout;
// using std::cin;
// using std::cerr;
// using std::endl;


// GLuint program;
// GLint attribute_coord2d;

// bool init_resources() {
// 	GLint compile_ok = GL_FALSE, link_ok = GL_FALSE;
	
// 	GLuint vs = glCreateShader(GL_VERTEX_SHADER);

// 	// GLSL version
// 	const char* version;
// 	int profile;
// 	SDL_GL_GetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, &profile);
// 	if (profile == SDL_GL_CONTEXT_PROFILE_ES)
// 		version = "#version 100\n";  // OpenGL ES 2.0
// 	else
// 		version = "#version 120\n";  // OpenGL 2.1

// 	const GLchar* vs_sources[] = {
// 		version,
// 		"attribute vec2 coord2d;                  "
// 		"void main(void) {                        "
// 		"  gl_Position = vec4(coord2d, 0.0, 1.0); "
// 		"}"
// 	};
// 	glShaderSource(vs, 2, vs_sources, NULL);
// 	glCompileShader(vs);
// 	glGetShaderiv(vs, GL_COMPILE_STATUS, &compile_ok);
// 	if (!compile_ok) {
// 		cerr << "Error in vertex shader" << endl;
// 		return false;
// 	}
	
// 	GLuint fs = glCreateShader(GL_FRAGMENT_SHADER);
// 	const GLchar* fs_sources[] = {
// 		version,
// 		"void main(void) {        "
// 		"  gl_FragColor[0] = 0.0; "
// 		"  gl_FragColor[1] = 0.0; "
// 		"  gl_FragColor[2] = 1.0; "
// 		"}"
// 	};
// 	glShaderSource(fs, 2, fs_sources, NULL);
// 	glCompileShader(fs);
// 	glGetShaderiv(fs, GL_COMPILE_STATUS, &compile_ok);
// 	if (!compile_ok) {
// 		cerr << "Error in fragment shader" << endl;
// 		return false;
// 	}
	
// 	program = glCreateProgram();
// 	glAttachShader(program, vs);
// 	glAttachShader(program, fs);
// 	glLinkProgram(program);
// 	glGetProgramiv(program, GL_LINK_STATUS, &link_ok);
// 	if (!link_ok) {
// 		cerr << "Error in glLinkProgram" << endl;
// 		return false;
// 	}
	
// 	const char* attribute_name = "coord2d";
// 	attribute_coord2d = glGetAttribLocation(program, attribute_name);
// 	if (attribute_coord2d == -1) {
// 		cerr << "Could not bind attribute " << attribute_name << endl;
// 		return false;
// 	}
	
// 	return true;
// }

// void render(SDL_Window* window) {
// 	/* Clear the background as white */
// 	glClearColor(1.0, 1.0, 1.0, 1.0);
// 	glClear(GL_COLOR_BUFFER_BIT);
	
// 	glUseProgram(program);
// 	glEnableVertexAttribArray(attribute_coord2d);
// 	GLfloat triangle_vertices[] = {
// 	    0.0,  0.8,
// 	   -0.8, -0.8,
// 	    0.8, -0.8,
// 	};
// 	/* Describe our vertices array to OpenGL (it can't guess its format automatically) */
// 	glVertexAttribPointer(
// 		attribute_coord2d, // attribute
// 		2,                 // number of elements per vertex, here (x,y)
// 		GL_FLOAT,          // the type of each element
// 		GL_FALSE,          // take our values as-is
// 		0,                 // no extra data between each position
// 		triangle_vertices  // pointer to the C array
// 						  );
	
// 	/* Push each element in buffer_vertices to the vertex shader */
// 	glDrawArrays(GL_TRIANGLES, 0, 3);
	
// 	glDisableVertexAttribArray(attribute_coord2d);

// 	/* Display the result */
// 	SDL_GL_SwapWindow(window);
// }

// void free_resources() {
// 	glDeleteProgram(program);
// }

// void mainLoop(SDL_Window* window) {
// 	while (true) {
// 		SDL_Event ev;
// 		while (SDL_PollEvent(&ev)) {
// 			if (ev.type == SDL_QUIT)
// 				return;
// 		}
// 		render(window);
// 	}
// }

// int main(int argc, char* argv[]) {
// 	/* SDL-related initialising functions */
// 	SDL_Init(SDL_INIT_VIDEO);
// 	SDL_Window* window = SDL_CreateWindow("My First Triangle",
// 		SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
// 		640, 480,
// 		SDL_WINDOW_RESIZABLE | SDL_WINDOW_OPENGL);
// 	SDL_GL_CreateContext(window);
	
// 	/* Extension wrangler initialising */
// 	GLenum glew_status = glewInit();
// 	if (glew_status != GLEW_OK) {
// 		cerr << "Error: glewInit: " << glewGetErrorString(glew_status) << endl;
// 		return EXIT_FAILURE;
// 	}

// 	/* When all init functions run without errors,
// 	   the program can initialise the resources */
// 	if (!init_resources())
// 		return EXIT_FAILURE;

// 	/* We can display something if everything goes OK */
// 	mainLoop(window);
	
// 	/* If the program exits in the usual way,
// 	   free resources and exit with a success */
// 	free_resources();

// 		// /* Draws points */
// 	// glBegin(GL_POINTS);
// 	// 	glVertex2f(0.5f, 0.5f); 
// 	// 	glVertex2f(0.5f, -0.5f); 
// 	// 	glVertex2f(-0.5f, 0.5f); 
// 	// 	glVertex2f(-0.5f, -0.5f); 
// 	// glEnd();
// 	// /* Draws two horizontal lines */
// 	// glBegin(GL_LINES);
// 	// glVertex2f(0.5f, 0.5f); 
// 	// glVertex2f(-0.5f, 0.5f); 
// 	// glVertex2f(-0.5f, -0.5f); 
// 	// glVertex2f(0.5f, -0.5f); 
// 	// glEnd();
// 	// /* Draws a square */
// 	// glBegin(GL_LINE_LOOP);
// 	// glVertex2f(0.5f, 0.5f); 
// 	// glVertex2f(-0.5f, 0.5f); 
// 	// glVertex2f(-0.5f, -0.5f); 
// 	// glVertex2f(0.5f, -0.5f); 
// 	// glEnd();
// 	// /* Draws a 'C' */
// 	// glBegin(GL_LINE_STRIP);
// 	// glVertex2f(0.5f, 0.5f); 
// 	// glVertex2f(-0.5f, 0.5f); 
// 	// glVertex2f(-0.5f, -0.5f); 
// 	// glVertex2f(0.5f, -0.5f); 
// 	// glEnd();

// 	// Point p1;
// 	// Point p2;
// 	// int nx, ny;
// 	// int dx, dy;
// 	// cout << "Enter p1: ";
// 	// cin >> nx >> ny;
// 	// p1.set(nx, ny);

// 	// cout << "Enter p2: ";
// 	// cin >> nx >> ny;
// 	// p2.set(nx, ny);
// 	// p1.print();
// 	// cout << ", ";
// 	// p2.print();
// 	// cout << endl;

// 	// cout << "Enter p2 changes: ";
// 	// cin >> dx >> dy;
// 	// while(!cin.eof())
// 	// {
// 	// 	p2.move(dx, dy);
// 	// 	p2.print();
// 	// 	cout << endl;
// 	// 	cin >> dx >> dy;
// 	// }

// 	return EXIT_SUCCESS;
// }


// Draw four triangles on a red background
#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>

// Read a shader source from a file
// store the shader source in a std::vector<char>
void read_shader_src(const char *fname, std::vector<char> &buffer);

// Compile a shader
GLuint load_and_compile_shader(const char *fname, GLenum shaderType);

// Create a program from two shaders
GLuint create_program(const char *path_vert_shader, const char *path_frag_shader);

// Called when the window is resized
void GLFWCALL window_resized(int width, int height);

// Called for keyboard events
void keyboard(int key, int action);

// Render scene
void display(GLuint &vao);

// Initialize the data to be rendered
void initialize(GLuint &vao);

int main () {
	// Initialize GLFW
	if ( !glfwInit()) {
		std::cerr << "Failed to initialize GLFW! I'm out!" << std::endl;
		exit(-1);
	}

	// Use OpenGL 3.2 core profile
	glfwOpenWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
	glfwOpenWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
	glfwOpenWindowHint(GLFW_OPENGL_VERSION_MAJOR, 3);
	glfwOpenWindowHint(GLFW_OPENGL_VERSION_MINOR, 2);

	// Open a window and attach an OpenGL rendering context to the window surface
	if( !glfwOpenWindow(500, 500, 8, 8, 8, 0, 0, 0, GLFW_WINDOW)) {
		std::cerr << "Failed to open a window! I'm out!" << std::endl;
		glfwTerminate();
		exit(-1);
	}

	// Register a callback function for window resize events
	glfwSetWindowSizeCallback( window_resized );

	// Register a callback function for keyboard pressed events
	glfwSetKeyCallback(keyboard);	

	// Print the OpenGL version
	int major, minor, rev;
	glfwGetGLVersion(&major, &minor, &rev);
	std::cout << "OpenGL - " << major << "." << minor << "." << rev << std::endl;

	// Initialize GLEW
	glewExperimental = GL_TRUE;
	if(glewInit() != GLEW_OK) {
		std::cerr << "Failed to initialize GLEW! I'm out!" << std::endl;
		glfwTerminate();
		exit(-1);
	}

	// Create a vertex array object
	GLuint vao;

	// Initialize the data to be rendered
	initialize(vao);

	// Create a rendering loop
	int running = GL_TRUE;

	while(running) {
		// Display scene
		display(vao);

		// Pool for events
		glfwPollEvents();
		// Check if the window was closed
		running = glfwGetWindowParam(GLFW_OPENED);
	}

	// Terminate GLFW
	glfwTerminate();

	return 0;
}

// Render scene
void display(GLuint &vao) {
	glClear(GL_COLOR_BUFFER_BIT);

	glBindVertexArray(vao);
	glDrawArrays(GL_TRIANGLES, 0, 12);

	// Swap front and back buffers
	glfwSwapBuffers();
}

void initialize(GLuint &vao) {
	// Use a Vertex Array Object
	glGenVertexArrays(1, &vao);
	glBindVertexArray(vao);

	// 4 triangles to be rendered
	GLfloat vertices_position[24] = {
		0.0, 0.0,
		0.5, 0.0,
		0.5, 0.5,
		
		0.0, 0.0,
		0.0, 0.5,
		-0.5, 0.5,
		
		0.0, 0.0,
		-0.5, 0.0,
		-0.5, -0.5,		

		0.0, 0.0,
		0.0, -0.5,
		0.5, -0.5,
	};

	// Create a Vector Buffer Object that will store the vertices on video memory
	GLuint vbo;
	glGenBuffers(1, &vbo);

	// Allocate space and upload the data from CPU to GPU
	glBindBuffer(GL_ARRAY_BUFFER, vbo);
	glBufferData(GL_ARRAY_BUFFER, sizeof(vertices_position), vertices_position, GL_STATIC_DRAW);	

	GLuint shaderProgram = create_program("shaders/vert.shader", "shaders/frag.shader");

	// Get the location of the attributes that enters in the vertex shader
	GLint position_attribute = glGetAttribLocation(shaderProgram, "position");

	// Specify how the data for position can be accessed
	glVertexAttribPointer(position_attribute, 2, GL_FLOAT, GL_FALSE, 0, 0);

	// Enable the attribute
	glEnableVertexAttribArray(position_attribute);
}

// Called when the window is resized
void GLFWCALL window_resized(int width, int height) {
	// Use red to clear the screen
	glClearColor(1, 0, 0, 1);

	// Set the viewport
	glViewport(0, 0, width, height);

	glClear(GL_COLOR_BUFFER_BIT);
	glfwSwapBuffers();
}

// Called for keyboard events
void keyboard(int key, int action) {
	if(key == 'Q' && action == GLFW_PRESS) {
		glfwTerminate();
		exit(0);
	}
}

// Read a shader source from a file
// store the shader source in a std::vector<char>
void read_shader_src(const char *fname, std::vector<char> &buffer) {
	std::ifstream in;
	in.open(fname, std::ios::binary);

	if(in.is_open()) {
		// Get the number of bytes stored in this file
		in.seekg(0, std::ios::end);
		size_t length = (size_t)in.tellg();

		// Go to start of the file
		in.seekg(0, std::ios::beg);

		// Read the content of the file in a buffer
		buffer.resize(length + 1);
		in.read(&buffer[0], length);
		in.close();
		// Add a valid C - string end
		buffer[length] = '\0';
	}
	else {
		std::cerr << "Unable to open " << fname << " I'm out!" << std::endl;
		exit(-1);
	}
}

// Compile a shader
GLuint load_and_compile_shader(const char *fname, GLenum shaderType) {
	// Load a shader from an external file
	std::vector<char> buffer;
	read_shader_src(fname, buffer);
	const char *src = &buffer[0];

	// Compile the shader
	GLuint shader = glCreateShader(shaderType);
	glShaderSource(shader, 1, &src, NULL);
	glCompileShader(shader);
	// Check the result of the compilation
	GLint test;
	glGetShaderiv(shader, GL_COMPILE_STATUS, &test);
	if(!test) {
		std::cerr << "Shader compilation failed with this message:" << std::endl;
		std::vector<char> compilation_log(512);
		glGetShaderInfoLog(shader, compilation_log.size(), NULL, &compilation_log[0]);
		std::cerr << &compilation_log[0] << std::endl;
		glfwTerminate();
		exit(-1);
	}
	return shader;
}

// Create a program from two shaders
GLuint create_program(const char *path_vert_shader, const char *path_frag_shader) {
	// Load and compile the vertex and fragment shaders
	GLuint vertexShader = load_and_compile_shader(path_vert_shader, GL_VERTEX_SHADER);
	GLuint fragmentShader = load_and_compile_shader(path_frag_shader, GL_FRAGMENT_SHADER);

	// Attach the above shader to a program
	GLuint shaderProgram = glCreateProgram();
	glAttachShader(shaderProgram, vertexShader);
	glAttachShader(shaderProgram, fragmentShader);

	// Flag the shaders for deletion
	glDeleteShader(vertexShader);
	glDeleteShader(fragmentShader);

	// Link and use the program
	glLinkProgram(shaderProgram);
	glUseProgram(shaderProgram);

	return shaderProgram;
}

