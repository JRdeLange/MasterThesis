import ratcave as rc

class Shaders:
    basic_vert_shader = """
     #version 330

     layout(location = 0) in vec3 vertexPosition;
     uniform mat4 projection_matrix, view_matrix, model_matrix;
     out vec4 vVertex;

     void main()
     {
        
         vVertex = model_matrix * vec4(vertexPosition, 1.0);
         gl_Position = projection_matrix * view_matrix * vVertex;
     }
     """

    basic_frag_shader = """
     #version 330
     out vec4 final_color;
     uniform vec3 diffuse;
     void main()
     {
         final_color = vec4(1, 1, 1, 1.);
     }
     """

    basic_shader = rc.Shader(vert=basic_vert_shader, frag=basic_frag_shader)
