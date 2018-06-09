Title: Install GoogleTest on Mac OSX
Date: 2018-06-09 19:43
Category: C++
Tags: c++, testing, TDD


GoogleTest is an awesome C++ testing framework. It is easy to install and use.

First, download GoogleTest from github.
```shell
git clone https://github.com/google/googletest.git gtest
cd gtest
```
Then, use `cmake` to build the GoogleTest.
```shell
mkdir build
cd build
cmake ..
```
Use `ccmake .` to turn on a project cmake configuration TUI. Using the TUI, set `BUILD_GTEST: ON` and change `CMAKE_INSTALL_PREFIX`.
Finally, compile and install.
```shell
make
sudo make install
```

To use the GoogleTest, compile you own testing file by adding the following compiler argument:
```shell
g++ -lgtest -lgtest_main
```
