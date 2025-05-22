1. python comes with binaries i.e executables , builtins(like loop,execption,types,functions like print,len,max ,min , input)
   and standard libraries( file i/o,json,timedate,math,os,threading etc) , so in short it is a directory of files .
2. difference between builtins and standard lib is  builtins need not be imported while standard lib needs to be imported.
3. then there is a cocenpt of third party library .
4. builtins are present in builtin module ( there is a builtins module present and it can be imported too )
5. content of builtins can be viewed by dir(builtins) :-> o/p is list having defined references or variables .
6. so python is a directory and we can copy the same directory and can make multiple versions of same python release or versions of multiple python versions .
7. 3rd party libraries get installed in python dorectory and it is just again a file or folder , even the version changes the filename does not get change hence 
   multiple versions of same 3rd library is not possible to be present in directory at the same time i.e same file name cannot be present in a directory.
8. installation means the library files gets copied to the python directory
9. so to avoid this make 2 copies of python directory and install different versions of 3rd party library in different copies. make copies of python and copy different versions
   of library in that.
10. keep the base python as it is , donot change it , make copies and then use it . for every project make new copy of python and use it and install dependicies .
11. step 10 is called virtual enviorment , on widows it copies the file , while in linux it makes symlink 
12. pipenv,virtualenv,venv( builtin comes with python) 
13. all 3 copies the python directory and then give option to deactivate and activate the enviorment as per our need .
14. activate means in simple terms , when we use the activate and then use python then it should use the binaries of the copied python to run the code 
15. 3rd party library often rely on another 3rd party libraries i.e called library dependicies.
16. There is a concept of dependecy conflict or dependency hell. it means suppose we are using 2 

17. Instead of typing the complete path /usr/local/bin/python3.exe what we usually do we add this path to PATH variable and now we were able to type just the python3
18. so if we want to run different codes on dfferent versions of python the manually we have to add and remove the python executable path from the PATH variable and then keep
    updating the new and it becomes very tedious work .
19. to solve this 18 there is a activate command , it does not remove the value from the PATH but it adds the new path value at the starting so python3 hits the first one  
    and comes out of search and this gets active for current cmd session once it is closed it is gone so this is like adding on run time and removing it .
20. first decide the python version and this needs to be installed on our system , on windows always provide the full path .
21. python_path -m venv venv_name :-> venv_name directory gets cretaed in current directory 
22. insidne venv_name there is a script folder and then there is activate.bat , run this while some time we have to jsut run the activate not the activate.bat 
23. py --list tells how many versions present on your windows 
24. py --list-paths  to find the complete path of all python versions on windows . py --list is called pythojn launcher .
25. so when you run the activate and see the path you will find that the venv python binaries path is added at the top and once it is deactivated and then it gets removed autoamtically.
26. python.exe and pythonw.exe both are python interpreter and pythonw.exe is widnies version pf python interpreter(used for gui app mainly)















