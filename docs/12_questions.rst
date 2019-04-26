.. raw:: latex

    \clearpage
    

    
12. FREQUENTLY ASKED QUESTIONS
==============================

FAQs
~~~~

**How can I import a pipe network created with a CAD or GIS program?**

  See Section 11.4.

**How do I model a groundwater pumping well?**

  Represent the well as a reservoir whose head equals the piezometric
  head of the groundwater aquifer. Then connect your pump from the
  reservoir to the rest of the network. You can add piping ahead of the
  pump to represent local losses around the pump.

  If you know the rate at which the well is pumping then an alternate
  approach is to replace the well – pump combination with a junction
  assigned a negative demand equal to the pumping rate. A time pattern
  can also be assigned to the demand if the pumping rate varies over
  time.

**How do I size a pump to meet a specific flow?**

  Set the status of the pump to CLOSED. At the suction (inlet) node of
  the pump add a demand equal to the required pump flow and place a
  negative demand of the same magnitude at the discharge node. After
  analyzing the network, the difference in heads between the two nodes
  is what the pump needs to deliver.

**How do I size a pump to meet a specific head?**

  Replace the pump with a Pressure Breaker Valve oriented in the
  opposite direction. Convert the design head to an equivalent pressure
  and use this as the setting for the valve. After running the analysis
  the flow through the valve becomes the pump’s design flow.

**How can I enforce a specific schedule of source flows into the
network from my reservoirs?**

  Replace the reservoirs with junctions that have negative demands
  equal to the schedule of source flows. (Make sure there is at least
  one tank or remaining reservoir in the network, otherwise EPANET will
  issue an error message.)

**How can I analyze fire flow conditions for a particular junction
node?**

  To determine the maximum pressure available at a node when the flow
  demanded must be increased to suppress a fire, add the fire flow to
  the node’s normal demand, run the analysis, and note the resulting
  pressure at the node.

  To determine the maximum flow available at a particular pressure, set
  the emitter coefficient at the node to a large value (e.g., 100 times
  the maximum expected flow) and add the required pressure head (2.3
  times the pressure in psi) to the node's elevation. After running the
  analysis, the available fire flow equals the actual demand reported
  for the node minus any consumer demand that was assigned to it.

**How do I model a reduced pressure backflow prevention valve?**

  Use a General Purpose Valve with a headloss curve that shows
  increasing head loss with decreasing flow. Information from the valve
  manufacturer should provide help in constructing the curve. Place a
  check valve (i.e., a short length of pipe whose status is set to CV)
  in series with the valve to restrict the direction of flow.

**How do I model a pressurized pneumatic tank?**

  If the pressure variation in the tank is negligible, use a very
  short, very wide cylindrical tank whose elevation is set close to the
  pressure head rating of the tank. Select the tank dimensions so that
  changes in volume produce only very small changes in water surface
  elevation.

  If the pressure head developed in the tank ranges between H1 and H2,
  with corresponding volumes V1 and V2, then use a cylindrical tank
  whose cross-sectional area equals (V2-V1)/(H2-H1).

**How do I model a tank inlet that discharges above the water surface?**

  |image146| 
  
  Use the configuration shown below:

  The tank's inlet consists of a Pressure Sustaining Valve followed by
  a short length of large diameter pipe. The pressure setting of the
  PSV should be 0, and the elevation of its end nodes should equal the
  elevation at which the true pipe connects to the tank. Use a Check
  Valve on the tank's outlet line to prevent reverse flow through it.

**How do I determine initial conditions for a water quality analysis?**

  If simulating existing conditions monitored as part of a calibration
  study, assign measured values to the nodes where measurements were
  made and interpolate (by eye) to assign values to other locations. It
  is highly recommended that storage tanks and source locations be
  included in the set of locations where measurements are made.

  To simulate future conditions start with arbitrary initial values
  (except at the tanks) and run the analysis for a number of repeating
  demand pattern cycles so that the

  water quality results begin to repeat in a periodic fashion as well.
  The number of such cycles can be reduced if good initial estimates
  are made for the water quality in the tanks. For example, if modeling
  water age the initial value could be set to the tank's average
  residence time, which is approximately equal to the fraction of its
  volume it exchanges each day.

**How do I estimate values of the bulk and wall reaction coefficients?**

  Bulk reaction coefficients can be estimated by performing a bottle
  test in the laboratory (see Bulk Reactions in Section 3.4). Wall
  reaction rates cannot be measured directly. They must be back-fitted
  against calibration data collected from field studies (e.g., using
  trial and error to determine coefficient values that produce
  simulation results that best match field observations). Plastic pipe
  and relatively new lined iron pipe are not expected to exert any
  significant wall demand for disinfectants such as chlorine and
  chloramines.

**How can I model a chlorine booster station?**

  Place the booster station at a junction node with zero or positive
  demand or at a tank. Select the node into the Property Editor and
  click the ellipsis button in the Source Quality field to launch the
  Source Quality Editor. In the editor, set Source Type to SETPOINT
  BOOSTER and set Source Quality to the chlorine concentration that
  water leaving the node will be boosted to. Alternatively, if the
  booster station will use flow-paced addition of chlorine then set
  Source Type to FLOW PACED BOOSTER and Source Quality to the
  concentration that will be added to the concentration leaving the
  node. Specify a time pattern ID in the Time Pattern field if you wish
  to vary the boosting level with time.

**How would I model THM growth in a network?**

  THM growth can be modeled using first-order saturation kinetics.
  Select Options – Reactions from the Data Browser. Set the bulk
  reaction order to 1 and the limiting concentration to the maximum THM
  level that the water can produce, given a long enough holding time.
  Set the bulk reaction coefficient to a positive number reflective of
  the rate of THM production (e.g., 0.7 divided by the THM doubling
  time). Estimates of the reaction coefficient and the limiting
  concentration can be obtained from laboratory testing. The reaction
  coefficient will increase with increasing water temperature. Initial
  concentrations at all network nodes should at least equal the THM
  concentration entering the network from its source node.

**Can I use a text editor to edit network properties while running
EPANET?**

  Save the network to file as ASCII text (select **File >> Export >>
  Network**). With EPANET still running, start up your text editor
  program. Load the saved network file into the editor. When you are
  done editing the file, save it to disk. Switch to EPANET and read in
  the file (select **File >> Open**). You can keep switching back and
  forth between the editor program and EPANET, as more changes are
  needed. Just remember to save the file after modifying it in the
  editor, and re-open it again

  after switching to EPANET. If you use a word processor (such as
  WordPad) or a spreadsheet as your editor, remember to save the file
  as plain ASCII text.

**Can I run multiple EPANET sessions at the same time?**

  Yes. This could prove useful in making side-by-side comparisons of
  two or more different design or operating scenarios.

  
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

