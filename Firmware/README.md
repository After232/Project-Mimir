# **Project Mimir Firmware**

The firmware installed aboard the Mark 2 prototype of the embosser uses a modified version of the Marlin firmware, version 2.0.6.1 installed using the MKS Robin E3D V1.1 board pinout settings. This firmware is based off of the STM32F1 Series microcontrollers, with the prototype’s specific version being the STM32F103RCT6. This came bundled with the MKS Robin E3D V1.1 board, and the firmware defaults were reconfigured as follows:
- Fan pinout set to PA2 pin (originally intended for Neopixel light outputs) with a MOSFET connected
- Reconfigured velocity, acceleration and steps/mm of Y, Z and E0 stepper motors
-- Maximum velocity for all three: 200 mm/s
-- Maximum acceleration for all three: 500 mm/s
