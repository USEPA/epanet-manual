.. raw:: latex

    \clearpage
  	\pagenumbering{arabic}
    \setcounter{page}{1}


.. _introduction:

Introduction
============


What is EPANET
~~~~~~~~~~~~~~

   EPANET is a computer program that performs extended period simulation
   of hydraulic and water quality behavior within pressurized pipe
   networks. A network consists of pipes, nodes (pipe junctions), pumps,
   valves and storage tanks or reservoirs. EPANET tracks the flow of
   water in each pipe, the pressure at each node, the height of water in
   each tank, and the concentration of a chemical species throughout the
   network during a simulation period comprised of multiple time steps.
   In addition to chemical species, water age and source tracing can
   also be simulated.

   EPANET is designed to be a research tool for improving our
   understanding of the movement and fate of drinking water constituents
   within distribution systems. It can be used for many different kinds
   of applications in distribution systems analysis. Sampling program
   design, hydraulic model calibration, chlorine residual analysis, and
   consumer exposure assessment are some examples. EPANET can help
   assess alternative management strategies for improving water quality
   throughout a system. These can include:

    -  altering source utilization within multiple source systems,

    -  altering pumping and tank filling/emptying schedules,

    -  use of satellite treatment, such as re-chlorination at storage tanks,

    -  targeted pipe cleaning and replacement.

..

   Running under Windows, EPANET provides an integrated environment for
   editing network input data, running hydraulic and water quality
   simulations, and viewing the results in a variety of formats. These
   include color-coded network maps, data tables, time series graphs,
   and contour plots.

Hydraulic Modeling Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Full-featured and accurate hydraulic modeling is a prerequisite for
   doing effective water quality modeling. EPANET contains a
   state-of-the-art hydraulic analysis engine that includes the
   following capabilities:

    - places no limit on the size of the network that can be analyzed

    - computes friction headloss using the Hazen-Williams, Darcy-Weisbach,
      or Chezy-Manning formulas

    - includes minor head losses for bends, fittings, etc.

    - models constant or variable speed pumps

    - computes pumping energy and cost

    - models various types of valves including shutoff, check, pressure
      regulating, and flow control valves

    - allows storage tanks to have any shape (i.e., diameter can vary with
      height)

    - considers multiple demand categories at nodes, each with its own
      pattern of time variation

    - models pressure-dependent flow issuing from emitters (sprinkler
      heads)

    - models pressure dependent demand at nodes

    - can base system operation on both simple tank level or timer controls
      and on complex rule-based controls.

Water Quality Modeling Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   In addition to hydraulic modeling, EPANET provides the following
   water quality modeling capabilities:

    - models the movement of a non-reactive tracer material through the
      network over time

    - models the movement and fate of a reactive material as it grows
      (e.g., a disinfection by-product) or decays (e.g., chlorine residual)
      with time

    - models the age of water throughout a network

    - tracks the percent of flow from a given node reaching all other nodes
      over time

    - models reactions both in the bulk flow and at the pipe wall

    - uses n-th order kinetics to model reactions in the bulk flow

    - uses zero or first order kinetics to model reactions at the pipe wall

    - accounts for mass transfer limitations when modeling pipe wall
      reactions

    - allows growth or decay reactions to proceed up to a limiting
      concentration

    - employs global reaction rate coefficients that can be modified on a
      pipe-by-pipe basis

    - allows wall reaction rate coefficients to be correlated to pipe
      roughness

    - allows for time-varying concentration or mass inputs at any location
      in the network

    - models storage tanks as being either complete mix, plug flow, or
      two-compartment reactors.

..

   By employing these features, EPANET can study such water quality
   phenomena as:

    -  blending water from different sources

    -  age of water throughout a system

    -  loss of chlorine residuals

    -  growth of disinfection by-products

    -  tracking contaminant propagation events.

Steps in Using EPANET
~~~~~~~~~~~~~~~~~~~~~

   One typically carries out the following steps when using EPANET to
   model a water distribution system:

    1. Draw a network representation of your distribution system (see
       Section 6.1) or import a basic description of the network placed in a
       text file (see Section 11.4).

    2. Edit the properties of the objects that make up the system (see
       Section 6.4)

    3. Describe how the system is operated (see Section 6.5)

    4. Select a set of analysis options (see Section 8.1)

    5. Run a hydraulic/water quality analysis (see Section 8.2)

    6. View the results of the analysis (see Chapter 9).
