.. EPANET documentation master file, created by
   sphinx-quickstart on Thu Sep 13 09:02:19 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to EPANET's documentation!
==================================

This on-line manual is based on the **EPANET 2 USERS MANUAL** 
by Lewis A. Rossman. 
The original report number is EPA/600/R-00/057 (September 2000). 

| NATIONAL RISK MANAGEMENT RESEARCH LABORATORY
| OFFICE OF RESEARCH AND DEVELOPMENT
| U.S. ENVIRONMENTAL PROTECTION AGENCY CINCINNATI, OH 45268

::
  
  DISCLAIMER

  The information in this document has been funded wholly or in part by
  the U.S. Environmental Protection Agency (EPA). It has been subjected
  to the Agency's peer and administrative review, and has been approved
  for publication as an EPA document. Mention of trade names or
  commercial products does not constitute endorsement or recommendation
  for use.

  Although a reasonable effort has been made to assure that the results
  obtained are correct, the computer programs described in this manual
  are experimental. Therefore the author and the U.S. Environmental
  Protection Agency are not responsible and assume no liability
  whatsoever for any results or any use made of the results obtained
  from these programs, nor for any damages or litigation that result
  from the use of these programs for any purpose.

-------------

.. toctree::
   :maxdepth: 1
   :caption: Table of Contents
   
   0_about_manual
   1_introduction
   2_quickstart
   3_network_model
   4_EPANET_workspace
   5_projects
   6_objects
   7_map
   8_analyzing_network
   9_viewing_results
   10_printing_copying
   11_importing_exporting
   12_questions
   A_units
   B_error_messages
   C_command_line_EPANET
   D_analysis_algorithms
   E_references
   F_en2_section_keywords
   


**Chapter 2** of this manual describes how to install EPANET and offers
up a quick tutorial on its use. Readers unfamiliar with the basics of
modeling distribution systems might wish to review Chapter 3 first
before working through the tutorial.

**Chapter 3** provides background material on how EPANET models a water
distribution system. It discusses the behavior of the physical
components that comprise a distribution system as well as how
additional modeling information, such as time variations and
operational control, are handled. It also provides an overview of how
the numerical simulation of system hydraulics and water quality
performance is carried out.

**Chapter 4** shows how the EPANET workspace is organized. It describes
the functions of the various menu options and toolbar buttons, and
how the three main windows – the Network Map, the Browser, and the
Property Editor—are used.

**Chapter 5** discusses the project files that store all of the
information contained in an EPANET model of a distribution system. It
shows how to create, open, and save these files as well as how to set
default project options. It also discusses how to register
calibration data that are used to compare simulation results against
actual measurements.

**Chapter 6** describes how one goes about building a network model of a
distribution system with EPANET. It shows how to create the various
physical objects (pipes, pumps, valves, junctions, tanks, etc.) that
make up a system, how to edit the properties of these objects, and
how to describe the way that system demands and operation change over
time.

**Chapter 7** explains how to use the network map that provides a
graphical view of the system being modeled. It shows how to view
different design and computed parameters in color-coded fashion on
the map, how to re-scale, zoom, and pan the map, how to locate
objects on the map, and what options are available to customize the
appearance of the map.

**Chapter 8** shows how to run a hydraulic/water quality analysis of a
network model. It describes the various options that control how the
analysis is made and offers some troubleshooting tips to use when
examining simulation results.

**Chapter 9** discusses the various ways in which the results of an
analysis can be viewed. These include different views of the network
map, various kinds of graphs and tables, and several different types
of special reports.

**Chapter 10** explains how to print and copy the views discussed in
Chapter 9.

**Chapter 11** describes how EPANET can import and export project
scenarios. A scenario is a subset of the data that characterizes the
current conditions under which a pipe network is being analyzed
(e.g., consumer demands, operating rules, water quality reaction
coefficients, etc.). It also discusses how to save a project’s entire
database to a readable text file and how to export the network map to
a variety of formats.

**Chapter 12** answers questions about how EPANET can be used to model
special kinds of situations, such as modeling pneumatic tanks,
finding the maximum flow available at a specific pressure, and
modeling the growth of disinfection by-products.

The manual also contains several appendixes. 

| **Appendix A** provides a table of units of expression for all design 
  and computed parameters.
| **Appendix B** is a list of error message codes and their meanings that
  the program can generate. 
| **Appendix C** describes how EPANET can be run
  from a command line prompt within a DOS window, and discusses the
  format of the files that are used with this mode of operation.
| **Appendix D** provides details of the procedures and formulas used by
  EPANET in its hydraulic and water quality analysis algorithms.

  
Contents
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
