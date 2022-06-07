import ctypes

class Shaders:
    basic_vert_shader = """
    #version 330

    in vec2 pos;
    
    uniform mat4 model;

    void main()
    {
        gl_Position = model * vec4(pos, 0.0, 1.0);
    }
    """

    basic_frag_shader = """
    #version 330
    
    out vec4 f_color;
    
    uniform vec4 color;
    
    void main()
    {
        f_color = color;
    }
    """