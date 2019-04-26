.. raw:: latex

    \clearpage

    
2. QUICK START TUTORIAL
=======================

    
*This chapter provides a tutorial on how to use EPANET. If you are
not familiar with the components that comprise a water distribution
system and how these are represented in pipe network models you might
want to review the first two sections of Chapter 3 first.*


-------

  
 
Installing EPANET
~~~~~~~~~~~~~~~~~

   EPANET Version 2 is designed to run under the Windows 95/98/NT
   operating system of an IBM/Intel-compatible personal computer. It is
   distributed as a single file, **en2setup.exe**, which contains a
   self-extracting setup program. To install EPANET:

    1. Select **Run** from the Windows Start menu.

    2. Enter the full path and name of the **en2setup.exe** file or click
       the **Browse** button to locate it on your computer.

    3. Click the **OK** button type to begin the setup process.



   The setup program will ask you to choose a folder (directory) where
   the EPANET files will be placed. The default folder is **c:\Program
   Files\EPANET2**. After the files are installed your Start Menu will
   have a new item named EPANET 2.0. To launch EPANET simply select this
   item off of the Start Menu, then select EPANET 2.0 from the submenu that 
   appears. (The name of the executable file that runs EPANET under 
   Windows is **epanet2w.exe**.)

   Should you wish to remove EPANET from your computer, you can use the
   following procedure:

    1. Select **Settings** from the Windows Start menu.

    2. Select **Control Panel** from the Settings menu.

    3. Double-click on the **Add/Remove Programs** item.

    4. Select EPANET 2.0 from the list of programs that appears.

    5. Click the **Add/Remove** button.

    
Example Network
~~~~~~~~~~~~~~~~


   In this tutorial we will analyze the simple distribution network
   shown in Figure 2.1 below. It consists of a source reservoir (e.g., a
   treatment plant clearwell) from which water is pumped into a two-loop
   pipe network. There is also a pipe leading to a storage tank that
   floats on the system. The ID labels for the various components are
   shown in the figure. The nodes in the network have the
   characteristics shown in Table 2.1. Pipe properties are listed in
   Table 2.2. In addition, the pump (Link 9) can
   deliver 150 ft of head at a flow of 600 gpm, and the tank (Node 8)
   has a 60-ft diameter, a 3.5-ft water level, and a maximum level of 20
   feet.

        |image0|

    **Figure 2.1** Example Pipe Network

    **Table 2.1** Example Network Node Properties
    
    +------+-----------+--------+
    | Node | Elevation | Demand |
    |      | (ft)      | (gpm)  |
    +======+===========+========+
    |    1 |    700    | 0      |
    +------+-----------+--------+
    |    2 |    700    | 0      |
    +------+-----------+--------+
    |    3 |    710    |    150 |
    +------+-----------+--------+
    |    4 |    700    |    150 |
    +------+-----------+--------+
    |    5 |    650    |    200 |
    +------+-----------+--------+
    |    6 |    700    |    150 |
    +------+-----------+--------+
    |    7 |    700    | 0      |
    +------+-----------+--------+
    |    8 |    830    | 0      |
    +------+-----------+--------+



    **Table 2.2** Example Network Pipe Properties
    
    +---------+----------------+----------------------+-------------+
    |    Pipe |    Length (ft) |    Diameter (inches) |    C-Factor |
    +=========+================+======================+=============+
    | 1       |    3000        |    14                |    100      |
    +---------+----------------+----------------------+-------------+
    | 2       |    5000        |    12                |    100      |
    +---------+----------------+----------------------+-------------+
    | 3       |    5000        |    8                 |    100      |
    +---------+----------------+----------------------+-------------+
    | 4       |    5000        |    8                 |    100      |
    +---------+----------------+----------------------+-------------+
    | 5       |    5000        |    8                 |    100      |
    +---------+----------------+----------------------+-------------+
    | 6       |    7000        |    10                |    100      |
    +---------+----------------+----------------------+-------------+
    | 7       |    5000        |    6                 |    100      |
    +---------+----------------+----------------------+-------------+
    | 8       |    7000        |    6                 |    100      |
    +---------+----------------+----------------------+-------------+

Project Setup
~~~~~~~~~~~~~

   Our first task is to create a new project in EPANET and make sure
   that certain default options are selected. To begin, launch EPANET,
   or if it is already running select **File >> New** (from the menu
   bar) to create a new project. Then select **Project**
   **>> Defaults** to open the dialog form shown in Figure 2.2. We will
   use this dialog to have EPANET automatically label new objects with
   consecutive numbers starting from 1 as they are added to the network.
   On the ID Labels page of the dialog, clear all of the ID Prefix
   fields and set the ID Increment to 1. Then select the Hydraulics page
   of the dialog and set the choice of Flow Units to GPM (gallons per
   minute). This implies that US Customary units will be used for all
   other quantities as well (length in feet, pipe diameter in inches,
   pressure in psi, etc.). Also select Hazen    - Williams (H-W) as the
   headloss formula. If you wanted to save these choices for all future
   new projects you could check the **Save** box at the bottom of the
   form before accepting it by clicking the **OK** button.

      |image1|

    **Figure 2.2** Project Defaults Dialog

   Next we will select some map display options so that as we add
   objects to the map, we will see their ID labels and symbols
   displayed. Select **View >> Options** to bring up the Map Options
   dialog form. Select the Notation page on this form and check the
   settings shown in Figure 2.3 below. Then switch to the Symbols page
   and check all of the boxes. Click the **OK** button to accept these
   choices and close the dialog.

   Finally, before drawing our network we should insure that our map
   scale settings are acceptable. Select **View >> Dimensions** to bring
   up the Map Dimensions dialog. Note the default dimensions assigned
   for a new project. These settings will suffice for this example, so
   click the **OK** button.

      |image2|

    **Figure 2.3** Map Options Dialog

Drawing the Network
~~~~~~~~~~~~~~~~~~~

   We are now ready to begin drawing our network by making use of our
   mouse and the buttons contained on the Map Toolbar shown below. (If
   the toolbar is not visible then select **View >> Toolbars >> Map**).

    |image3|

   First we will add the reservoir. Click the Reservoir button |image4|.
   Then click the mouse on the map at the location of the reservoir
   (somewhere to the left of the map).

   Next we will add the junction nodes. Click the Junction button
   |image5| and then click on the map at the locations of nodes 2
   through 7.

   Finally add the tank by clicking the Tank button |image6| and
   clicking the map where the tank is located. At this point the Network
   Map should look something like the drawing in Figure 2.4.

    |image7|

   **Figure 2.4** Network Map after Adding Nodes

   Next we will add the pipes. Let’s begin with pipe 1 connecting node 2
   to node 3. First click the Pipe button |image8| on the Toolbar. Then
   click the mouse on node 2 on the map and then on node 3. Note how an
   outline of the pipe is drawn as you move the mouse from node 2 to 3.
   Repeat this procedure for pipes 2 through 7.

   Pipe 8 is curved. To draw it, click the mouse first on Node 5. Then
   as you move the mouse towards Node 6, click at those points where a
   change of direction is needed to maintain the desired shape. Complete
   the process by clicking on Node 6.

   Finally we will add the pump. Click the Pump button |image9|, click
   on node 1 and then on node 2.

   Next we will label the reservoir, pump and tank. Select the Text
   button |image10| on the Map Toolbar and click somewhere close to the
   reservoir (Node 1). An edit box will appear. Type in the word SOURCE
   and then hit the **Enter** key. Click next to the pump and enter its
   label, then do the same for the tank. Then click the Selection button
   |image11| on the Toolbar to put the map into Object Selection mode
   rather than Text Insertion mode.

   At this point we have completed drawing the example network. Your
   Network Map should look like the map in Figure 2.1. If the nodes are
   out of position you can move them around by clicking the node to
   select it, and then dragging it with the left mouse button held down
   to its new position. Note how pipes connected to the node are moved
   along with the node. The labels can be repositioned in similar
   fashion. To re    - shape the curved Pipe 8:

    1. First click on Pipe 8 to select it and then click the |image12|
       button on the Map Toolbar to put the map into Vertex Selection mode.

    2. Select a vertex point on the pipe by clicking on it and then drag it
       to a new position with the left mouse button held down.

    3. If required, vertices can be added or deleted from the pipe by right-
       clicking the mouse and selecting the appropriate option from the
       popup menu that appears.

    4. When finished, click |image13| to return to Object Selection mode.

Setting Object Properties
~~~~~~~~~~~~~~~~~~~~~~~~~

   As objects are added to a project they are assigned a default set of
   properties. To change the value of a specific property for an object
   one must select the object into the Property Editor (Figure 2.5).
   There are several different ways to do this. If the Editor is already
   visible then you can simply click on the object or select it from the
   Data page of the Browser. If the Editor is not visible then you can
   make it appear by one of the following actions:

    - Double-click the object on the map.

    - Right-click on the object and select **Properties** from the pop-up
      menu that appears.

    - Select the object from the Data page of the Browser window and then
      click the Browser’s Edit button |image14|.


   Whenever the Property Editor has the focus you can press the F1 key
   to obtain fuller descriptions of the properties listed

      |image15|

     **Figure 2.5** Property Editor

   Let us begin editing by selecting Node 2 into the Property Editor as
   shown above. We would now enter the elevation and demand for this
   node in the appropriate fields. You can use the **Up** and **Down**
   arrows on the keyboard or the mouse to move between fields. We need
   only click on another object (node or link) to have its properties
   appear next in the Property Editor. (We could also press the **Page
   Down** or **Page Up** key to move to the next or previous object of
   the same type in the database.) Thus we can simply move from object
   to object and fill in elevation and demand for nodes, and length,
   diameter, and roughness (C-factor) for links.

   For the reservoir you would enter its elevation (700) in the Total
   Head field. For the tank, enter 830 for its elevation, 4 for its
   initial level, 20 for its maximum level, and 60 for its diameter. For
   the pump, we need to assign it a pump curve (head versus flow
   relationship). Enter the ID label 1 in the Pump Curve field.

   Next we will create Pump Curve 1. From the Data page of the Browser
   window, select Curves from the dropdown list box and then click the
   Add button |image16|. A new Curve 1 will be added to the database and
   the Curve Editor dialog form will appear (see Figure 2.6). Enter the
   pump’s design flow (600) and head (150) into this form. EPANET
   automatically creates a complete pump curve from this single point.
   The curve’s equation is shown along with its shape. Click **OK** to
   close the Editor.

      |image17|

     **Figure 2.6** Curve Editor

Saving and Opening Projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Having completed the initial design of our network it is a good idea
   to save our work to a file at this point.

    1.  From the **File** menu select the **Save As** option.

    2.  In the Save As dialog that appears, select a folder and file name
        under which to save this project. We suggest naming the file
        **tutorial.net**. (An extension of **.net** will be added to the
        file name if one is not supplied.)

    3. Click **OK** to save the project to file.

   The project data is saved to the file in a special binary format. If
   you wanted to save the network data to file as readable text, use the
   **File >> Export >> Network** command instead.

   To open our project at some later time, we would select the **Open**
   command from the **File** menu.

Running a Single Period Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   We now have enough information to run a single period (or snapshot)
   hydraulic analysis on our example network. To run the analysis select
   **Project >> Run Analysis** or click the Run button |image18| on the
   Standard Toolbar. (If the toolbar is not visible select **View >>
   Toolbars >> Standard** from the menu bar).

   If the run was unsuccessful then a Status Report window will appear
   indicating what the problem was. If it ran successfully you can view
   the computed results in a variety of ways. Try some of the following:

    - Select Node Pressure from the Browser’s Map page and observe how
      pressure values at the nodes become color-coded. To view the legend
      for the color-coding, select **View >> Legends >> Node** (or right-
      click on an empty portion of the map and select Node Legend from the
      popup menu). To change the legend intervals and colors, right-click
      on the legend to make the Legend Editor appear.

    - Bring up the Property Editor (double-click on any node or link) and
      note how the computed results are displayed at the end of the
      property list.

    - Create a tabular listing of results by selecting **Report >> Table**
      (or by clicking the Table button |image19| on the Standard Toolbar).
      Figure

   2.7 displays such a table for the link results of this run. Note that
   flows with negative signs means that the flow is in the opposite
   direction to the direction in which the pipe was drawn initially.

      |image20|

     **Figure 2.7** Example Table of Link Results

Running an Extended Period Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   To make our network more realistic for analyzing an extended period
   of operation we will create a Time Pattern that makes demands at the
   nodes vary in a periodic way over the course of a day. For this
   simple example we will use a pattern time step of 6 hours thus making
   demands change at four different times of the day. (A 1-hour pattern
   time step is a more typical number and is the default assigned to new
   projects.) We set the pattern time step by selecting Options-Times
   from the Data Browser, clicking the Browser’s Edit button to make the
   Property Editor appear (if its not already visible), and entering 6
   for the value of the Pattern Time Step (as shown in Figure 2.8
   below). While we have the Time Options available we can also set the
   duration for which we want the extended period to run. Let’s use a
   3-day period of time (enter 72 hours for the Duration property).

      |image21|

     **Figure 2.8** Times Options

   To create the pattern, select the Patterns category in the Browser
   and then click the Add button |image22|. A new Pattern 1 will be
   created and the Pattern Editor dialog should appear (see Figure 2.9).
   Enter the multiplier values 0.5, 1.3, 1.0, 1.2 for the time periods 1
   to 4 that will give our pattern a duration of 24 hours. The
   multipliers are used to modify the demand from its base level in each
   time period. Since we are making a run of 72 hours, the pattern will
   wrap around to the start after each 24-hour interval of time.

      |image23|

     **Figure 2.9** Pattern Editor

   We now need to assign Pattern 1 to the Demand Pattern property of all
   of the junctions in our network. We can utilize one of EPANET’s
   Hydraulic Options to avoid having to edit each junction individually.
   If you bring up the Hydraulic Options in the Property Editor you will
   see that there is an item called Default Pattern. Setting its value
   equal to 1 will make the Demand Pattern at each junction equal
   Pattern 1, as long as no other pattern is assigned to the junction.

   Next run the analysis (select **Project >> Run Analysis** or click
   the |image24| button on the Standard Toolbar). For extended period
   analysis you have several more ways in which to view results:

    - The scrollbar in the Browser’s Time controls is used to display the
      network map at different points in time. Try doing this with Pressure
      selected as the node parameter and Flow as the link parameter.

    - The VCR-style buttons in the Browser can
      animate the map through time. Click the Forward button |image25|  to start the
      animation and the Stop button |image26|  to stop it.

    - Add flow direction arrows to the map (select **View >> Options**,
      select the Flow Arrows page from the Map Options dialog, and check a
      style of arrow that you wish to use). Then begin the animation again
      and note the change in flow direction through the pipe connected to
      the tank as the tank fills and empties over time.

    - Create a time series plot for any node or link. For example, to see
      how the water elevation in the tank changes with time:

      1. Click on the tank.

      2. Select **Report >> Graph** (or click the Graph button |image27|
         on the Standard Toolbar) which will display a Graph Selection
         dialog box.

      3. Select the Time Series button on the dialog.

      4. Select Head as the parameter to plot.

      5. Click **OK** to accept your choice of graph.



   Note the periodic behavior of the water elevation in the tank over
   time (Figure 2.10).

      |image28|

     **Figure 2.10** Example Time Series Plot

Running a Water Quality Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Next we show how to extend the analysis of our example network to
   include water quality. The simplest case would be tracking the growth
   in water age throughout the network over time. To make this analysis
   we only have to select Age for the Parameter property in the Quality
   Options (select Options-Quality from the Data page of the Browser,
   then click the Browser's Edit button to make the Property Editor
   appear). Run the analysis and select Age as the parameter to view on
   the map. Create a time series plot for Age in the tank. Note that
   unlike water level, 72 hours is not enough time for the tank to reach
   periodic behavior for water age. (The default initial condition is to
   start all nodes with an age of 0.) Try repeating the simulation using
   a 240-hour duration or assigning an initial age of 60 hours to the
   tank (enter 60 as the value of Initial Quality in the Property Editor
   for the tank).

   Finally we show how to simulate the transport and decay of chlorine
   through the network. Make the following changes to the database:

     1. Select Options-Quality to edit from the Data Browser. In the
        Property Editor’s Parameter field type in the word Chlorine.

     2. Switch to Options-Reactions in the Browser. For Global Bulk
        Coefficient enter a value of -1.0. This reflects the rate at which
        chlorine will decay due to reactions in the bulk flow over time.
        This rate will apply to all pipes in the network. You could edit
        this value for individual pipes if you needed to.

     3. Click on the reservoir node and set its Initial Quality to 1.0. This
        will be the concentration of chlorine that continuously enters the
        network. (Reset the initial quality in the Tank to 0 if you had
        changed it.)



   Now run the example. Use the Time controls on the Map Browser to see
   how chlorine levels change by location and time throughout the
   simulation. Note how for this simple network, only junctions 5, 6,
   and 7 see depressed chlorine levels because of being fed by low
   chlorine water from the tank. Create a reaction report for this run
   by selecting **Report >> Reaction** from the main menu. The report
   should look like Figure 2.11. It shows on average how much chlorine
   loss occurs in the pipes as opposed to the tank. The term “bulk”
   refers to reactions occurring in the bulk fluid while “wall” refers
   to reactions with material on the pipe wall. The latter reaction is
   zero because we did not specify any wall reaction coefficient in this
   example.

       |image29|

     **Figure 2.11** Example Reaction Report

   We have only touched the surface of the various capabilities offered
   by EPANET. Some additional features of the program that you should
   experiment with are:

   - Editing a property for a group of objects that lie within a user-
     defined area.

   - Using Control statements to base pump operation on time of day or
     tank water levels.

   - Exploring different Map Options, such as making node size be related
     to value.

   - Attaching a backdrop map (such as a street map) to the network map.

   - Creating different types of graphs, such as profile plots and contour
     plots.

   - Adding calibration data to a project and viewing a calibration
     report.

   - Copying the map, a graph, or a report to the clipboard or to a file.

   - Saving and retrieving a design scenario (i.e., current nodal demands,
     pipe roughness values, etc.).

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

