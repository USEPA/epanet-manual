.. raw:: latex

    \clearpage


.. _workspace:

EPANET's Workspace
==================


*This chapter discusses the essential features of EPANET’s workspace.
It describes the main menu bar, the tool and status bars, and the
three windows used most often – the Network Map, the Browser, and the
Property Editor. It also shows how to set program preferences.*

-------


Overview
~~~~~~~~

   The basic EPANET workspace is pictured below. It consists of the
   following user interface elements: a Menu Bar, two Toolbars, a Status
   Bar, the Network Map window, a Browser window, and a Property Editor
   window. A description of each of these elements is provided in the
   sections that follow.


   |image39|


Menu Bar
~~~~~~~~

   The Menu Bar located across the top of the EPANET workspace contains
   a collection of menus used to control the program. These include:

    -  File Menu

    -  Edit Menu

    -  View Menu

    -  Project Menu

    -  Report Menu

    -  Window Menu

    -  Help Menu


**File Menu**

   The File Menu contains commands for opening and saving data files and
   for printing:

  +---------------+------------------------------------------------------+
  | *Command*     | *Description*                                        |
  +===============+======================================================+
  | New           | Creates a new EPANET project                         |
  +---------------+------------------------------------------------------+
  | Open          | Opens an existing project                            |
  +---------------+------------------------------------------------------+
  | Save          | Saves the current project                            |
  +---------------+------------------------------------------------------+
  | Save As       | Saves the current project under a different name     |
  +---------------+------------------------------------------------------+
  | Import        | Imports network data or map from a file              |
  +---------------+------------------------------------------------------+
  | Export        | Exports network data or map to a file                |
  +---------------+------------------------------------------------------+
  | Page Setup    | Sets page margins, headers, and footers for printing |
  +---------------+------------------------------------------------------+
  | Print Preview | Previews a printout of the current view              |
  +---------------+------------------------------------------------------+
  | Print         | Prints the current view                              |
  +---------------+------------------------------------------------------+
  | Preferences   | Sets program preferences                             |
  +---------------+------------------------------------------------------+
  | Exit          | Exits EPANET                                         |
  +---------------+------------------------------------------------------+


**Edit Menu**

   The Edit Menu contains commands for editing and copying.

  +-----------------------------------+-----------------------------------+
  | *Command*                         | *Description*                     |
  +===================================+===================================+
  | Copy To                           | Copies the currently active view  |
  |                                   | (map, report, graph or table) to  |
  |                                   | the clipboard or to file          |
  +-----------------------------------+-----------------------------------+
  | Select Object                     | Allows selection of an object on  |
  |                                   | the map                           |
  +-----------------------------------+-----------------------------------+
  | Select Vertex                     | Allows selection of link vertices |
  |                                   | on the map                        |
  +-----------------------------------+-----------------------------------+
  | Select Region                     | Allows selection of an outlined   |
  |                                   | region on the map                 |
  +-----------------------------------+-----------------------------------+
  | Select All                        | Makes the outlined region the     |
  |                                   | entire viewable map area          |
  +-----------------------------------+-----------------------------------+
  | Group Edit                        | Edits a property for the group of |
  |                                   | objects that fall within the      |
  |                                   | outlined region of the map        |
  +-----------------------------------+-----------------------------------+


**View Menu**

   The View Menu controls how the network map is viewed.

  +--------------+-----------------------------------------------------------+
  | *Command*    | *Description*                                             |
  +==============+===========================================================+
  | Dimensions   | Dimensions the map                                        |
  +--------------+-----------------------------------------------------------+
  | Backdrop     | Allows a backdrop map to be viewed                        |
  +--------------+-----------------------------------------------------------+
  | Pan          | Pans across the map                                       |
  +--------------+-----------------------------------------------------------+
  | Zoom In      | Zooms in on the map                                       |
  +--------------+-----------------------------------------------------------+
  | Zoom Out     | Zooms out on the map                                      |
  +--------------+-----------------------------------------------------------+
  | Full Extent  | Redraws the map at full extent                            |
  +--------------+-----------------------------------------------------------+
  | Find         | Locates a specific item on the map                        |
  +--------------+-----------------------------------------------------------+
  | Query        | Searches for items on the map that meet specific criteria |
  +--------------+-----------------------------------------------------------+
  | Overview Map | Toggles the Overview Map on/off                           |
  +--------------+-----------------------------------------------------------+
  | Legends      | Controls the display of map legends                       |
  +--------------+-----------------------------------------------------------+
  | Toolbars     | Toggles the toolbars on/off                               |
  +--------------+-----------------------------------------------------------+
  | Options      | Sets map appearance options                               |
  +--------------+-----------------------------------------------------------+


**Project Menu**

  +-----------------------------------+-----------------------------------+
  | *Command*                         | *Description*                     |
  +===================================+===================================+
  | Summary                           | Provides a summary description of |
  |                                   | the project's characteristics     |
  +-----------------------------------+-----------------------------------+
  | Defaults                          | Edits a project's default         |
  |                                   | properties                        |
  +-----------------------------------+-----------------------------------+
  | Calibration Data                  | Registers files containing        |
  |                                   | calibration data with the project |
  +-----------------------------------+-----------------------------------+
  | Analysis Options                  | Edits analysis options            |
  +-----------------------------------+-----------------------------------+
  | Run Analysis                      | Runs a simulation                 |
  +-----------------------------------+-----------------------------------+


**Report Menu**

   The Report menu has commands used to report analysis results in
   different formats.

  +-----------------------------------+-----------------------------------+
  | *Command*                         | *Description*                     |
  +===================================+===================================+
  | Status                            | Reports changes in the status of  |
  |                                   | links over time                   |
  +-----------------------------------+-----------------------------------+
  | Energy                            | Reports the energy consumed by    |
  |                                   | each pump                         |
  +-----------------------------------+-----------------------------------+
  | Calibration                       | Reports differences between       |
  |                                   | simulated and measured values     |
  +-----------------------------------+-----------------------------------+
  | Reaction                          | Reports average reaction rates    |
  |                                   | throughout the network            |
  +-----------------------------------+-----------------------------------+
  | Full                              | Creates a full report of computed |
  |                                   | results for all nodes and links   |
  |                                   | in all time periods which is      |
  |                                   | saved to a plain text file        |
  +-----------------------------------+-----------------------------------+
  | Graph                             | Creates time series, profile,     |
  |                                   | frequency, and contour plots of   |
  |                                   | selected parameters               |
  +-----------------------------------+-----------------------------------+
  | Table                             | Creates a tabular display of      |
  |                                   | selected node and link quantities |
  +-----------------------------------+-----------------------------------+
  | Options                           | Controls the display style of a   |
  |                                   | report, graph, or table           |
  +-----------------------------------+-----------------------------------+


**Window Menu**

   The Window Menu contains the following commands:

  +-------------+-------------------------------------------------------------+
  | *Command*   | *Description*                                               |
  +=============+=============================================================+
  | Arrange     | Rearranges all child windows to fit within the main window  |
  +-------------+-------------------------------------------------------------+
  | Close All   | Closes all open windows (except the Map and Browser)        |
  +-------------+-------------------------------------------------------------+
  | Window List | Lists all open windows; selected window currently has focus |
  +-------------+-------------------------------------------------------------+



**Help Menu**

   The Help Menu contains commands for getting help in using EPANET:

  +-------------+----------------------------------------------------------+
  | *Command*   | *Description*                                            |
  +=============+==========================================================+
  | Help Topics | Displays the Help system's Help Topics dialog box        |
  +-------------+----------------------------------------------------------+
  | Units       | Lists the units of measurement for all EPANET parameters |
  +-------------+----------------------------------------------------------+
  | Tutorial    | Presents a short tutorial introducing the user to EPANET |
  +-------------+----------------------------------------------------------+
  | About       | Lists information about the version of EPANET being used |
  +-------------+----------------------------------------------------------+


   Context-sensitive Help is also available by pressing the F1 key.


Toolbars
~~~~~~~~

   Toolbars provide shortcuts to commonly used operations. There are two
   such toolbars:

    -  Standard Toolbar

    -  Map Toolbar



   The toolbars can be docked underneath the Main Menu bar or dragged to
   any location on the EPANET workspace. When undocked, they can also be
   re-sized. The toolbars can be made visible or invisible by selecting
   **View >> Toolbars**.


**Standard Toolbar**

   The Standard Toolbar contains speed buttons for commonly used
   commands.

   |image40| Opens a new project (**File >> New**)

   |image41| Opens an existing project (**File >> Open**)

   |image42| Saves the current project (**File >> Save**)

   |image43| Prints the currently active window (**File >> Print**)

   |image45| Copies selection to the clipboard or to a file (**Edit >> Copy To**)

   |image46| Deletes the currently selected item

   |image44| Finds a specific item on the map (**View >> Find**)

   |image48| Runs a simulation (**Project >> Run Analysis**)

   |image47| Runs a visual query on the map (**View >> Query**)

   |image49| Creates a new graph view of results (**Report >> Graph**)

   |image50| Creates a new table view of results (**Report >> Table**)

   |image51| Modifies options for the currently active view (**View >>
   Options** or **Report >> Options**)


**Map Toolbar**

   The Map Toolbar contains buttons for working with the Network Map.

   |image52| Selects an object on the map (**Edit >> Select Object**)

   |image53| Selects link vertex points (**Edit >> Select Vertex**)

   |image54| Selects a region on the map (**Edit >> Select Region**)

   |image55| Pans across the map (**View >> Pan**)

   |image56| Zooms in on the map (**View >> Zoom In**)

   |image57| Zooms out on the map (**View >> Zoom Out**)

   |image58| Draws map at full extent (**View >> Full Extent**)

   |image59| Adds a junction to the map

   |image60| Adds a reservoir to the map

   |image61| Adds a tank to the map

   |image62| Adds a pipe to the map

   |image63| Adds a pump to the map

   |image64| Adds a valve to the map

   |image65| Adds a label to the map



Status Bar
~~~~~~~~~~

   The Status Bar appears at the bottom of the EPANET workspace and is
   divided into four sections which display the following information:

   - **Auto-Length** – indicates whether automatic computation of pipe
     lengths is turned on or off

   - **Flow Units** - displays the current flow units that are in effect

   - **Zoom Level** - displays the current zoom in level for the map (100%
     is full scale)

   - **Run Status** - a faucet icon shows:

      - no running water if no analysis results are available,

      - running water when valid analysis results are available,

      - a broken faucet when analysis results are available but may be
        invalid because the network data have been modified.

   - **XY Location** - displays the map coordinates of the current
     position of the mouse pointer.


Network Map
~~~~~~~~~~~

   The Network Map provides a planar schematic diagram of the objects
   comprising a water distribution network. The location of objects and
   the distances between them do not necessarily have to conform to
   their actual physical scale. Selected properties of these objects,
   such as water quality at nodes or flow velocity in links, can be
   displayed by using different colors. The color-coding is described in
   a Legend, which can be edited. New objects can be directly added to
   the map and existing objects can be clicked on for editing, deleting,
   and repositioning. A backdrop drawing (such as a street or
   topographic map) can be placed behind the network map for reference.
   The map can be zoomed to any scale and panned from one position to
   another. Nodes and links can be drawn at different sizes, flow
   direction arrows added, and object symbols, ID labels and numerical
   property values displayed. The map can be printed, copied onto the
   Windows clipboard, or exported as a DXF file or Windows metafile.


Data Browser
~~~~~~~~~~~~

   The Data Browser (shown below) is accessed from the Data
   tab on the Browser window. It gives access to the various objects, by
   category (Junctions, Pipes, etc.) that are contained in the network
   being analyzed. The buttons at the bottom are used to add, delete,
   and edit these objects.

   |image66| 

   .. image:: media/image53.jpeg
      :align: left

   
   
      Selects an object category
   
      
   
   
      Lists items in the selected category



      Add, Delete, and Edit buttons
  

Map Browser
~~~~~~~~~~~

   The Map Browser (shown below) is accessed from the Map tab
   of the Browser Window. It selects the parameters and time period that
   are viewed in color-coded fashion on the Network Map. It also
   contains controls for animating the map through time.

   |image67| 
 
   The animation control pushbuttons on the Map Browser work as follows:

   |image68|   \ Rewind (return to initial time)

   |image68_2| \ Animate back through time
   
   |image68_3| \ Stop the animation
   
   |image68_4| \ Animate forward in time


Property Editor
~~~~~~~~~~~~~~~

   The Property Editor (shown at the left) is used to edit
   the properties of network nodes, links, labels, and analysis options.
   It is invoked when one of these objects is selected (either on the
   Network Map or in the Data Browser) and double-clicked or the
   Browser's Edit button is clicked. The following points help explain
   how to use the Editor.

    -  The Editor is a grid with two columns - one for the property's name
       and the other for its value.

    -  The columns can be re-sized by re-sizing the header at the top of the
       Editor with the mouse.

    -  The Editor window can be moved and re-sized via the normal Windows
       procedures.

    -  An asterisk next to a property name means that it is a required
       property -- its value cannot be left blank.

    -  Depending on the property, the value field can be one of the
       following:

      -  a text box where you type in a value

      -  a dropdown list box where you select from a list of choices

      -  an ellipsis button which you click to bring up a specialized editor

      -  a read-only label used to display computed results

    -  The property in the Editor that currently has focus will be
       highlighted with a white background.

    -  You can use both the mouse and the Up and Down arrow keys on the
       keyboard to move between properties.

    -  To begin editing the property with the focus, either begin typing
       a value or hit the Enter key.

    -  To have EPANET accept what you have entered, press the Enter key
       or move to another property; to cancel, press the Esc key.

    -  Clicking the Close button in the upper right corner of its title
       bar will hide the Editor.

      |image69|


Program Preferences
~~~~~~~~~~~~~~~~~~~~

   Program preferences allow you to customize certain program features.
   To set program preferences select **Preferences** from the **File**
   menu. A Preferences dialog form will appear containing two tabbed
   pages – one for General Preferences and one for Format Preferences.


**General Preferences**

   The following preferences can be set on the General page of the
   Preferences dialog:

  +-----------------------------------+-----------------------------------+
  | *Preference*                      | *Description*                     |
  +===================================+===================================+
  | Bold Fonts                        | Check to use bold fonts in all    |
  |                                   | newly created windows             |
  +-----------------------------------+-----------------------------------+
  | Blinking Map Hiliter              | Check to make the selected node,  |
  |                                   | link, or label on the map blink   |
  |                                   | on and off                        |
  +-----------------------------------+-----------------------------------+
  | Flyover Map Labeling              | Check to display the ID label and |
  |                                   | current parameter value in a      |
  |                                   | hint-style box whenever the mouse |
  |                                   | is placed over a node or link on  |
  |                                   | the network map                   |
  +-----------------------------------+-----------------------------------+
  | Confirm Deletions                 | Check to display a confirmation   |
  |                                   | dialog box before deleting any    |
  |                                   | object                            |
  +-----------------------------------+-----------------------------------+
  | Automatic Backup File             | Check to save a backup copy of a  |
  |                                   | newly opened project to disk      |
  |                                   | named with a .bak extension       |
  +-----------------------------------+-----------------------------------+
  | Temporary Directory               | Name of the directory (folder)    |
  |                                   | where EPANET writes its temporary |
  |                                   | files                             |
  +-----------------------------------+-----------------------------------+


     **Note**: The Temporary Directory must be a file directory (folder)
     where the user has write privileges and must have sufficient space to
     store files which can easily grow to several tens of megabytes for
     larger networks and simulation runs. The original default is the
     Windows TEMP directory (usually c:\Windows\Temp).

      |image70|


**Formatting Preferences**

   The Formats page of the Preferences dialog box controls how many
   decimal places are displayed when results for computed parameters are
   reported. Use the dropdown list boxes to select a specific Node or
   Link parameter. Use the spin edit boxes to select the number of
   decimal places to use when displaying computed results for the
   parameter. The number of decimal places displayed for any particular
   input design parameter, such as pipe diameter, length, etc. is
   whatever the user enters.

      |image71|




.. include:: image_subdefs.rst
