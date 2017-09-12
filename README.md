Vmap
===         
```
               _______
               \      \        _____
                \      \      |     |
                 \      \     |     |
                  \      \    |     |
                   \      \   |     | ____    ____   ______       ___________
                    \      \  |     |/    \  /    \ |      \     |    ____   /
                     \      \ |     /      \/      \|       \    |   |   /  /  
                      \      \|    /    /\    /\    \   |\   \   |   |__/  /
                       \           |   |  \__/  |   |   |_\   \  |    ____/
                        \          |   |        |   |    __    \ |   |
                         \        /|   |        |   |   |   \   \|   |
                          \______/ |___|        |___|___|    \___\___|
            
                  
                                              A simple way to find open ports!
```

##How it works
```
Vmap uses parallel threading to connect to multiple ports. If the connection is successful it means
that the port is open. Otherwise it is closed.
```

##Clone and run
```
git clone https://github.com/0verloader/Vmap.git
```
```
cd Vmap
```
```
python Vmap.py
```

Once you have successfully run the program:
```
Insert IP or domain name of the target

Insert minimum port that will be checked (greater than 0)

Insert maximum port that will be checked (less than 65536)
```

##Contributors
0verloader
