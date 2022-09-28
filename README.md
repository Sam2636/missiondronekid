# missiondronekit


# Give lat long position of the copter in the terminal
```dronekit-sitl copter --home=12.976763,80.264469,0,180```

# step2
```mavproxy.py --master tcp:127.0.0.1:5760 --out udp:127.0.0.1:14551 --out udp:10.55.222.120:14550```

# starting mission planner in linux using mono
```mono MissionPlanner.exe```
conncet to the mission planner udp 14450

# After connecting copter with missionplanner start the python programm using this commad and call the udp port
```python connection_1.py --connect udp:127.0.0.1:14551```
