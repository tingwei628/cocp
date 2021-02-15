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

## Execute
```
qemu-aarch64 [your_arm64_binary]
```

## Debug
```
qemu-aarch64 -g [your_debug_port] [your_arm64_binary]
gdb-multiarch [your_arm64_binary]
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
