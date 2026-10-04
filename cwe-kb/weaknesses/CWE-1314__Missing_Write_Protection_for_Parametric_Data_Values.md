# CWE-1314: Missing Write Protection for Parametric Data Values

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1314.html  

## Description
The device does not write-protect the parametric data values for sensors that scale the sensor value, allowing untrusted software to manipulate the apparent result and potentially damage hardware or cause operational failure.

## Extended Description
Various sensors are used by hardware to detect any devices operating outside of the design limits. The threshold limit values are set by hardware fuses or trusted software such as the BIOS. These limits may be related to thermal, power, voltage, current, and frequency. Hardware mechanisms may be used to protect against alteration of the threshold limit values by untrusted software. The limit values are generally programmed in standard units for the type of value being read. However, the hardware-sensor blocks may report the settings in different units depending upon sensor design and operation. The raw sensor output value is converted to the desired units using a scale conversion based on the parametric data programmed into the sensor. The final converted value is then compared with the previously programmed limits. While the limit values are usually protected, the sensor parametric data values may not be. By changing the parametric data, safe operational limits may be bypassed.

## Related Weaknesses
- ChildOf: CWE-862
- PeerOf: CWE-1299

## Common Consequences
- Scope: Availability; Impact: Quality Degradation, DoS: Resource Consumption (Other) — Sensor value manipulation, particularly thermal or power, may allow physical damage to occur or disabling of the device by a false fault shutdown causing a Denial-Of-Service.

## Potential Mitigations
- [Architecture and Design] Access controls for sensor blocks should ensure that only trusted software is allowed to change threshold limits and sensor parametric data.

## Demonstrative Examples (summary)
- Malicious software executes instructions to increase power consumption to the highest possible level while causing the clock frequency to increase to its maximum value. Such a program executing for an extended period of time would likely overheat the device, possibly resulting in permanent damage to the device. A ring, oscillator-based temperature sensor will generally report the sensed value as oscillator frequency rather than degrees centigrade. The temperature sensor will have calibration values that are used to convert the detected frequency into the corresponding temperature in degrees centigrade. Consider a SoC design where the critical maximum temperature limit is set in fuse values to 100C and is not modifiable by software. If the scaled thermal sensor output equals or exceeds this limit, the system is commanded to shut itself down. The thermal sensor calibration values are programmable through registers that are exposed to system software. These registers allow software to affect the converted temperature output such that the output will never exceed the maximum temperature limit.
