# TDKernelDMVW

The algorithm implements the theoretical research of the following papers:

- S. Asadi and A. Lilienthal, "Approaches to time-dependent gas distribution modelling," 2015 European Conference on Mobile Robots (ECMR), Lincoln, 2015, pp. 1-6.
- Asadi, Sahar & Reggente, Matteo & Stachniss, Cyrill & Plagemann, Christian & Lilienthal, Achim. (2011). Statistical Gas Distribution Modelling Using Kernel Methods. Intelligent Systems for Machine Olfaction: Tools and Methodologies. 153-179.
- A. J. Lilienthal, M. Reggente, M. Trincavelli, J. L. Blanco and J. Gonzalez, "A statistical approach to gas distribution modelling with mobile robots - The Kernel DM+V algorithm," 2009 IEEE/RSJ International Conference on Intelligent Robots and Systems, St. Louis, MO, 2009, pp. 570-576.
- M. Reggente and A. J. Lilienthal, "Using local wind information for gas distribution mapping in outdoor environments with a mobile robot," 2009 IEEE Sensors, Christchurch, 2009, pp. 1715-1720.
- Neumann, Patrick. (2013). BAM-Dissertationsreihe. Bd. 109: Gas Source Localization and Gas Distribution Mapping with a Micro-Drone. Berlin : Bundesanstalt für
Materialforschung und -prüfung (BAM)

Besides the root algorithm (KernelDM), it contains the proposed extensions:
- time dependency (TD)
- variance (V)
- wind dependency (W)

Thanks to Achim Lilienthal, Patrick Neumann and Victor Hernandez for providing Matlab implementations for the extensions V and W.

## Run demo
Run the following code to generate the different maps. The mean map, variance map and confidence map are being plotted.

```bash
git clone https://github.com/smueller18/TDKernelDMVW.git
cd TDKernelDMVW/demo
python3 simple_example.py
```
