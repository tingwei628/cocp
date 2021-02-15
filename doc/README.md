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
//compile c++ into executable(aarch64)
// -g, add gdb debug symbol
aarch64-linux-gnu-g++ -g -o [your_aarch64_executable] [your_cpp_file] -static

//convert c++ into shared object file(aarch64)
aarch64-linux-gnu-g++ [your_cpp_file] -o [your_arm_file(.o)]

//compile c++ into aarch64(.s)
aarch64-linux-gnu-g++ -S [your_cpp_file]

//assemble and link into executable(aarch64)
aarch64-linux-gnu-as a64.s -o a64.o && aarch64-linux-gnu-ld a64.o -o a64
```

```
  -S                       Compile only; do not assemble or link. => result is assembly file (.s)
  -c                       Compile and assemble, but do not link. => result is relocatable
  -o <file>                Place the output into <file>.          => result is shared object
```



## Execute
```
qemu-aarch64 [your_aarch64_executable]
```

## Debug
```
// window 1
qemu-aarch64 -g [your_por_number] [your_aarch64_executable]

// window 2
gdb-multiarch -q [your_aarch64_executable] -ex 'target remote :[your_por_number]'
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

## Reference:
https://azeria-labs.com/arm-on-x86-qemu-user
