.. raw:: latex

    \clearpage
  	\pagenumbering{roman}


| February 2020


#############################
EPANET 2.2 Users Manual
#############################


| Water System Division
| National Risk Management Research Laboratory


| NATIONAL RISK MANAGEMENT RESEARCH LABORATORY
| OFFICE OF RESEARCH AND DEVELOPMENT
| U.S. ENVIRONMENTAL PROTECTION AGENCY CINCINNATI, OH 45268



**DISCLAIMER**

This User Manual is an updated version of the EPANET 2 User Manual
(EPA/600/R-00/057) written by Lewis Rossman in 2000.  The EPANET 2 software
was developed by the U.S. Environmental Protection Agency (EPA).
Version 2.2 includes contributions from EPA and from other individuals outside
the United States Government. No warranty expressed or implied is made regarding
the functionality of the software, nor shall the act of release or distribution
constitute any such warranty. The software is released on condition that neither
the EPA nor the U.S. Government shall be held liable for any damages resulting
from its authorized or unauthorized use. The EPA has relinquished control of
the information and no longer has responsibility to protect the integrity,
confidentiality or availability of the information.  Any reference to specific
commercial products, processes, or services by service mark, trademark,
manufacturer, or otherwise, does not constitute or imply their endorsement,
recommendation or favoring by the EPA. The EPA seal and logo shall not be
used in any manner to imply endorsement of any commercial product or activity
by the EPA or the United States Government.


-----------------------


**About This Manual**

:ref:`Chapter 1 <introduction>` of this manual describes what EPANET is and its
capabilities.

:ref:`Chapter 2 <quickstart>` describes how to install EPANET and offers
up a quick tutorial on its use. Readers unfamiliar with the basics of
modeling distribution systems might wish to review :ref:`Chapter 3 <network_model>`
first before working through the tutorial.

:ref:`Chapter 3 <network_model>` provides background material on how EPANET
models a water distribution system. It discusses the behavior of the physical
components that comprise a distribution system as well as how
additional modeling information, such as time variations and
operational control, are handled. It also provides an overview of how
the numerical simulation of system hydraulics and water quality
performance is carried out.

:ref:`Chapter 4 <workspace>` shows how the EPANET workspace is organized. It
describes the functions of the various menu options and toolbar buttons, and
how the three main windows – the Network Map, the Browser, and the
Property Editor—are used.

:ref:`Chapter 5 <projects>` discusses the project files that store all of the
information contained in an EPANET model of a distribution system. It
shows how to create, open, and save these files as well as how to set
default project options. It also discusses how to register
calibration data that are used to compare simulation results against
actual measurements.

:ref:`Chapter 6 <objects>` describes how one goes about building a network
model of a distribution system with EPANET. It shows how to create the various
physical objects (pipes, pumps, valves, junctions, tanks, etc.) that
make up a system, how to edit the properties of these objects, and
how to describe the way that system demands and operation change over
time.

:ref:`Chapter 7 <map>` explains how to use the network map that provides a
graphical view of the system being modeled. It shows how to view
different design and computed parameters in color-coded fashion on
the map, how to re-scale, zoom, and pan the map, how to locate
objects on the map, and what options are available to customize the
appearance of the map.

:ref:`Chapter 8 <analyzing_network>` shows how to run a hydraulic/water quality
analysis of a network model. It describes the various options that control how
the analysis is made and offers some troubleshooting tips to use when
examining simulation results.

:ref:`Chapter 9 <viewing_results>` discusses the various ways in which the
results of an analysis can be viewed. These include different views of the
network map, various kinds of graphs and tables, and several different types
of special reports.

:ref:`Chapter 10 <printing_copying>` explains how to print and copy the views
discussed in :ref:`Chapter 9 <viewing_results>`.

:ref:`Chapter 11 <importing_exporting>` describes how EPANET can import and
export project scenarios. A scenario is a subset of the data that characterizes
the current conditions under which a pipe network is being analyzed
(e.g., consumer demands, operating rules, water quality reaction
coefficients, etc.). It also discusses how to save a project’s entire
database to a readable text file and how to export the network map to
a variety of formats.

:ref:`Chapter 12 <questions>` answers questions about how EPANET can be used
to model special kinds of situations, such as modeling pneumatic tanks,
finding the maximum flow available at a specific pressure, and
modeling the growth of disinfection by-products.

:ref:`Chapter 13 <analysis_algorithms>` provides details of the procedures and
formulas used by EPANET in its hydraulic and water quality analysis algorithms.


The manual also contains several appendixes.

| :ref:`Appendix A <units>` provides a table of units of expression for all
  design and computed parameters.
| :ref:`Appendix B <error_messages>` is a list of error message codes and their
  meanings that the program can generate.
| :ref:`Appendix C <command_line>` describes how EPANET can be run
  from a command line prompt within a DOS window, and discusses the
  format of the files that are used with this mode of operation.
