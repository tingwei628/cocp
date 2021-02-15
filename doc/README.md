## Install 
```
//toolchain
sudo apt install gcc-aarch64-linux-gnu
sudo apt install g++-aarch64-linux-gnu

//qemu (emulator) to run binaries of different architectures
sudo apt install qemu

//GDB with support for multiple architecture 
sudo apt install gdb-multiarch
```

## Debug
```
qemu-aarch64 -g [your_debug_port] [your_arm64_binary]
gdb-multiarch [your_arm64_binary]
```