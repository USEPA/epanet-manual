.. raw:: latex

    \clearpage


.. _command_line:

C. Command Line EPANET
======================


General Instructions
~~~~~~~~~~~~~~~~~~~~

  EPANET can also be run as a console application from the command line
  within a DOS window. In this case network input data are placed into
  a text file and results are written to a text file. The command line
  for running EPANET in this fashion is:

    ::

      epanet2d  inpfile  rptfile  outfile


  Here **inpfile** is the name of the input file, **rptfile** is the
  name of the output report file, and **outfile** is the name of an
  optional binary output file that stores results in a special binary
  format. If the latter file is not needed then just the input and
  report file names should be supplied. As written, the above command
  assumes that you are working in the directory in which EPANET was
  installed or that this directory has been added to the PATH statement
  in your AUTOEXEC.BAT file. Otherwise full pathnames for the
  executable **epanet2d.exe** and the files on the command line must be
  used. The error messages for command line EPANET are the same as
  those for Windows EPANET and are listed in Appendix B.

Input File Format
~~~~~~~~~~~~~~~~~

  The input file for command line EPANET has the same format as the
  text file that Windows EPANET generates from its **File >> Export >>
  Network** command. It is organized in sections, where each section
  begins with a keyword enclosed in brackets. The various keywords are
  listed below.

  +-------------+-------------+-------------+-------------+-------------+
  | *Network    | *System     | *Water      | *Options*   | *Network    |
  | Components* | Operation*  | Quality*    |             | Map/Tags*   |
  +=============+=============+=============+=============+=============+
  | [TITLE]     | [CURVES]    | [QUALITY]   | [OPTIONS]   |[COORDINATES]|
  +-------------+-------------+-------------+-------------+-------------+
  | [JUNCTIONS] | [PATTERNS]  | [REACTIONS] | [TIMES]     | [VERTICES]  |
  +-------------+-------------+-------------+-------------+-------------+
  | [RESERVOIRS]| [ENERGY]    | [SOURCES]   | [REPORT]    | [LABELS]    |
  +-------------+-------------+-------------+-------------+-------------+
  | [TANKS]     | [STATUS]    | [MIXING]    |             | [BACKDROP]  |
  +-------------+-------------+-------------+-------------+-------------+
  | [PIPES]     | [CONTROLS]  |             |             | [TAGS]      |
  +-------------+-------------+-------------+-------------+-------------+
  | [PUMPS]     | [RULES]     |             |             |             |
  +-------------+-------------+-------------+-------------+-------------+
  | [VALVES]    | [DEMANDS]   |             |             |             |
  +-------------+-------------+-------------+-------------+-------------+
  | [EMITTERS]  |             |             |             |             |
  +-------------+-------------+-------------+-------------+-------------+


  The order of sections is not important. However, whenever a node or
  link is referred to in a section it must have already been defined in
  the [JUNCTIONS], [RESERVOIRS], [TANKS], [PIPES], [PUMPS], or [VALVES]
  sections. Thus it is
  recommended that these sections be placed first, right after the
  [TITLE] section. The network map and tags sections are not used by
  command line EPANET and can be eliminated from the file.

  Each section can contain one or more lines of data. Blank lines can
  appear anywhere in the file and the semicolon (;) can be used to
  indicate that what follows on the line is a comment, not data. A
  maximum of 255 characters can appear on a line. The ID labels used to
  identify nodes, links, curves and patterns can be any combination of
  up to 15 characters and numbers.

  Figure C.1 displays the input file that represents the tutorial
  network discussed in Chapter 2.

    ::

      [TITLE]
      EPANET TUTORIAL

      [JUNCTIONS]
      ;ID Elev Demand
      ;------------------
      2 0 0
      3 710 650
      4 700 150
      5 695 200
      6 700 150

      [RESERVOIRS]
      ;ID Head
      ;---------
      1 700

      [TANKS]
      ;ID Elev InitLvl MinLvl MaxLvl Diam Volume
      ;-----------------------------------------------
      7 850 5 0 15 70 0

      [PIPES]
      ;ID Node1 Node2 Length Diam Roughness
      ;-----------------------------------------
      1 2 3 3000 12 100
      2 3 6 5000 12 100
      3 3 4 5000 8 100
      4 4 5 5000 8 100
      5 5 6 5000 8 100
      6 6 7 7000 10 100

      [PUMPS]
      ;ID Node1 Node2 Parameters
      ;---------------------------------
      7 1 2 HEAD 1

      [PATTERNS]
      ;ID Multipliers
      ;-----------------------
      1 0.5 1.3 1 1.2

      [CURVES]
      ;ID X-Value Y-Value
      ;--------------------
      1 1000 200

      [QUALITY]
      ;Node InitQual
      ;-------------
      1 1

      [REACTIONS]
      Global Bulk -1
      Global Wall 0

      [TIMES]
      Duration 24:00
      Hydraulic Timestep 1:00
      Quality Timestep 0:05
      Pattern Timestep 6:00

      [REPORT]
      Page 55
      Energy Yes
      Nodes All
      Links All

      [OPTIONS]
      Units GPM
      Headloss H-W
      Pattern 1
      Quality Chlorine mg/L
      Tolerance 0.01

      [END]

    **Figure C.1** Example EPANET Input File

  On the pages that follow the contents and formats of each keyword
  section are described in alphabetical order.


.. include:: input_keywords.rst


---------------------


Report File Format
~~~~~~~~~~~~~~~~~~

   Statements supplied to the [REPORT] section of the input file control
   the contents of the report file generated from a command-line run of
   EPANET. A portion of the report generated from the input file of
   Figure C.1 is shown in Figure C.2. In general a report can contain
   the following sections:

    -  Status Section

    -  Energy Section

    -  Nodes Section

    -  Links Section



Status Section
--------------

   The Status Section of the output report lists the initial status of
   all reservoirs, tanks, pumps, valves, and closed pipes as well as any
   changes in the status of these components as they occur over time in
   an extended period simulation. The status of reservoirs and tanks
   indicates whether they are filling or emptying. The status of links
   indicates whether they are open or closed and includes the relative
   speed setting for pumps and the pressure/flow setting for control
   valves. To include a Status Section in the report use the command
   **STATUS YES** in the [REPORT] section of the input file.

   Using **STATUS FULL** will also produce a full listing of the
   convergence results for all iterations of each hydraulic analysis
   made during a simulation. This listing will also show which
   components are changing status during the iterations. This level of
   detail is only useful when one is trying to debug a run that fails to
   converge because a component’s status is cycling.

Energy Section
---------------

   The Energy Section of the output report lists overall energy
   consumption and cost for each pump in the network. The items listed
   for each pump include:

    -  Percent Utilization (percent of the time that the pump is on-line)

    -  Average Efficiency

    -  Kilowatt-hours consumed per million gallons (or cubic meters) pumped

    -  Average Kilowatts consumed

    -  Peak Kilowatts used

    -  Average cost per day



   Also listed is the total cost per day for pumping and the total
   demand charge (cost based on the peak energy usage) incurred. To
   include an Energy Section in the report the command **ENERGY YES**
   must appear in the [REPORT] section of the input file.

    ::

      ******************************************************************
      * E P A N E T *
      * Hydraulic and Water Quality *
      * Analysis for Pipe Networks *
      * Version 2.0 *
      ******************************************************************
      EPANET TUTORIAL
      Input Data File ................... tutorial.inp
      Number of Junctions................ 5
      Number of Reservoirs............... 1
      Number of Tanks ................... 1
      Number of Pipes ................... 6
      Number of Pumps ................... 1
      Number of Valves .................. 0
      Headloss Formula .................. Hazen-Williams
      Hydraulic Timestep ................ 1.00 hrs
      Hydraulic Accuracy ................ 0.001000
      Maximum Trials .................... 40
      Quality Analysis .................. Chlorine
      Water Quality Time Step ........... 5.00 min
      Water Quality Tolerance ........... 0.01 mg/L
      Specific Gravity .................. 1.00
      Relative Kinematic Viscosity ...... 1.00
      Relative Chemical Diffusivity ..... 1.00
      Demand Multiplier ................. 1.00
      Total Duration .................... 24.00 hrs
      Reporting Criteria:
      All Nodes
      All Links
      Energy Usage:
      ----------------------------------------------------------------
      Usage Avg. Kw-hr Avg. Peak Cost
      Pump Factor Effic. /Mgal Kw Kw /day
      ----------------------------------------------------------------
      7 100.00 75.00 746.34 51.34 51.59 0.00
      ----------------------------------------------------------------
                         Demand Charge: 0.00
                            Total Cost: 0.00

      Node Results at 0:00 hrs:
      --------------------------------------------------------
      Demand Head Pressure Chlorine
      Node gpm ft psi mg/L
      --------------------------------------------------------
      2 0.00 893.37 387.10 0.00
      3 325.00 879.78 73.56 0.00
      4 75.00 874.43 75.58 0.00
      5 100.00 872.69 76.99 0.00
      6 75.00 872.71 74.84 0.00
      1 -1048.52 700.00 0.00 1.00 Reservoir
      7 473.52 855.00 2.17 0.00 Tank
      Link Results at 0:00 hrs:
      ----------------------------------------------
      Flow Velocity Headloss
      Link gpm fps /1000ft
      ----------------------------------------------
      1 1048.52 2.97 4.53
      2 558.33 1.58 1.41
      3 165.19 1.05 1.07
      4 90.19 0.58 0.35
      5 -9.81 0.06 0.01
      6 473.52 1.93 2.53
      7 1048.52 0.00 -193.37 Pump
      Node Results at 1:00 hrs:
      --------------------------------------------------------
      Demand Head Pressure Chlorine
      Node gpm ft psi mg/L
      --------------------------------------------------------
      2 0.00 893.92 387.34 1.00
      3 325.00 880.42 73.84 0.99
      4 75.00 875.12 75.88 0.00
      5 100.00 873.40 77.30 0.00
      6 75.00 873.43 75.15 0.00
      1 -1044.60 700.00 0.00 1.00 Reservoir
      7 469.60 855.99 2.59 0.00 Tank
      Link Results at 1:00 hrs:
      ----------------------------------------------
      Flow Velocity Headloss
      Link gpm fps /1000ft
      ----------------------------------------------
      1 1044.60 2.96 4.50
      2 555.14 1.57 1.40
      3 164.45 1.05 1.06
      4 89.45 0.57 0.34
      5 -10.55 0.07 0.01
      6 469.60 1.92 2.49
      7 1044.60 0.00 -193.92 Pump

    **Figure C.2** Excerpt from a Report File

Nodes Section
--------------

   The Nodes Section of the output report lists simulation results for
   those nodes and parameters identified in the [REPORT] section of the
   input file. Results are listed for each reporting time step of an
   extended period simulation. The reporting time step is specified in
   the [TIMES] section of the input file. Results at intermediate times
   when certain hydraulic events occur, such as pumps turning on or off
   or tanks closing because they become empty or full, are not reported.

   To have nodal results reported the [REPORT] section of the input file
   must contain the keyword **NODES** followed by a listing of the ID
   labels of the nodes to be included in the report. There can be
   several such **NODES** lines in the file. To report results for all
   nodes use the command **NODES ALL**.

   The default set of reported quantities for nodes includes Demand,
   Head, Pressure, and Water Quality. You can specify how many decimal
   places to use when listing results for a parameter by using commands
   such as **PRESSURE PRECISION 3** in the input file (i.e., use 3
   decimal places when reporting results for pressure). The default
   precision is 2 decimal places for all quantities. You can filter the
   report to list only the occurrences of values below or above a
   certain value by adding statements of the form **PRESSURE BELOW 20**
   to the input file.

Links Section
-------------

   The Links Section of the output report lists simulation results for
   those links and parameters identified in the [REPORT] section of the
   input file. The reporting times follow the same convention as was
   described for nodes in the previous section.

   As with nodes, to have any results for links reported you must
   include the keyword **LINKS** followed by a list of link ID labels in
   the [REPORT] section of the input file. Use the command **LINKS ALL**
   to report results for all links.

   The default parameters reported on for links includes Flow, Velocity,
   and Headloss. Diameter, Length, Water Quality, Status, Setting,
   Reaction Rate, and Friction Factor can be added to these by using
   commands such as **DIAMETER YES** or **DIAMETER PRECISION 0**. The
   same conventions used with node parameters for specifying reporting
   precision and filters also applies to links.

Binary Output File Format
~~~~~~~~~~~~~~~~~~~~~~~~~

  If a third file name is supplied to the command line that runs EPANET
  then the results for all parameters for all nodes and links for all
  reporting time periods will be saved to this file in a special binary
  format. This file can be used for special post- processing purposes.
  Data written to the file are 4-byte integers, 4-byte floats, or
  fixed-size strings whose size is a multiple of 4 bytes. This allows
  the file to be divided conveniently into 4-byte records. The file
  consists of four sections of the following sizes in bytes:


  +-----------------+----------------------------------------+
  | *Section*       | *Size in bytes*                        |
  +=================+========================================+
  | Prolog          | 852 + 20*Nnodes + 36*Nlinks + 8*Ntanks |
  +-----------------+----------------------------------------+
  | Energy Use      | 28*Npumps + 4                          |
  +-----------------+----------------------------------------+
  | Extended Period | (16*Nnodes + 32*Nlinks)*Nperiods       |
  +-----------------+----------------------------------------+
  | Epilog          | 28                                     |
  +-----------------+----------------------------------------+

  where

    Nnodes = number of nodes (junctions + reservoirs + tanks) Nlinks =
    number of links (pipes + pumps + valves) Ntanks = number of tanks and
    reservoirs

    Npumps = number of pumps

    Nperiods = number of reporting periods

    and all of these counts are themselves written to the file's Prolog
    or Epilog sections.


Prolog Section
---------------

  The prolog section of the binary Output File contains the following
  data:

  +-----------------------+-----------------------+-----------------------+
  | **Item**              |    **Type**           |    **Number of        |
  |                       |                       |    Bytes**            |
  +=======================+=======================+=======================+
  | Magic Number ( =      |    Integer            |    4                  |
  | 516114521)            |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Version (= 200)       |    Integer            |    4                  |
  +-----------------------+-----------------------+-----------------------+
  | Number of Nodes       |    Integer            |    4                  |
  |                       |                       |                       |
  | (Junctions +          |                       |                       |
  | Reservoirs + Tanks)   |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Number of Reservoirs  |    Integer            |    4                  |
  | & Tanks               |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Number of Links       |    Integer            |    4                  |
  |                       |                       |                       |
  | (Pipes + Pumps +      |                       |                       |
  | Valves)               |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Number of Pumps       |    Integer            |    4                  |
  +-----------------------+-----------------------+-----------------------+
  | Number of Valves      |    Integer            |    4                  |
  +-----------------------+-----------------------+-----------------------+
  |    Water Quality      |    Integer            |    4                  |
  |    Option 0 = none    |                       |                       |
  |                       |                       |                       |
  |    1 = chemical       |                       |                       |
  |                       |                       |                       |
  |    2 = age            |                       |                       |
  |                       |                       |                       |
  |    3 = source trace   |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Index of Node for     |    Integer            |    4                  |
  | Source Tracing        |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  |    Flow Units Option  |    Integer            |    4                  |
  |    0 = cfs            |                       |                       |
  |                       |                       |                       |
  |    1 = gpm            |                       |                       |
  |                       |                       |                       |
  |    2 = mgd            |                       |                       |
  |                       |                       |                       |
  |    3 = Imperial mgd 4 |                       |                       |
  |    = acre-ft/day      |                       |                       |
  |                       |                       |                       |
  |    5 = liters/second  |                       |                       |
  |                       |                       |                       |
  |    6 = liters/minute  |                       |                       |
  |                       |                       |                       |
  |    7 = megaliters/day |                       |                       |
  |                       |                       |                       |
  |    8 = cubic          |                       |                       |
  |    meters/hour 9 =    |                       |                       |
  |    cubic meters/day   |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  |    Pressure Units     |    Integer            |    4                  |
  |    Option 0 = psi     |                       |                       |
  |                       |                       |                       |
  |    1 = meters         |                       |                       |
  |                       |                       |                       |
  |    2 = kPa            |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Statistics Flag       |    Integer            |    4                  |
  |                       |                       |                       |
  |    0 = no statistical |                       |                       |
  |    processing 1 =     |                       |                       |
  |    results are        |                       |                       |
  |    time-averaged      |                       |                       |
  |                       |                       |                       |
  |    2 = only minimum   |                       |                       |
  |    values reported    |                       |                       |
  |                       |                       |                       |
  |    3 = only maximum   |                       |                       |
  |    values reported 4  |                       |                       |
  |    = only ranges      |                       |                       |
  |    reported           |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Reporting Start Time  |    Integer            |    4                  |
  | (seconds)             |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Reporting Time Step   |    Integer            |    4                  |
  | (seconds)             |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Simulation Duration   |    Integer            |    4                  |
  | (seconds)             |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Problem Title (1st    |    Char               |    80                 |
  | line)                 |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Problem Title (2nd    |    Char               |    80                 |
  | line)                 |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Problem Title (3rd    |    Char               |    80                 |
  | line)                 |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Name of Input File    |    Char               |    260                |
  +-----------------------+-----------------------+-----------------------+
  | Name of Report File   |    Char               |    260                |
  +-----------------------+-----------------------+-----------------------+
  | Name of Chemical      |    Char               |    16                 |
  +-----------------------+-----------------------+-----------------------+
  | Chemical              |    Char               |    16                 |
  | Concentration Units   |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | ID Label of Each Node |    Char               |    16                 |
  +-----------------------+-----------------------+-----------------------+
  | ID Label of Each Link |    Char               |    16                 |
  +-----------------------+-----------------------+-----------------------+
  | Index of Start Node   |    Integer            |    4*Nlinks           |
  | of Each Link          |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Index of End Node of  |    Integer            |    4*Nlinks           |
  | Each Link             |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  |    Type Code of Each  |    Integer            |    4*Nlinks           |
  |    Link 0 = Pipe with |                       |                       |
  |    CV                 |                       |                       |
  |                       |                       |                       |
  |    1 = Pipe           |                       |                       |
  |                       |                       |                       |
  |    2 = Pump           |                       |                       |
  |                       |                       |                       |
  |    3 = PRV            |                       |                       |
  |                       |                       |                       |
  |    4 = PSV            |                       |                       |
  |                       |                       |                       |
  |    5 = PBV            |                       |                       |
  |                       |                       |                       |
  |    6 = FCV            |                       |                       |
  |                       |                       |                       |
  |    7 = TCV            |                       |                       |
  |                       |                       |                       |
  |    8 = GPV            |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Node Index of Each    |    Integer            |    4*Ntanks           |
  | Tank                  |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Cross-Sectional Area  |    Float              |    4*Ntanks           |
  | of Each Tank          |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Elevation of Each     |    Float              |    4*Nnodes           |
  | Node                  |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Length of Each Link   |    Float              |    4*Nlinks           |
  +-----------------------+-----------------------+-----------------------+
  | Diameter of Each Link |    Float              |    4*Nlinks           |
  +-----------------------+-----------------------+-----------------------+



  There is a one-to-one correspondence between the order in which the
  ID labels for nodes and links are written to the file and the index
  numbers of these components. Also, reservoirs are distinguished from
  tanks by having their cross-sectional area set to zero.

Energy Use Section
----------------------

  The Energy Use section of the binary output file immediately follows
  the Prolog section. It contains the following data:

  +-----------------------+-----------------------+-----------------------+
  | **Item**              |    **Type**           |    **Number of        |
  |                       |                       |    Bytes**            |
  +=======================+=======================+=======================+
  | Repeated for each     |                       |                       |
  | pump:                 |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | -  Pump Index in List |    Float              |    4                  |
  |    of Links           |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | -  Pump Utilization   |    Float              |    4                  |
  |    (%)                |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | -  Average Efficiency |    Float Float        |    4                  |
  |    (%)                |                       |                       |
  |                       |                       |    4                  |
  | -  Average            |                       |                       |
  |    Kwatts/Million     |                       |                       |
  |    Gallons            |                       |                       |
  |    (/Meter:sup:`3`)   |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | -  Average Kwatts     |    Float              |    4                  |
  +-----------------------+-----------------------+-----------------------+
  | -  Peak Kwatts        |    Float              |    4                  |
  +-----------------------+-----------------------+-----------------------+
  | -  Average Cost Per   |    Float              |    4                  |
  |    Day                |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Overall Peak Energy   |    Float              |    4                  |
  | Usage                 |                       |                       |
  +-----------------------+-----------------------+-----------------------+


  The statistics reported in this section refer to the period of time
  between the start of the output reporting period and the end of the
  simulation.

Extended Period Section
-----------------------

  The Extended Period section of the binary Output File contains
  simulation results for each reporting period of an analysis (the
  reporting start time and time step are written to the Output File's
  Prolog section and the number of steps is written to the Epilog
  section). For each reporting period the following values are written
  to the file:

  +-----------------------+-----------------------+-----------------------+
  | **Item**              |    **Type**           |    **Size in Bytes**  |
  +=======================+=======================+=======================+
  | Demand at Each Node   |    Float              |    4*Nnodes           |
  +-----------------------+-----------------------+-----------------------+
  | Hydraulic Head at     |    Float              |    4*Nnodes           |
  | Each Node             |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Pressure at Each Node |    Float              |    4*Nnodes           |
  +-----------------------+-----------------------+-----------------------+
  | Water Quality at Each |    Float              |    4*Nnodes           |
  | Node                  |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Flow in Each Link     |    Float              |    4*Nlinks           |
  |                       |                       |                       |
  | (negative for reverse |                       |                       |
  | flow)                 |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Velocity in Each Link |    Float              |    4*Nlinks           |
  +-----------------------+-----------------------+-----------------------+
  | Headloss per 1000     |    Float              |    4*Nlinks           |
  | Units of Length for   |                       |                       |
  | Each Link (Negative   |                       |                       |
  | of head gain for      |                       |                       |
  | pumps and total head  |                       |                       |
  |                       |                       |                       |
  | loss for valves)      |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Average Water Quality |    Float              |    4*Nlinks           |
  | in Each Link          |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Status Code for Each  |    Float              |    4*Nlinks           |
  | Link                  |                       |                       |
  |                       |                       |                       |
  |    0 = closed (max.   |                       |                       |
  |    head exceeded) 1 = |                       |                       |
  |    temporarily closed |                       |                       |
  |                       |                       |                       |
  |    2 = closed         |                       |                       |
  |                       |                       |                       |
  |    3 = open           |                       |                       |
  |                       |                       |                       |
  |    4 = active         |                       |                       |
  |    (partially open)   |                       |                       |
  |                       |                       |                       |
  |    5 = open (max.     |                       |                       |
  |    flow exceeded) 6 = |                       |                       |
  |    open (flow setting |                       |                       |
  |    not met)           |                       |                       |
  |                       |                       |                       |
  |    7 = open (pressure |                       |                       |
  |    setting not met)   |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Setting for Each      |    Float              |    4*Nlinks           |
  | Link:                 |                       |                       |
  |                       |                       |                       |
  |    Roughness          |                       |                       |
  |    Coefficient for    |                       |                       |
  |    Pipes Speed for    |                       |                       |
  |    Pumps              |                       |                       |
  |                       |                       |                       |
  |    Setting for Valves |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Reaction Rate for     |    Float              |    4*Nlinks           |
  | Each Link             |                       |                       |
  | (mass/L/day)          |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | Friction Factor for   |    Float              |    4*Nlinks           |
  | Each Link             |                       |                       |
  +-----------------------+-----------------------+-----------------------+



Epilogue Section
-----------------

  The Epilogue section of the binary output file contains the following
  data:

  +--------------------------------------+-------------+------------------------+
  | **Item**                             |    **Type** |    **Number of Bytes** |
  +======================================+=============+========================+
  | Average bulk reaction rate (mass/hr) |    Float    |    4                   |
  +--------------------------------------+-------------+------------------------+
  | Average wall reaction rate (mass/hr) |    Float    |    4                   |
  +--------------------------------------+-------------+------------------------+
  | Average tank reaction rate (mass/hr) |    Float    |    4                   |
  +--------------------------------------+-------------+------------------------+
  | Average source inflow rate (mass/hr) |    Float    |    4                   |
  +--------------------------------------+-------------+------------------------+
  | Number of Reporting Periods          |    Integer  |    4                   |
  +--------------------------------------+-------------+------------------------+
  | Warning Flag:                        |    Integer  |    4                   |
  |                                      |             |                        |
  |    0 = no warnings                   |             |                        |
  |                                      |             |                        |
  |    1 = warnings were generated       |             |                        |
  +--------------------------------------+-------------+------------------------+
  | Magic Number ( = 516114521)          |    Integer  |    4                   |
  +--------------------------------------+-------------+------------------------+



  The mass units of the reaction rates both here and in the Extended
  Period output depend on the concentration units assigned to the
  chemical being modeled. The reaction rates listed in this section
  refer to the average of the rates seen in all pipes (or all tanks)
  over the entire reporting period of the simulation.
