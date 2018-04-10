## Installing Drivers for Windows

[DPInst](https://technet.microsoft.com/en-us/ff544842(v=vs.96)) is a driver package installer tool provided by Microsoft in the Windows Driver Kit (WDK). For simplicity, we provide a copy of it here.

You can use the following commands to install the drivers:

### Wireless

[WSDA200](https://github.com/LORD-MicroStrain/Drivers/tree/master/Windows/Wireless/WSDA200) - Used for the WSDA-200 USB BaseStations.
```
DPInst.exe /lm /sw /sa /PATH "Path/To/WSDA200"
```

[CP210x](https://github.com/LORD-MicroStrain/Drivers/tree/master/Windows/Wireless/CP210x) - Used for the WSDA-Base-10X BaseStations.
```
DPInst.exe /lm /sw /sa /PATH "Path/To/CP210x"
```

[WsdaUsbEthernet](https://github.com/LORD-MicroStrain/Drivers/tree/master/Windows/Wireless/WsdaUsbEthernet) - Used for the WSDA-2000 communicating over USB.
```
DPInst.exe /lm /sw /sa /PATH "Path/To/WsdaUsbEthernet"
```

### Inertial

[ST_VCOM](https://github.com/LORD-MicroStrain/Drivers/tree/master/Windows/Inertial/ST_VCOM) - Used for the 3DM-GX4 and 3DM-GX5 product lines.
```
DPInst.exe /lm /sw /sa /PATH "Path/To/ST_VCOM"
```

[3DM-GX3](https://github.com/LORD-MicroStrain/Drivers/tree/master/Windows/Inertial/3DM_GX3) - Used for the 3DM-GX3 product line.
```
DPInst.exe /lm /sw /sa /PATH "Path/To/3DM_GX3"
```

[EasySYNC](https://github.com/LORD-MicroStrain/Drivers/tree/master/Windows/Inertial/EasySYNC) - Used for the RQ1 Starter Package.
```
DPInst.exe /lm /sw /sa /PATH "Path/To/EasySYNC"
```
