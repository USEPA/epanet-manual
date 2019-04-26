.. raw:: latex

    \clearpage

    
5. WORKING WITH PROJECTS
========================

    
*This chapter discusses how EPANET uses project files to store a
piping network’s data. It explains how to set certain default options
for the project and how to register calibration data (observed
measurements) with the project to use for model evaluation.*

-------

  

Opening and Saving Project Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Project files contain all of the information used to model a network.
   They are usually named with a .NET extension.

   To create a new project:

      1. Select **File >> New** from the Menu Bar or click |image72| on the
         Standard Toolbar.

      2. You will be prompted to save the existing project (if changes were
         made to it) before the new project is created.

      3. A new, unnamed project is created with all options set to their
         default values.



   A new project is automatically created whenever EPANET first begins.
   To open an existing project stored on disk:

      1. Either select **File >> Open** from the Menu Bar or click |image73|
         on the Standard Toolbar.

      2. You will be prompted to save the current project (if changes were
         made to it).

      3. Select the file to open from the Open File dialog form that will
         appear. You can choose to open a file type saved previously as an
         EPANET project (typically with a .NET extension) or exported as a
         text file (typically with a .INP extension). EPANET recognizes file
         types by their content, not their names.

      4. Click **OK** to close the dialog and open the selected file.



   To save a project under its current name:

    -  Either select **File >> Save** from the Menu Bar or click |image74|
       on the Standard Toolbar.



   To save a project using a different name:

      1. Select **File >> Save As** from the Menu Bar.

      2. A standard File Save dialog form will appear from which you can
         select the folder and name that the project should be saved under.



   **Note:** Projects are always saved as binary .NET files. To save a
   project's data as readable ASCII text, use the **Export >> Network**
   command from the **File** menu.

Project Defaults
~~~~~~~~~~~~~~~~

   Each project has a set of default values that are used unless
   overridden by the EPANET user. These values fall into three
   categories:

    -  Default ID labels (labels used to identify nodes and links when they
       are first created)

    -  Default node/link properties (e.g., node elevation, pipe length,
       diameter, and roughness)

    -  Default hydraulic analysis options (e.g., system of units, headloss
       equation, etc.)



   To set default values for a project:

      1. Select **Project >> Defaults** from the Menu Bar.

      2. A Defaults dialog form will appear with three pages, one for each
         category listed above.

      3. Check the box in the lower right of the dialog form if you want to
         save your choices for use in all new future projects as well.

      4. Click **OK** to accept your choice of defaults.



   The specific items for each category of defaults will be discussed
   next.

   **Default ID Labels**

   The ID Labels page of the Defaults dialog form is shown in Figure 5.1
   below. It is used to determine how EPANET will assign default ID
   labels to network components when they are first created. For each
   type of object one can enter a label prefix or leave the field blank
   if the default ID will simply be a number. Then one supplies an
   increment to be used when adding a numerical suffix to the default
   label. As an example, if J were used as a prefix for Junctions along
   with an increment of 5, then as junctions are created they receive
   default labels of J5, J10, J15 and so on. After an object has been
   created, the Property Editor can be used to modify its ID label if
   need be.

   |image75|

   **Figure 5.1** ID Labels Page of Project Defaults Dialog

   
   **Default Node/Link Properties**

   The Properties page of the Defaults dialog form is shown in Figure
   5.2. It sets default property values for newly created nodes and
   links. These properties include:

    -  Elevation for nodes

    -  Diameter for tanks

    -  Maximum water level for tanks

    -  Length for pipes

    -  Auto-Length (automatic calculation of length) for pipes

    -  Diameter for pipes

    -  Roughness for pipes

..

   When the Auto-Length property is turned on, pipe lengths will
   automatically be computed as pipes are added or repositioned on the
   network map. A node or link created with these default properties can
   always be modified later on using the Property Editor.

   |image76|

   **Figure 5.2** Properties Page of the Project Defaults Dialog

   
   **Default Hydraulic Options**

   The third page of the Defaults dialog form is used to assign default
   hydraulic analysis options. It contains the same set of hydraulic
   options as the project's Hydraulic Options accessed from the Browser
   (see Section 8.1). They are repeated on the Project Defaults dialog
   so that they can be saved for use with future projects as well as
   with the current one. The most important Hydraulic Options to check
   when setting up a new project are Flow Units, Headloss Formula, and
   Default Pattern. The choice of Flow Units determines whether all
   other network quantities are expressed in Customary US units or in SI
   metric units. The choice of Headloss Formula defines the type of the
   roughness coefficient to be supplied for each pipe in the network.
   The Default Pattern automatically becomes the time pattern used to
   vary demands in an extended period simulation for all junctions not
   assigned any pattern.

Calibration Data
~~~~~~~~~~~~~~~~

   EPANET allows you to compare results of a simulation against measured
   field data. This can be done via Time Series plots for selected
   locations in the network or by special Calibration Reports that
   consider multiple locations. Before EPANET can use such calibration
   data it has to be entered into a file and registered with the
   project.

   Calibration Files

   A Calibration File is a text file containing measured data for a
   particular quantity taken over a particular period of time within a
   distribution system. The file provides observed data that can be
   compared to the results of a network simulation. Separate files
   should be created for different parameters (e.g., pressure, fluoride,
   chlorine, flow, etc.) and different sampling studies. Each line of
   the file contains the following items:

    -  Location ID - ID label (as used in the network model) of the location
       where the measurement was made

    -  Time - Time (in hours) when the measurement was made

    -  Value - Result of the measurement



   The measurement time is with respect to time zero of the simulation
   to which the Calibration File will be applied. It can be entered as
   either a decimal number (e.g., 27.5) or in hours:minutes format
   (e.g., 27:30). For data to be used in a single period analysis all
   time values can be 0. Comments can be added to the file by placing a
   semicolon (;) before them. For a series of measurements made at the
   same location the Location ID does not have to be repeated. An
   excerpt from a Calibration File is shown below.
   
    ::
      
      ;Fluoride Tracer Measurements
   
      ;Location  Time   Value
      
      ;--------------------------
      
             N1    0      0.5   
                   6.4    1.2   
                  12.7    0.9   
             N2    0.5    0.72  
                   5.6    0.77  


   Registering Calibration Data

   To register calibration data residing in a Calibration File:

      1. Select **Project >> Calibration Data** from the Menu Bar.

      2. In the Calibration Data dialog form shown in Figure 5.3, click in
         the box next to the parameter you wish to register data for.

      3. Either type in the name of a Calibration File for this parameter or
         click the **Browse** button to search for it.

      4. Click the **Edit** button if you want to open the Calibration File
         in Windows NotePad for editing.

      5. Repeat steps 2 - 4 for any other parameters that have calibration
         data.

      6. Click **OK** to accept your selections.

..

   |image77|

   **Figure 5.3** Calibration Data Dialog

Project Summary
~~~~~~~~~~~~~~~

   To view a summary description of the current project select **Project
   >> Summary** from the Menu Bar. The Project Summary dialog form will
   appear in which you can edit a descriptive title for the project as
   well as add notes that further describe the project. When you go to
   open a previously saved file, the Open File dialog box will display
   both of these items as different file names are selected. This makes
   them very useful for locating specific network analyses. The form
   also displays certain network statistics, such as the number of
   junctions, pipes, pumps, etc.


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

