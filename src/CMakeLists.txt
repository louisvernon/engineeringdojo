find_package(PythonLibs)
#set(PYTHON_LIBRARIES /Users/vernon/usr/lib)
cmake_minimum_required(VERSION 2.6)

install(FILES libmym.py LIBRARY DESTINATION ${PYTHON_LIBRARIES})
enable_testing()
add_subdirectory(tests)
