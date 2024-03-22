'''
Thread: An entity within a process that can be scheduled (aka "light weight process")
A process can spawn multiple threads

Pros:
- All threads within a process share the same memory
- light weight
- Starting a thread is faster > starting a process
- Great for I/O-bound tasks

Limitations:
- Threading is limited by GIL: Only one thread at a time
- No effect for CPU-bound tasks 
- Not interruptable/killable
- Careful with race conditions

'''