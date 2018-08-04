# _*_ coding=utf-8 _*_

class text():
    header_list = """#include <fcntl.h>\n#include <inttypes.h>\n#include <stdio.h>\n#include <stdlib.h>\n#include <unistd.h>\n#include <string.h>\n"""
    header_inttype = "#include <inttypes.h>\n"
    main_sig = 'int main(int argc, char** argv)'
    pragma_weak_main = '#pragma weak main'
    pre_header_guard = "\n// first line intentionally left blank\n"
    header_guard_begin = "#ifndef _AUTO_XXX_H\n#define _AUTO_XXX_H\n"
    pragma_endif = "#endif\n"
    autogen_warning = "// automatically generated by faultreiber\n"
    last_comment = "// last line intentionally left blank\n\n"
    read_func_sig = "int read_structured_file(char* path)"
    #c_read_elem_sig = "XXX ft_read_YYY(int _fd) {\n"
    #c_read_elem_sig = "void ft_read_YYY(int _fd, XXX* dummyZZZ) {\n"
    c_read_elem_sig = "void ft_read_YYY(int _fd, XXX* dummy) {\n"
    c_read_elem_sig_h = "void ft_read_YYY(int _fd, XXX* dummy);\n"
    c_read_elem_sig_1 = "ft_read_XXX(_fd)"
    c_read_elem_sig_2 = "ft_read_XXX(_fd, YYY)"
    #c_read_elem_sig_2 = "ft_read_XXX(_fd, &YYY)"
    c_open_file = "int ft_read_file = open(_ft_file_path, RDONLY);\n"
    c_function_close = "}\n"
    c_function_dummy_dec = "XXX dummy;\n"
    c_function_return_type = "return dummy;\n"
    c_read_def_1 = "uint8_t XXX;\n"
    c_read_def_2 = "uint16_t XXX;\n"
    c_read_def_4 = "uint32_t XXX;\n"
    c_read_def_8 = "uint64_t XXX;\n"
    c_read_1 = "read(_fd, &XXX, sizeof(uint8_t));\n"
    c_read_2 = "read(_fd, &XXX, sizeof(uint16_t));\n"
    c_read_4 = "read(_fd, &XXX, sizeof(uint32_t));\n"
    c_read_8 = "read(_fd, &XXX, sizeof(uint64_t));\n"
    c_read_gen = "read(_fd, &XXX, sizeof(YYY));\n"
    c_read_gen_2 = "read(_fd, &XXX, YYY);\n"
    c_assign_struct = "XXX.YYY = ZZZ;\n"
    simple_loop = "for (int i = 0; i < XXX; ++i) {\nYYY}\n"
    c_read_leb_u_def = """
uint64_t read_leb_128_u(int _fd, int max_size) {
  uint8_t read_bytes = 0U;
  uint8_t byte = 0;
  uint64_t result = 0U;
  uint32_t shift = 0U;
  do {
    read(_fd, &byte, 1);read_bytes++;read_bytes++;
    result |= (byte & 0x7f) << shift;
    shift += 7;
  } while(((byte & 0x80) != 0) && (read_bytes < max_size));
  return result;
}"""

    c_read_leb_s_def = """
int64_t read_leb_128_s(int _fd, int max_size) {
  uint8_t byte;
  uint8_t read_bytes = 0U;
  uint8_t last_byte;
  int64_t result;
  uint32_t shift = 0U;
  read(_fd, &byte, 1);
  do {
    read(_fd, &byte, 1);read_bytes++;
    result |= (byte & 0x7f) << shift;
    last_byte = byte;
    shift += 7;
  } while(((byte & 0x80) != 0) && read_bytes < max_size);
  if ((last_byte & 0x40) != 0) result |= -(1 << shift);
  return result;
}"""
    c_read_leb_128_s_sig = "int64_t read_leb_128_s(int _fd, int max_size);\n"
    c_read_leb_128_u_sig = "uint64_t read_leb_128_u(int _fd, int max_size);\n"

    c_read_leb_macro_defs = """
#define READ_VAR_UINT_1(FD) read_leb128_u(FD, 1)
#define READ_VAR_UINT_7(FD) read_leb128_u(FD, 1)
#define READ_VAR_UINT_32(FD) read_leb128_u(FD, 5)
#define READ_VAR_INT_1(FD) read_leb128_s(FD, 1)
#define READ_VAR_INT_7(FD) read_leb128_s(FD, 1)
"""

    c_read_leb_macro_varuin1 = "READ_VAR_UINT_1(XXX)"
    c_read_leb_macro_varuin7 = "READ_VAR_UINT_7(XXX)"
    c_read_leb_macro_varuin32 = "READ_VAR_UINT_32(XXX)"
    c_read_leb_macro_varin1 = "READ_VAR_INT_1(XXX)"
    c_read_leb_macro_varin7 = "READ_VAR_INT_7(XXX)"
    c_read_leb_macro_varin32 = "READ_VAR_INT_32(XXX)"
    c_read_leb_128_u = "read_leb_128_u(_fd, 5);\n"
    c_read_leb_128_s = "read_leb_128_s(_fd, 5);\n"

    c_define_str_buff_size = "#define STR_BUFF_SIZE XXX"
    c_define_str_buff_grow_fact = "#define STR_BUFFER_GROW_FACTOR XXX"
    c_define_void_buff_size = "#define VOID_BUFF_SIZE XXX"
    c_define_void_buff_grow_fact = "#define VOID_BUFFER_GROW_FACTOR XXX"
    c_reserve_void_ptr = "malloc(XXX)"
