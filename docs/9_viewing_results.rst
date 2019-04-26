.. raw:: latex

    \clearpage


9. VIEWING RESULTS
==================
    
*This chapter describes the different ways in which the results of an
analysis as well as the basic network input data can be viewed. These
include different map views, graphs, tables, and special reports.*

-------



Viewing Results on the Map
~~~~~~~~~~~~~~~~~~~~~~~~~~

  There are several ways in which database values and results of a
  simulation can be viewed directly on the Network Map:

  -  For the current settings on the Map Browser (see Section 4.6), the
     nodes and links of the map will be colored according to the color-
     coding used in the Map Legends (see Section 7.6). The map's coloring
     will be updated as a new time period is selected in the Browser.

  -  When the Flyover Map Labeling program preference is selected (see
     Section 4.9), moving the mouse over any node or link will display its
     ID label and the value of the current viewing parameter for that node
     or link in a hint-style box.

  -  ID labels and viewing parameter values can be displayed next to all
     nodes and/or links by selecting the appropriate options on the
     Notation page of the Map Options dialog form (see Section 7.8).

  -  Nodes or links meeting a specific criterion can be identified by
     submitting a Map Query (see below).

  -  You can animate the display of results on the network map either
     forward or backward in time by using the Animation buttons on the Map
     Browser. Animation is only available when a node or link viewing
     parameter is a computed value (e.g., link flow rate can be animated
     but diameter cannot).

  -  The map can be printed, copied to the Windows clipboard, or saved as
     a DXF file or Windows metafile.



Submitting a Map Query
----------------------

  A Map Query identifies nodes or links on the network map that meet a
  specific criterion (e.g., nodes with pressure less than 20 psi, links
  with velocity above 2 ft/sec, etc.). See Figure 9.1 for an example.
  To submit a map query:

    |image115|

    **Figure 9.1** Results of a Map Query

    1. Select a time period in which to query the map from the Map Browser.

    2. Select **View >> Query** or click |image116| on the Map Toolbar.

    3. Fill in the following information in the Query dialog form that
       appears:

       -  Select whether to search for Nodes or Links

       -  Select a parameter to compare against

       -  Select **Above**, **Below,** or **Equals**

       -  Enter a value to compare against

    4. Click the **Submit** button. The objects that meet the criterion will
       be highlighted on the map.

    5. As a new time period is selected in the Browser, the query results
       are automatically updated.

    6. You can submit another query using the dialog box or close it by
       clicking the button in the upper right corner.



  After the Query box is closed the map will revert back to its
  original display.

   
Viewing Results with a Graph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Analysis results, as well as some design parameters, can be viewed
  using several different types of graphs. Graphs can be printed,
  copied to the Windows clipboard, or saved as a data file or Windows
  metafile. The following types of graphs can be used to view values
  for a selected parameter (see Figure 9.2 for examples of each):


  +-----------------------+-----------------------+-----------------------+
  | *Type of Plot*        | *Description*         | *Applies To*          |
  +=======================+=======================+=======================+
  | Time Series Plot      | Plots value versus    | Specific nodes or     |
  |                       | time                  | links                 |
  +-----------------------+-----------------------+-----------------------+
  |                       |                       | over all time periods |
  +-----------------------+-----------------------+-----------------------+
  | Profile Plot          | Plots value versus    | A list of nodes at a  |
  |                       | distance              |                       |
  +-----------------------+-----------------------+-----------------------+
  |                       |                       | specific time         |
  +-----------------------+-----------------------+-----------------------+
  | Contour Plot          | Shows regions of the  | All nodes at a        |
  |                       | map                   | specific time         |
  +-----------------------+-----------------------+-----------------------+
  |                       | where values fall     |                       |
  |                       | within specific       |                       |
  |                       | intervals             |                       |
  +-----------------------+-----------------------+-----------------------+
  | Frequency Plot        | Plots value versus    | All nodes or links at |
  |                       | fraction of           | a specific time       |
  +-----------------------+-----------------------+-----------------------+
  |                       | objects at or below   |                       |
  |                       | the value             |                       |
  +-----------------------+-----------------------+-----------------------+
  | System Flow           | Plots total system    | Water demand for all  |
  |                       | production            | nodes over all time   |
  |                       |                       | periods               |
  +-----------------------+-----------------------+-----------------------+
  |                       | and consumption       |                       |
  |                       | versus time           |                       |
  +-----------------------+-----------------------+-----------------------+

   **Note**: When only a single node or link is graphed in a Time Series
   Plot the graph will also display any measured data residing in a
   Calibration File that has been registered with the project (see
   Section 5.3).

  To create a graph:

    1. Select **Report >> Graph** or click |image117| on the Standard
       Toolbar.

    2. Fill in the choices on the Graph Selection dialog box that appears.

    3. Click **OK** to create the graph.


  The Graph Selection dialog, as pictured in Figure 9.3, is used to
  select a type of graph and its contents to display. The choices
  available in the dialog consist of the following:

  +-----------------------------------+-----------------------------------+
  | *Item*                            | *Description*                     |
  +===================================+===================================+
  | Graph Type                        | Selects a graph type              |
  +-----------------------------------+-----------------------------------+
  | Parameter                         | Selects a parameter to graph      |
  +-----------------------------------+-----------------------------------+
  | Time Period                       | Selects a time period to graph    |
  |                                   | (does not apply to Time Series    |
  |                                   | plots)                            |
  +-----------------------------------+-----------------------------------+
  | Object Type                       | Selects either Nodes or Links     |
  |                                   | (only Nodes can be graphed on     |
  |                                   | Profile and Contour plots)        |
  +-----------------------------------+-----------------------------------+
  | Items to Graph                    | Selects items to graph (applies   |
  |                                   | only to Time Series and Profile   |
  |                                   | plots)                            |
  +-----------------------------------+-----------------------------------+


      |image118|

      |image119|

      |image120|

      |image121|

      |image122|

    **Figure 9.2** Examples of Different Types of Graphs

    
      |image123|

    **Figure 9.3** Graph Selection Dialog

  Time Series plots and Profile plots require one or more objects be
  selected for plotting. To select items into the Graph Selection
  dialog for plotting:

    1. Select the object (node or link) either on the Network Map or on the
       Data Browser. (The Graph Selection dialog will remain visible during
       this process).

    2. Click the **Add** button on the Graph Selection dialog to add the
       selected item to the list.


  In place of Step 2, you can also drag the object’s label from the
  Data Browser onto the Form’s title bar or onto the Items to Graph
  list box.

  The other buttons on the **Graph Selection** dialog form are used as
  follows:


  +-----------------------------------+-----------------------------------+
  | *Button*                          | *Purpose*                         |
  +===================================+===================================+
  | Load (Profile Plot Only)          | Loads a previously saved list of  |
  |                                   | nodes                             |
  +-----------------------------------+-----------------------------------+
  | Save (Profile Plot Only)          | Saves current list of nodes to    |
  |                                   | file                              |
  +-----------------------------------+-----------------------------------+
  | Delete                            | Deletes selected item from list   |
  +-----------------------------------+-----------------------------------+
  | Move Up                           | Moves selected item on list up    |
  |                                   | one position                      |
  +-----------------------------------+-----------------------------------+
  | Move Down                         | Moves selected item on list       |
  |                                   | down one position                 |
  +-----------------------------------+-----------------------------------+



   To customize the appearance of a graph:

    1. Make the graph the active window (click on its title bar).

    2. Select **Report >> Options**, or click |image124| on the Standard
       Toolbar, or right-click on the graph.

    3. For a Time Series, Profile, Frequency or System Flow plot, use the
       resulting Graph Options dialog (Figure 9.4) to customize the graph's
       appearance.

    4. For a Contour plot use the resulting Contour Options dialog to
       customize the plot.

    

    **Note**: A Time Series, Profile, or Frequency plot can be zoomed by
    holding down the **Ctrl** key while drawing a zoom rectangle with the
    mouse's left button held down. Drawing the rectangle from left to
    right zooms in, drawing from right to left zooms out. The plot can
    also be panned in any direction by holding down the **Ctrl** key and
    moving the mouse across the plot with the right button held down.

   The Graph Options dialog form (Figure 9.4) is used to customize the
   appearance of an X-Y graph. To use the dialog box:

    1. Select from among the five tabbed pages that cover the following
       categories of options:

       -  General

       -  Horizontal Axis

       -  Vertical Axis

       -  Legend

       -  Series

    2. Check the **Default** box if you wish to use the current settings as
       defaults for all new graphs as well.

    3. Select **OK** to accept your selections.

    

   The items contained on each page of the Graph Options dialog are as
   follows:

General Page
------------

  +-----------------------------------+-----------------------------------+
  | *Option*                          | *Description*                     |
  +===================================+===================================+
  | Panel Color                       | Color of the panel which          |
  |                                   | surrounds the graph’s plotting    |
  |                                   | area                              |
  +-----------------------------------+-----------------------------------+
  | Background Color                  | Color of graph's plotting area    |
  +-----------------------------------+-----------------------------------+
  | View in 3D                        | Check if graph should be drawn in |
  |                                   | 3D                                |
  +-----------------------------------+-----------------------------------+
  | 3D Effect Percent                 | Degree to which 3D effect is      |
  |                                   | drawn                             |
  +-----------------------------------+-----------------------------------+
  | Main Title                        | Text of graph's main title        |
  +-----------------------------------+-----------------------------------+
  | Font                              |                                   |
  |                                   | Changes the font used for         |
  |                                   | the main title                    |
  +-----------------------------------+-----------------------------------+


   |image125|

   **Figure 9.4** Graph Options Dialog

   Horizontal and Vertical Axis Pages


  +-----------------------------------+-----------------------------------+
  | *Option*                          | *Description*                     |
  +===================================+===================================+
  | Minimum                           | Sets minimum axis value (minimum  |
  |                                   | data value is shown in            |
  |                                   | parentheses). Can be left blank.  |
  +-----------------------------------+-----------------------------------+
  | Maximum                           | Sets maximum axis value (maximum  |
  |                                   | data value is shown in            |
  |                                   | parentheses). Can be left blank.  |
  +-----------------------------------+-----------------------------------+
  | Increment                         | Sets increment between axis       |
  |                                   | labels. Can be left blank.        |
  +-----------------------------------+-----------------------------------+
  | Auto Scale                        | If checked then Minimum, Maximum, |
  |                                   | and Increment settings are        |
  |                                   | ignored.                          |
  +-----------------------------------+-----------------------------------+
  | Gridlines                         | Selects type of gridline to draw. |
  +-----------------------------------+-----------------------------------+
  | Axis Title                        | Text of axis title                |
  +-----------------------------------+-----------------------------------+
  | Font                              | Click to select a font for        |
  |                                   | the axis title.                   |
  +-----------------------------------+-----------------------------------+



   Legend Page



  +-----------------------------------+-----------------------------------+
  | *Option*                          | *Description*                     |
  +===================================+===================================+
  | Position                          | Selects where to place the        |
  |                                   | legend.                           |
  +-----------------------------------+-----------------------------------+
  | Color                             | Selects color to use for legend   |
  |                                   | background.                       |
  +-----------------------------------+-----------------------------------+
  | Symbol Width                      | Selects width to use (in pixels)  |
  |                                   | to draw symbol portion of the     |
  |                                   | legend.                           |
  +-----------------------------------+-----------------------------------+
  | Framed                            | Places a frame around the legend. |
  +-----------------------------------+-----------------------------------+
  | Visible                           | Makes the legend visible.         |
  +-----------------------------------+-----------------------------------+


   
Series Page
-----------

   The Series page (see Figure 9.4) of the Graph Options dialog controls
   how individual data series (or curves) are displayed on a graph. To
   use this page:

    -  Select a data series to work with from the Series combo box.

    -  Edit the title used to identify this series in the legend.

    -  Click the Font button to change the font used for the legend. (Other
       legend properties are selected on the Legend page of the dialog.)

    -  Select a property of the data series you would like to modify. The
       choices are:

       -  Lines

       -  Markers

       -  Patterns

       -  Labels

       (Not all properties are available for some types of graphs.)

   The data series properties that can be modified include the
   following:

    +-----------------------+-----------------------+-----------------------+
    |    *Category*         |    *Option*           |    *Description*      |
    +=======================+=======================+=======================+
    |    *Lines*            |    Style              |    Selects line       |
    |                       |                       |    style.             |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Color              |    Selects line       |
    |                       |                       |    color.             |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Size               |    Selects line       |
    |                       |                       |    thickness (only    |
    |                       |                       |    for solid line     |
    |                       |                       |    style).            |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Visible            |    Determines if line |
    |                       |                       |    is visible.        |
    +-----------------------+-----------------------+-----------------------+
    | *Markers*             |    Style              |    Selects marker     |
    |                       |                       |    style.             |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Color              |    Selects marker     |
    |                       |                       |    color.             |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Size               |    Selects marker     |
    |                       |                       |    size.              |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Visible            |    Determines if      |
    |                       |                       |    marker is visible. |
    +-----------------------+-----------------------+-----------------------+
    | *Patterns*            |    Style              |    Selects pattern    |
    |                       |                       |    style.             |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Color              |    Selects pattern    |
    |                       |                       |    color.             |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Stacking           |    Not used with      |
    |                       |                       |    EPANET.            |
    +-----------------------+-----------------------+-----------------------+
    | *Labels*              |    Style              |    Selects what type  |
    |                       |                       |    of information is  |
    |                       |                       |    displayed in the   |
    |                       |                       |    label.             |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Color              |    Selects the color  |
    |                       |                       |    of the label's     |
    |                       |                       |    background.        |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Transparent        |    Determines if      |
    |                       |                       |    graph shows        |
    |                       |                       |    through label or   |
    |                       |                       |    not.               |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Show Arrows        |    Determines if      |
    |                       |                       |    arrows are         |
    |                       |                       |    displayed on pie   |
    |                       |                       |    charts.            |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Visible            |    Determines if      |
    |                       |                       |    labels are visible |
    |                       |                       |    or not.            |
    +-----------------------+-----------------------+-----------------------+



   The Contour Options dialog form (Figure 9.5) is used to customize the
   appearance of a contour graph. A description of each option is
   provided below:

    |image126|

    **Figure 9.5** Contour Plot Options Dialog

    +-----------------------+-----------------------+-----------------------+
    |    *Category*         |    *Option*           |    *Description*      |
    +=======================+=======================+=======================+
    |    *Legend*           |    Display Legend     |    Toggles display of |
    |                       |                       |    legend on/off      |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Modify Legend      |    Changes colors and |
    |                       |                       |    contour intervals  |
    +-----------------------+-----------------------+-----------------------+
    |    *Network*          |                       |                       |
    +-----------------------+-----------------------+-----------------------+
    |    *Backdrop*         |    Foreground         |    Color of network   |
    |                       |                       |    image displayed on |
    |                       |                       |    plot               |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Background         |    Background color   |
    |                       |                       |    used for line      |
    |                       |                       |    contour plot       |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Link Size          |    Thickness of lines |
    |                       |                       |    used to display    |
    |                       |                       |    network            |
    +-----------------------+-----------------------+-----------------------+
    |    *Style*            |    Filled Contours    |    Plot uses colored  |
    |                       |                       |    area-filled        |
    |                       |                       |    contours           |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Line Contours      |    Plot uses colored  |
    |                       |                       |    line contours      |
    +-----------------------+-----------------------+-----------------------+
    |    *Contour Lines*    |    Thickness          |    Thickness of lines |
    |                       |                       |    used for contour   |
    |                       |                       |    intervals          |
    +-----------------------+-----------------------+-----------------------+
    |                       |    Lines per Level    |    Number of          |
    |                       |                       |    sub-contours per   |
    |                       |                       |    major contour      |
    |                       |                       |    level              |
    +-----------------------+-----------------------+-----------------------+
    |    *Default*          |                       |    Saves choices as   |
    |                       |                       |    defaults for next  |
    |                       |                       |    contour plot       |
    +-----------------------+-----------------------+-----------------------+

Viewing Results with a Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   EPANET allows you to view selected project data and analysis results
   in a tabular format:

    -  A Network Table lists properties and results for all nodes or links
       at a specific period of time.

    -  A Time Series Table lists properties and results for a specific node
       or link in all time periods.



   Tables can be printed, copied to the Windows clipboard, or saved to
   file. An example table is shown in Figure 9.6.

   To create a table:

    1. Select **View >> Table** or click |image127| on the Standard Toolbar.

    2. Use the Table Options dialog box that appears to select:

       -  the type of table

       -  the quantities to display in each column

       -  any filters to apply to the data

      |image128|

     **Figure 9.6** Example Network Nodes Table

   The Table Options dialog form has three tabbed pages as shown in
   Figure 9.7. All three pages are available when a table is first
   created. After the table is created, only the Columns and Filters
   tabs will appear. The options available on each page are as follows:

      |image129|

     **Figure 9.7** Table Selection Dialog

Type Page
----------

   The Type page of the Table Options dialog is used to select the type
   of table to create. The choices are:

    -  All network nodes at a specific time period

    -  All network links at a specific time period

    -  All time periods for a specific node

    -  All time periods for a specific link


   Data fields are available for selecting the time period or node/link
   to which the table applies.

Columns Page
-------------

   The Columns page of the Table Options dialog form (Figure 9.8)
   selects the parameters that are displayed in the table’s columns.

    -  Click the checkbox next to the name of each parameter you wish to
       include in the table, or if the item is already selected, click in
       the box to deselect it. (The keyboard's Up and Down Arrow keys can be
       used to move between the parameter names, and the spacebar can be
       used to select/deselect choices).

    -  To sort a Network-type table with respect to the values of a
       particular parameter, select the parameter from the list and check
       off the **Sorted By** box at the bottom of the form. (The sorted
       parameter does not have to be selected as one of the columns in the
       table.) Time Series tables cannot be sorted.

      |image130|

     **Figure 9.8** Columns Page of the Table Selection Dialog

Filters Page
-------------

   The Filters page of the Table Options dialog form (Figure 9.9) is
   used to define conditions for selecting items to appear in a table.
   To filter the contents of a table:

    -  Use the controls at the top of the page to create a condition (e.g.,
       Pressure Below 20).

    -  Click the **Add** button to add the condition to the list.

    -  Use the **Delete** button to remove a selected condition from the
       list.


   Multiple conditions used to filter the table are connected by AND's.
   If a table has been filtered, a re-sizeable panel will appear at the
   bottom indicating how many items have satisfied the filter
   conditions.

      |image131|

     **Figure 9.9** Filters Page of the Table Selection Dialog

   Once a table has been created you can add/delete columns or sort or
   filter its data:

    -  Select **Report >> Options** or click |image132| on the Standard
       Toolbar or right-click on the table.

    -  Use the Columns and Filters pages of the Table Selection dialog form
       to modify your table.

Viewing Special Reports
~~~~~~~~~~~~~~~~~~~~~~~

   In addition to graphs and tables, EPANET can generate several other
   specialized reports. These include:

    -  Status Report

    -  Energy Report

    -  Calibration Report

    -  Reaction Report

    -  Full Report



   All of these reports can be printed, copied to a file, or copied to
   the Windows clipboard (the Full Report can only be saved to file.)

Status Report
--------------

   EPANET writes all error and warning messages generated during an
   analysis to a Status Report (see Figure 9.10). Additional information
   on when network objects change status is also written to this report
   if the Status Report option in the project's Hydraulics Options was
   set to Yes or Full. To view a status report on the most recently
   completed analysis select **Report >> Status** from the main menu.

      |image133|

     **Figure 9.10** Excerpt from a Status Report

Energy Report
--------------

   EPANET can generate an Energy Report that displays statistics about
   the energy consumed by each pump and the cost of this energy usage
   over the duration of a simulation (see Figure 9.11). To generate an
   Energy Report select **Report >> Energy** from the main menu. The
   report has two tabbed pages. One displays energy usage by pump in a
   tabular format. The second compares a selected energy statistic
   between pumps using a bar chart.

      |image134|

     **Figure 9.11** Example Energy Report

Calibration Report
-------------------

   A Calibration Report can show how well EPANET's simulated results
   match measurements taken from the system being modeled. To create a
   Calibration Report:

    1. First make sure that Calibration Data for the quantity being
       calibrated has been registered with the project (see Section 5.3).

    2. Select **Report >> Calibration** from the main menu.

    3. In the Calibration Report Options form that appears (see Figure
       9.12):

       -  select a parameter to calibrate against

       -  select the measurement locations to use in the report

    4. Click **OK** to create the report.



   After the report is created the Calibration Report Options form can
   be recalled to change report options by selecting **Report >>
   Options** or by clicking |image135| on the Standard Toolbar when the
   report is the current active window in EPANET’s workspace.

   A sample Calibration Report is shown in Figure 9.13. It contains
   three tabbed pages: Statistics, Correlation Plot, and Mean
   Comparisons.

Statistics Page
----------------

   The Statistics page of a Calibration Report lists various error
   statistics between simulated and observed values at each measurement
   location and for the network as a whole. If a measured value at a
   location was taken at a time in-between the simulation's reporting
   time intervals then a simulated value for that time is found by
   interpolating between the simulated values at either end of the
   interval.

      |image136|

     **Figure 9.12** Calibration Report Options Dialog

      |image137|

     **Figure 9.13** Example Calibration Report

   The statistics listed for each measurement location are:

    -  Number of observations

    -  Mean of the observed values

    -  Mean of the simulated values

    -  Mean absolute error between each observed and simulated value

    -  Root mean square error (square root of the mean of the squared errors
       between the observed and simulated values).



   These statistics are also provided for the network as a whole (i.e.,
   all measurements and model errors pooled together). Also listed is
   the correlation between means (correlation coefficient between the
   mean observed value and mean simulated value at each location).

   **Correlation Plot Page**

   The Correlation Plot page of a Calibration Report displays a scatter
   plot of the observed and simulated values for each measurement made
   at each location. Each location is assigned a different color in the
   plot. The closer that the points come to the 45-degree angle line on
   the plot the closer is the match between observed and simulated
   values.

   **Mean Comparisons Page**

   The Mean Comparisons page of a Calibration Report presents a bar
   chart that compares the mean observed and mean simulated value for a
   calibration parameter at each location where measurements were taken.

   **Reaction Report**

   A Reaction Report, available when modeling the fate of a reactive
   water quality constituent, graphically depicts the overall average
   reaction rates occurring throughout the network in the following
   locations:

    -  the bulk flow

    -  the pipe wall

    -  within storage tanks.



   A pie chart shows what percent of the overall reaction rate is
   occurring in each location. The chart legend displays the average
   rates in mass units per hour. A footnote on the chart shows the
   inflow rate of the reactant into the system.

   The information in the Reaction Report can show at a glance what
   mechanism is responsible for the majority of growth or decay of a
   substance in the network. For example, if one observes that most of
   the chlorine decay in a system is occurring in the storage tanks and
   not at the walls of the pipes then one might infer that a corrective
   strategy of pipe cleaning and replacement will have little effect in
   improving chlorine residuals.

   A Graph Options dialog box can be called up to modify the appearance
   of the pie chart by selecting **Report >> Options** or by clicking
   |image138| on the Standard Toolbar, or by right-clicking anywhere on
   the chart.

   **Full Report**

   When the |image139| icon appears in the Run Status section of the
   Status Bar, a report of computed results for all nodes, links and
   time periods can be saved to file by selecting **Full** from the
   **Report** menu. This report, which can be viewed or printed outside
   of EPANET using any text editor or word processor, contains the
   following information:

    -  project title and notes

    -  a table listing the end nodes, length, and diameter of each link

    -  a table listing energy usage statistics for each pump

    -  a pair of tables for each time period listing computed values for
       each node (demand, head, pressure, and quality) and for each link
       (flow, velocity, headloss, and status).

..

   This feature is useful mainly for documenting the final results of a
   network analysis on small to moderately sized networks (full report
   files for large networks analyzed over many time periods can easily
   consume dozens of megabytes of disk space). The other reporting tools
   described in this chapter are available for viewing computed results
   on a more selective basis.

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

