# MicroStrain Device Drivers

This repository contains the drivers to communicate with MicroStrain devices.

To install the drivers manually, you can do so with the provided files.

If you have any questions or run into any issues, please let us know! [MicroStrain Support Portal](https://support.microstrain.com)

## Linux
[WSDA-200 and WSDA-10X](https://github.com/LORD-MicroStrain/Drivers/releases/tag/linux-cp210x-0.2) - Used for the WSDA-200 and WSDA-10X BaseStations.

## Windows

[DPInst](https://technet.microsoft.com/en-us/ff544842(v=vs.96)) is a driver package installer tool provided by Microsoft in the Windows Driver Kit (WDK). For simplicity, we provide a copy of it [here](Windows/DPInst).

To install the drivers on Windows using DPInst, you can use the following command:
```
DPInst.exe /lm /sw /sa /PATH "Path/To/DriverFolder"
```

#### Wireless

[WSDA200](Windows/Wireless/WSDA200) - Used for the WSDA-200 USB BaseStations.

[CP210x](Windows/Wireless/CP210x) - Used for the WSDA-Base-10X BaseStations.

[WsdaUsbEthernet](Windows/Wireless/WsdaUsbEthernet) - Used for the WSDA-2000 communicating over USB.

#### Inertial

[ST_VCOM](Windows/Inertial/ST_VCOM) - Used for the 4-, 5- and 7-series product lines.

[3DM-GX3](Windows/Inertial/3DM_GX3) - Used for the 3DM-GX3 product line.

[EasySYNC](Windows/Inertial/EasySYNC) - Used for the RQ1 Starter Package.
