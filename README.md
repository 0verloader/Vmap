        
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
***Version 1.0.0***

What does Vmap do
---

Vmap uses parallel threading to connect to multiple ports of the target. If a connection is successful it means
that the port is open. Otherwise it is closed.

---

Clone and run
---
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
1.Insert number of parallel threads
2.Insert IP or domain name of the target
3.Insert minimum port to be checked (greater than 0)
4.Insert maximum port to be checked (less than 65536)
```

Contributors
---

- 0verloader <https://github.com/0verloader>

  Please report bugs to <konstantinosarakadakis@gmail.com>

License & copyright
---
Licenced under the [MIT licence](LICENSE).
