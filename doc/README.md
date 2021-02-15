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
## Compile
```
//compile c++ into aarch64
// -g, add gdb debug symbol
aarch64-linux-gnu-g++ -g -o [your_aarch64_binary] [your_cpp_file] -static
```

## Execute
```
qemu-aarch64 [your_aarch64_binary]
```

## Debug
```
// window 1
qemu-aarch64 -g [your_por_number] [your_aarch64_binary]

// window 2
gdb-multiarch -q [your_aarch64_binary] -ex 'target remote :[your_por_number]'
```

```
// quit gdb
(gdb) q
```

```
// free port used by gdb
netstat -anp|grep "port_number"
kill -9 [PID]
```
