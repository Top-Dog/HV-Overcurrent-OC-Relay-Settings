# HV-Overcurrent-OC-Relay-Settings
Overcurrent (OC) protection is a standard protection function offered by many relays in the HVAC power industry. However, sometimes field results arrive incomplete or incompressible, or electro-mechanical relays are used which do not have any recorded curve settings. This is a utility script to help find the best fit OC configuration settings by supplying an initial estimate/best guess for the settings.

From (1) two test points measuring the time-to-trip and injected fault current, (2) the known IEEE/IEC curve, (3) and CT ratio determine the best fit Time Multiplier (TMS) and Pickup (PU) settings.

Requires the SymPy libary. Get it using: ```pip install sympy```

The user just needs to change the configuration options to match their test case, for example:
```python
################## User Supplied Parameters ##################
CTRatio = 400/1
point1 = Point(0.7*CTRatio, 1.923)      # Test point one (x,y)
point2 = Point(3.5*CTRatio, 0.219)      # Test point two (x,y)
curve = Curve("IEC very inverse Class B")
hint = [0.2, 0.1]       # The approximate [PU, TMS] settings
##############################################################
```
