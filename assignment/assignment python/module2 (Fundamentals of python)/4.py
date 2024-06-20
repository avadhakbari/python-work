# How memory is managed in Python?



# Python uses a technique called reference counting to keep track of objects in memory. Each object in Python has a reference count associated with it, which is incremented whenever a new reference to the object is created, and decremented whenever a reference to the object is deleted or goes out of scope.

# In Python, memory management is handled by the Python Memory Manager. The memory manager takes care of allocating memory for Python objects and freeing up memory that is no longer in use through a process known as garbage collection. Python uses a combination of private heap space and the memory management functions provided by the underlying operating system.

# According to the Python memory management documentation,
#       Python has a private heap that stores our program’s objects and 
#       data structures. Python memory manager takes care of the bulk of the memory management work and
#       allows us to concentrate on our code.
        
#       two Types of memory allocation..
#            1. Static memory
#            2. Dynamic memory