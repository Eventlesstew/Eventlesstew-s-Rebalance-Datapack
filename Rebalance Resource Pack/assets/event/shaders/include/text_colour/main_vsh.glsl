bool textColour_ingui(mat4 projectionMat) {
    #if !defined(IS_GUI)
    return projectionMat[2][3] == 0.0;
    #else
    return true;
    #endif
}
int textColour_toint(vec3 col) {
  ivec3 icol = ivec3(col*255);
  return (icol.r << 16) + (icol.g << 8) + icol.b;
}
vec3 textColour_tovec(int col) {
    return vec3(col >> 16, (col >> 8) % 256, col % 256) / 255.;
}

vec4 textColour_recolourText(vec4 colourAttribute, mat4 projectionMatrix) {
    if(!textColour_ingui(projectionMatrix)) return colourAttribute;
    return vec4(0.0,0.0,0.0,0.0);
}