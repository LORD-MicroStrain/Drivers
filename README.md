# LORD Sensing Drivers

This repository contains the drivers to communicate with LORD Sensing - MicroStrain devices.

The easiest way to install the drivers is to install our Desktop software, such as [SensorConnect](http://www.microstrain.com/software/sensorconnect). However, if you want to install the drivers manually, you can do so with the provided files.

## Linux
[WSDA-200 and WSDA-10X](https://github.com/LORD-MicroStrain/Drivers/releases/tag/linux-cp210x-0.2) - Used for the WSDA-200 and WSDA-10X BaseStations.

## Windows

[DPInst](https://technet.microsoft.com/en-us/ff544842(v=vs.96)) is a driver package installer tool provided by Microsoft in the Windows Driver Kit (WDK). For simplicity, we provide a copy of it [here](https://github.com/LORD-MicroStrain/Drivers/tree/master/Windows/DPInst).

To install the drivers on Windows using DPInst, you can use the following command:
```
DPInst.exe /lm /sw /sa /PATH "Path/To/DriverFolder"
```

#### Wireless

[WSDA200](https://github.com/LORD-MicroStrain/Drivers/tree/master/Windows/Wireless/WSDA200) - Used for the WSDA-200 USB BaseStations.

[CP210x](https://github.com/LORD-MicroStrain/Drivers/tree/master/Windows/Wireless/CP210x) - Used for the WSDA-Base-10X BaseStations.

[WsdaUsbEthernet](https://github.com/LORD-MicroStrain/Drivers/tree/master/Windows/Wireless/WsdaUsbEthernet) - Used for the WSDA-2000 communicating over USB.

#### Inertial

[ST_VCOM](https://github.com/LORD-MicroStrain/Drivers/tree/master/Windows/Inertial/ST_VCOM) - Used for the 3DM-GX4 and 3DM-GX5 product lines.

[3DM-GX3](https://github.com/LORD-MicroStrain/Drivers/tree/master/Windows/Inertial/3DM_GX3) - Used for the 3DM-GX3 product line.

[EasySYNC](https://github.com/LORD-MicroStrain/Drivers/tree/master/Windows/Inertial/EasySYNC) - Used for the RQ1 Starter Package.
