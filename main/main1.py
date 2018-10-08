# In order to get this test1 module to run, I needed to add
# the directory to the memory file to the environmental variable "PYTHONPATH".
# After I did that, I had to add an __init__.py file to the memory folder so
# Python would consider the memory folder as a module and import it.

import test1

test1.printString("over here")