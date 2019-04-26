.. raw:: latex

    \clearpage


11. IMPORTING AND EXPORTING
===========================

*This chapter introduces the concept of Project Scenarios and
describes how EPANET can import and export these and other data, such
as the network map and the entire project database.*

-------



   

Project Scenarios
~~~~~~~~~~~~~~~~~

  A Project Scenario consists of a subset of the data that
  characterizes the current conditions under which a pipe network is
  being analyzed. A scenario can consist of one or more of the
  following data categories:

    -  Demands (baseline demand plus time patterns for all categories) at
       all nodes

    -  Initial water quality at all nodes

    -  Diameters for all pipes

    -  Roughness coefficients for all pipes

    -  Reaction coefficients (bulk and wall) for all pipes

    -  Simple and rule-based controls



  EPANET can compile a scenario based on some or all of the data
  categories listed above, save the scenario to file, and read the
  scenario back in at a later time.

  Scenarios can provide more efficient and systematic analysis of
  design and operating alternatives. They can be used to examine the
  impacts of different loading conditions, search for optimal parameter
  estimates, and evaluate changes in operating policies. The scenario
  files are saved as ASCII text and can be created or modified outside
  of EPANET using a text editor or spreadsheet program.

Exporting a Scenario
~~~~~~~~~~~~~~~~~~~~

   To export a project scenario to a text file:

    1. Select **File >> Export >> Scenario** from the main menu.

    2. In the Export Data dialog form that appears (see Figure 11.1) select
       the types of data that you wish to save.

    3. Enter an optional description of the scenario you are saving in the
       Notes memo field.

    4. Select the **OK** button to accept your choices.

    5. In the Save dialog box that next appears select a folder and name for
       the scenario file. Scenario files use the default extension .SCN.

    6. Click **OK** to complete the export.

  

      |image144|

      **Figure 11.1** Export Data Dialog

   The exported scenario can be imported back into the project at a
   later time as described in the next section.

Importing a Scenario
~~~~~~~~~~~~~~~~~~~~

   To import a project scenario from a file:

    1. Select **File >> Import >> Scenario** from the main menu.

    2. Use the Open File dialog box that appears to select a scenario file
       to import. The dialog's Contents panel will display the first several
       lines of files as they are selected, to help locate the desired file.

    3. Click the **OK** button to accept your selection.

   

   The data contained in the scenario file will replace any existing of
   the same kind in the current project.

Importing a Partial Network
~~~~~~~~~~~~~~~~~~~~~~~~~~~

   EPANET has the ability to import a geometric description of a pipe
   network in a simple text format. This description simply contains the
   ID labels and map coordinates of the nodes and the ID labels and end
   nodes of the links. This simplifies the process of using other
   programs, such as CAD and GIS packages, to digitize network geometric
   data and then transfer these data to EPANET.

   The format of a partial network text file looks as follows, where the
   text between brackets (< >) describes what type of information
   appears in that line of the file:

   ::
   
     [TITLE]

     <optional description of the file>

     [JUNCTIONS]

     <ID label of each junction>

     [PIPES]

     <ID label of each pipe followed by the ID labels of its end
     junctions>

     [COORDINATES]

     <Junction ID and its X and Y coordinates>

     [VERTICES]

     <Pipe ID and the X and Y coordinates of an intermediate vertex point>

   Note that only junctions and pipes are represented. Other network
   elements, such as reservoirs and pumps, can either be imported as
   junctions or pipes and converted later on or simply be added in later
   on. The user is responsible for transferring any data generated from
   a CAD or GIS package into a text file with the format shown above.

   In addition to this partial representation, a complete specification
   of the network can be placed in a file using the format described in
   Appendix C. This is the same format EPANET uses when a project is
   exported to a text file (see Section 11.7 below). In this case the
   file would also contain information on node and link properties, such
   as elevations, demands, diameters, roughness, etc.

Importing a Network Map
~~~~~~~~~~~~~~~~~~~~~~~

   To import the coordinates for a network map stored in a text file:

    1. Select **File >> Import >> Map** from the main menu.

    2. Select the file containing the map information from the Open File
       dialog that appears.

    3. Click **OK** to replace the current network map with the one
       described in the file.

Exporting the Network Map
~~~~~~~~~~~~~~~~~~~~~~~~~~

   The current view of the network map can be saved to file using either
   Autodesk's DXF (Drawing Exchange Format) format, the Windows enhanced
   metafile (EMF) format, or EPANET's own ASCII text (map) format. The
   DXF format is readable by many Computer Aided Design (CAD) programs.
   Metafiles can be inserted into word

   processing documents and loaded into drawing programs for re-scaling
   and editing. Both formats are vector-based and will not loose
   resolution when they are displayed at different scales.

   To export the network map at full extent to a DXF, metafile, or text
   file:

    1. Select **File >> Export >> Map** from the main menu.

    2. In the Map Export dialog form that appears (see Figure 11.2) select
       the format that you want the map saved in.

    3. If you select DXF format, you have a choice of how junctions will be
       represented in the DXF file. They can be drawn as open circles, as
       filled circles, or as filled squares. Not all DXF readers can
       recognize the commands used in the DXF file to draw a filled circle.

    4. After choosing a format, click OK and enter a name for the file in
       the Save As dialog form that appears.

      |image145|

      **Figure 11.2** Map Export Dialog

Exporting to a Text File
~~~~~~~~~~~~~~~~~~~~~~~~

   To export a project's data to a text file:

    1. Select **File >> Export >> Network** from the main menu.

    2. In the Save dialog form that appears enter a name for the file to
       save to (the default extension is .INP).

    3. Click **OK** to complete the export.



   The resulting file will be written in ASCII text format, with the
   various data categories and property labels clearly identified. It
   can be read back into EPANET

   for analysis at another time by using either the **File >> Open** or
   **File >> Import >> Network** commands. Complete network descriptions
   using this input format can also be created outside of EPANET using
   any text editor or spreadsheet program. A complete specification of
   the .INP file format is given in Appendix C.

   It is a good idea to save an archive version of your database in this
   format so you have access to a human readable version of your data.
   However, for day-to-day use of EPANET it is more efficient to save
   your data using EPANET's special project file format (that creates a
   .NET file) by using the **File >> Save** or **File >> Save As**
   commands. This format contains additional project information, such
   as the colors and ranges chosen for the map legends, the set of map
   display options in effect, the names of registered calibration data
   files, and any printing options that were selected.

   
..  |image0| image:: media/image1.jpeg
..  |image1| image:: media/image2.png
..  |image2| image:: media/image3.png
..  |image3| image:: media/image4.png
..  |image4| image:: media/image5.png
..  |image5| image:: media/image6.png
..  |image6| image:: media/image7.png
..  |image7| image:: media/image8.png
..  |image8| image:: media/image9.png
..  |image9| image:: media/image10.png
..  |image10| image:: media/image11.png
..  |image11| image:: media/image12.png
..  |image12| image:: media/image13.png
..  |image13| image:: media/image12.png
..  |image14| image:: media/image14.jpeg
..  |image15| image:: media/image15.png
..  |image16| image:: media/image16.jpeg
..  |image17| image:: media/image17.png
..  |image18| image:: media/image18.png
..  |image19| image:: media/image19.png
..  |image20| image:: media/image20.png
..  |image21| image:: media/image21.png
..  |image22| image:: media/image16.jpeg
..  |image23| image:: media/image22.png
..  |image24| image:: media/image18.png
..  |image25| image:: media/image23.png
..  |image26| image:: media/image24.png
..  |image27| image:: media/image25.png
..  |image28| image:: media/image26.png
..  |image29| image:: media/image27.png
..  |image30| image:: media/image28.png
..  |image31| image:: media/image29.png
    :width: 250pt
    :align: middle

..  |image31-2| image:: media/image29-2.png
    :width: 250pt
    :align: middle
    
..  |image32| image:: media/image30-2.png
    :width: 250pt
    :align: middle
    
..  |image32-2| image:: media/image30.png
    :width: 250pt
    :align: middle
    
..  |image33| image:: media/image31.png
..  |image34| image:: media/image32.png
..  |image35| image:: media/image33.png
..  |image36| image:: media/image34.png
..  |image36-2| image:: media/image36-2.png
..  |image37| image:: media/image35.png
..  |image38| image:: media/image36.png
..  |image39| image:: media/image37.png
..  |image40| image:: media/image38.png
..  |image41| image:: media/image39.png
..  |image42| image:: media/image40.png
..  |image43| image:: media/image41.png
..  |image44| image:: media/image42.png
..  |image45| image:: media/image43.png
..  |image46| image:: media/image44.png
..  |image47| image:: media/image45.png
..  |image48| image:: media/image18.png
..  |image49| image:: media/image25.png
..  |image50| image:: media/image19.png
..  |image51| image:: media/image46.png
..  |image52| image:: media/image12.png
..  |image53| image:: media/image13.png
..  |image54| image:: media/image47.png
..  |image55| image:: media/image48.png
..  |image56| image:: media/image49.png
..  |image57| image:: media/image50.png
..  |image58| image:: media/image51.png
..  |image59| image:: media/image6.png
..  |image60| image:: media/image5.png
..  |image61| image:: media/image7.png
..  |image62| image:: media/image9.png
..  |image63| image:: media/image10.png
..  |image64| image:: media/image52.png
..  |image65| image:: media/image11.png
..  |image66| image:: media/image53.jpeg
..  |image67| image:: media/image54.jpeg
..  |image68| image:: media/image55.png
..  |image69| image:: media/image57.png
..  |image70| image:: media/image58.png
..  |image71| image:: media/image59.png
..  |image72| image:: media/image38.png
..  |image73| image:: media/image39.png
..  |image74| image:: media/image40.png
..  |image75| image:: media/image2.png
..  |image76| image:: media/image60.png
..  |image77| image:: media/image61.png
..  |image78| image:: media/image6.png
..  |image79| image:: media/image5.png
..  |image80| image:: media/image7.png
..  |image81| image:: media/image16.jpeg
..  |image82| image:: media/image9.png
..  |image83| image:: media/image10.png
..  |image84| image:: media/image52.png
..  |image85| image:: media/image11.png
..  |image86| image:: media/image12.png
..  |image87| image:: media/image14.jpeg
..  |image88| image:: media/image14.jpeg
..  |image89| image:: media/image17.png
..  |image90| image:: media/image22.png
..  |image91| image:: media/image62.png
..  |image92| image:: media/image63.png
..  |image93| image:: media/image64.png
..  |image94| image:: media/image13.png
..  |image95| image:: media/image65.png
..  |image96| image:: media/image44.png
..  |image97| image:: media/image47.png
..  |image98| image:: media/image44.png
..  |image99| image:: media/image66.png
..  |image100| image:: media/image67.png
..  |image101| image:: media/image68.png
..  |image102| image:: media/image49.png
..  |image103| image:: media/image50.png
..  |image104| image:: media/image48.png
..  |image105| image:: media/image42.png
..  |image106| image:: media/image42.png
..  |image107| image:: media/image69.jpeg
..  |image108| image:: media/image70.png
..  |image109| image:: media/image71.png
..  |image110| image:: media/image46.png
..  |image111| image:: media/image72.png
..  |image112| image:: media/image14.jpeg
..  |image113| image:: media/image18.png
..  |image114| image:: media/image73.png
..  |image115| image:: media/image74.png
..  |image116| image:: media/image45.png
..  |image117| image:: media/image25.png
..  |image118| image:: media/image75.png
..  |image119| image:: media/image76.png
..  |image120| image:: media/image77.png
..  |image121| image:: media/image78.png
..  |image122| image:: media/image79.png
..  |image123| image:: media/image80.png
..  |image124| image:: media/image46.png
..  |image125| image:: media/image81.png
..  |image126| image:: media/image82.png
..  |image127| image:: media/image19.png
..  |image128| image:: media/image83.png
..  |image129| image:: media/image84.png
..  |image130| image:: media/image85.png
..  |image131| image:: media/image86.png
..  |image132| image:: media/image46.png
..  |image133| image:: media/image87.png
..  |image134| image:: media/image88.png
..  |image135| image:: media/image46.png
..  |image136| image:: media/image89.png
..  |image137| image:: media/image90.png
..  |image138| image:: media/image46.png
..  |image139| image:: media/image73.png
..  |image140| image:: media/image91.png
..  |image141| image:: media/image41.png
..  |image142| image:: media/image43.png
..  |image143| image:: media/image92.png
..  |image144| image:: media/image93.png
..  |image145| image:: media/image94.png
..  |image146| image:: media/image95.png
..  |image147| image:: media/image96.png
..  |image148| image:: media/image98.png

