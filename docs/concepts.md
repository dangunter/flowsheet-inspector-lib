# Concepts

## Main components

Below are the main components of 

Flowsheet: IDAES/PrOMMiS/WaterTAP/etc. model, based on Pyomo, that represents the equations of a chemical engineering process as a set of equations that can be optimized with a solver.

Solver: Optimization algorithm that runs on a constructed flowsheet and attempts to find values of input variables that come closest to maximizing (or minimizing) certain output variables. The most common solver used is IPOPT (Interior Point Optimizer).

Structured Flowsheet: A Python module that uses the IDAES Python platform to create a flowsheet, and then *wraps* the major *steps* in this flowsheet, for which a standard list is recommended. This allows the flowsheet to operate in a more standard way and be more easily controlled by other Python modules.

Flowsheet Inspector: Two components, a front-end VSCode extension and back-end Python library, that work together to provide an interface inside the VSCode IDE for integrated execution and inspection of structured flowsheets.

AI Skill: Roughly standardized format for providing instructions, reference materials, and executable scripts to an AI agent that are specific to one specialized area of knowledge. A set of AI skills are being developed in parallel with the Flowsheet Inspector, which can be used in the IDE to provide a high-level interface to creating, modifying, and debugging flowsheets.