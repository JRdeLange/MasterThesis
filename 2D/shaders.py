

class Shaders:
    basic_vert_shader = """
    #version 330

    in vec2 pos;

    void main()
    {
        gl_Position = vec4(pos, 0.0, 1.0);
    }
    """

    basic_frag_shader = """
    #version 330
    
    out vec4 f_color
    
    void main()
    {
        f_color = (0.8, 0.8, 0.8, 1;
    }
    """