'''
Process: An instance of a program (e.g a Python interpreter)
- Take advantage of multiple CPUs and cores
- Separate memory space -> Memory is not shared between processes
- Great for CPU-bound processing
- Processes are interuptable/killable
- One GIL for each process -> avoids GIL limitation

Limitations:
- Heavy weight
- Starting a process is slower than starting a thread
- More memory
- IPC (inter-process communication) is more complicated


'''