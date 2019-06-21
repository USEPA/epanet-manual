

  Now consider the case where the demand at a node :math:`i`, :math:`d_{i}`,
  depends on the pressure head :math:`p_{i}` available at the node (where
  pressure head is hydraulic head :math:`h_{i}` minus elevation :math:`E_{i}`).
  There are several different forms of pressure dependency that have been
  proposed. Here we use Wagner’s equation:

  .. math::
     :label: eq:wagners

     d_{i} =
       \left\{
         \begin{array}{l l}
           D_{i}                                                           & p_{i} \ge P_{f}     \\
           D_{i} \left( \frac{p_{i} - P_{0}}{P_{f} - P_{0}} \right) ^{1/e} & P_{0} < p_i < P_{f} \\
           0                                                               & p_{i} \le P_{0}
         \end{array}
       \right.

  :math:`D_{i}` is the full normal demand at node :math:`i` when the pressure
  :math:`p_{i}` equals or exceeds :math:`P_{f}`, :math:`P_{0}` is the pressure
  below which the demand is 0, and :math:`e` is an exponent usually set equal
  to 2 (to mimic flow through an orifice).

  Eq. :eq:`eq:wagners` can be inverted to express head loss through a virtual
  link as a function of the demand flowing out of node :math:`i` to a virtual
  reservoir with fixed pressure head :math:`P_{0} + E_{i}`:

  .. math::
     :label: eq:inv_wagner

     h_{i} - P_{0} - E_{i} = R_{di} d_{i}^{e}

  where :math:`E_{i}` is the node’s elevation and
  :math:`R_{di} = (P_{f} - P_{0})/D_{i}^{e}` is the link’s resistance
  coefficient. This expression can be folded into the GGA matrix equations,
  where the pressure dependent demands :math:`d_{i}` are treated as the
  unknown flows in the virtual links that honor constraints in Eq.
  :eq:`eq:wagners`.

  The head loss :math:`h_{d}` and its gradient :math:`g_{d}` through the
  virtual link can be evaluated as follows (with node subscripts
  suppressed for clarity):

  1. If the current demand flow :math:`d` is greater than the full Demand
     :math:`D`:

     .. math::
        \begin{gathered}
          h_{d} = R_{d} D^{e} + R_{\text{HIGH}}(d - D) \\
          g_{d} = R_{\text{HIGH}}
        \end{gathered}

     where :math:`R_{\text{HIGH}}` is a large resistance factor
     (e.g. 10\ :sup:`9`).

  2. Otherwise Eq. :eq:`eq:inv_wagner` is used to evaluate the head loss and
     gradient:

     .. math::
        \begin{gathered}
          g_{d} = e R_{d} \left| d \right|^{e - 1} \\
          h_{d} = g_{d} d / e
        \end{gathered}

     and a one-sided barrier function :math:`h_{b}(d)` and its derivative
     :math:`g_{b}(d)` is added onto :math:`h_{d}` and :math:`g_{d}`,
     respectively, to prevent :math:`d` from going negative.

  The aforementioned barrier function has the form:

  .. math::
     \begin{gathered}
       h_{b} = \ \left( a - \sqrt{a^{2} + \epsilon^{2}} \right)/2 \\
       g_{b} = \left( R_{\text{HIGH}}/2 \right)\left( 1 - a/\sqrt{a^{2} + \epsilon^{2}} \right)
     \end{gathered}

  where :math:`a = R_{\text{HIGH}}d` and :math:`\epsilon` is a small
  tolerance (e.g., 10\ :sup:`-3`).

  .. Examples of these functions are graphed in Figure 1.

  These head loss and gradient values are then incorporated into the normal
  set of GGA matrix equations as follows:

  1. For the diagonal entry of :math:`A` corresponding to node *i*:

     .. math::
        A_{ii} = A_{ii} + 1/g_{di}

  2. For the entry of :math:`F` corresponding to node :math:`i`:

     .. math::
        F_{i} = F_{i} + D_{i} - d_{i} + \left( h_{di} + E_{i} + P_{0} \right) / g_{di}


  Note that :math:`D_{i}` is added to :math:`F_{i}` to cancel out having
  subtracted it from the original :math:`F_{i}` value appearing in Eq.
  :eq:`eq:matrix_rhs`.

..
  ======== ========
  |image0| |image1|
  ======== ========

  **Figure 1. One-Sided Barrier Function and its Derivative (for**
  :math:`\mathbf{R}_{\mathbf{\text{HIGH}}}\mathbf{=}\mathbf{10}^{\mathbf{6}}`\ **).**

  After a new set of nodal heads is found, the demands at node *i* are
  updated using Eq. (9) which takes the form:

  .. math::
     d_{i} = d_{i} - \left( h_{\text{di}} - h_{i} + E_{i} + P_{0} \right)/g_{\text{di}}
**EPANET Implementation**

A special research version of EPANET 2.0 was written that incorporates
pressure dependent demands using the method just described. To keep
modifications to a minimum, the following restrictions were imposed:

1. A global set of minimum and full (or nominal) pressure limits apply
   to all nodes.

2. A hard-wired global demand function exponent *e* of 2 applies to all
   nodes.

3. In extended period analysis, where the full demands change at
   different time periods, the same pressure-dependent demand function
   is applied to the current full demand (instead of changing *P\ f* to
   accommodate changes in *D\ f*).

Two new entries were added to the [OPTIONS] section of the EPANET input
file (and to the Hydraulic Options editor of the graphical user
interface):

Minimum Pressure is the minimum pressure :math:`(P_{0})` needed to have
any demand realized.

   Nominal Pressure is the pressure :math:`{(P}_{f})` above which the
   full demand is realized.

The Nominal Pressure must be greater than zero (the default value) for a
pressure dependent analysis to be made (otherwise a traditional fixed
demand analysis will be made). The units for both of these input
pressures are either PSI for US units or Meters for metric units. At the
start of each new hydraulic time period the demands are set equal to
their full value. The demand reported as output by both the GUI and the
EPANET toolkit is the pressure-adjusted demand, not the nominal (or
full) demand.

A more extensive update to EPANET would allow one to override the
pressure limits and exponent at each node (or for each demand category
at each node) and would add each node’s full demand (or demand deficit)
to the list of reportable output variables.

**Validation Examples**

Example 1 is a simple linear arrangement of pipes fed by a single
reservoir as shown in Figure 2. It was first proposed by Gupta and Bhave
(1996) and used in many PDD evaluations since then.

Table 1 compares the pressure dependent demands found for this network
by the PDD-modified EPANET and an earlier study by Cheung et al. (2005).
These results are for a Reservoir head of 100 m, *P\ 0* of 0 m, and
*P\ f* of 20 m. Note that the results are all pressure-limited and are
essentially identical between the two methods.

|Example1.png|

**Figure 2. Linear Pipe Network Used in Example 1.**

**Table 1. Comparison of PDD Solutions for Example 1.**

==== ====================================== ===================================
Node Demand – Cheung et al. (m:sup:`3`/min) Demand – EPANET PDD (m:sup:`3`/min)
==== ====================================== ===================================
2    1.28                                   1.29
3    1.28                                   1.28
4    1.26                                   1.26
5    2.42                                   2.42
==== ====================================== ===================================

Example 2 solves the same network as Example 1 using what is known as
Pressure Deficient Network Analysis (PDNA). PDNA does not use a specific
demand v. pressure function. Instead it asks which nodes must have their
full demands reduced and by how much so that no pressures below
:math:`P_{0}` will exist. Todini (2003) and Ang and Jowitt (2006) have
described procedures, based on making multiple runs of EPANET, for
solving a PDNA. We show that it can also be accomplished using a PDD
analysis where :math:`P_{f}` is chosen to be very close to
:math:`P_{0}`.

Table 2 displays the results of running a PDNA on Example 1’s network as
the reservoir head is increased from 85 m up to 109.86 m. The solutions
found by Ang and Jowitt (2006) are compared with those of EPANET-PDD
using a :math:`P_{0}` of 0 and a :math:`P_{f}` of 0.001 m. The two sets
of solutions are seen to be virtually identical.

**Table 2. Demands (in m\ 3/min) found for Example 2 (A: Ang and Jowitt;
B: EPANET-PDD).**

=============== ====== ====== ====== ====== ==== ==== ==== ====
Source Head (m) Node 2 Node 3 Node 4 Node 5
=============== ====== ====== ====== ====== ==== ==== ==== ====
\               A      B      A      B      A    B    A    B
85.00           0.00   0.00   0.00   0.00   0.00 0.00 0.00 0.00
90.98           0.00   0.00   2.00   2.00   0.00 0.00 2.73 2.74
91.97           2.00   2.00   2.00   2.00   0.00 0.00 2.75 2.75
98.78           2.00   2.00   2.00   2.00   0.00 0.01 4.00 4.00
109.86          2.00   2.00   2.00   2.00   3.00 3.00 4.00 4.00
=============== ====== ====== ====== ====== ==== ==== ==== ====

Example 3 is another PDNA also taken from Ang and Jowitt (2006) where
:math:`P_{0}` is 0. Figure 3a shows the pressures obtained after a fixed
demand analysis where R1 has elevation of 100 m, R2 has elevation of 105
m, nodes 1-8 have full demands of 25 LPS and node 9 has a full demand of
75 LPS. Six out of nine junctions can only meet their demands under
negative pressures. Figure 3b shows the results of running a PDNA, with
both the multi-pass method described by Todini (2003) and by using
EPANET-PDD with :math:`P_{f} = 0.001` (both methods produce the same
result). Only one of the original six negative pressure nodes (9) must
have its demand reduced to avoid any negative pressures. In terms of
computational effort, the fixed demand analysis required 4 iterations of
EPANET to converge; the EPANET-PDD method required 6 iterations and the
multi-pass Todini method required four separate runs of EPANET with a
total of 20 iterations.

|image3|\ |image4|

**Figure 3. Results for: A- Fixed Demand Analysis; B- Pressure Deficient
Analysis**

**Performance on Larger Networks**

EPANET-PDD was tested on several larger networks to determine how
efficient it was for both typical pressure dependent analysis and for
pressure deficient analysis. The results are presented in Table 3 for
four networks ranging in size from 22 to 1891 demand nodes. The Net3
system is one of the examples distributed with EPANET 2 while the other
networks were downloaded from the University of Exeter’s Centre for
Water Systems Benchmarks web site. Each network was solved for a single
time period, first for fixed demands (the DDA solution) and then under
pressure dependent demands (the PDA solution). The PDA runs were made
under different sets of pressure limits, including one that provides for
a Pressure Deficient Network Analysis. For the DDA runs, the number of
nodes that could not meet the lower pressure limit used in the PDA was
noted. The last two columns in the table compare the number of GGA
iterations needed to reach convergence. They show that a PDA takes more
iterations to converge than does a conventional DDA run. Also, in most
cases a pressure deficient analysis, where the pressure limits are very
close to one another, requires more iterations than a pressure dependent
one where the limits are more widely spaced.

**Table 3. Efficiency of EPANET-PDD for different size networks.**

======= ============== ================ ================ ========================== ==================== ===
Network # Demand Nodes Minimum Pressure Nominal Pressure # Pressure Deficient Nodes Number of Iterations
======= ============== ================ ================ ========================== ==================== ===
\                                                                                   DDA                  PDA
AnyTown 22             20 psi           60 psi           10                         7                    8
\                      20 psi           20.01 psi                                   7                    13
Hanoi   31             10 m             40 m             20                         3                    5
\                      10 m             20 m                                        3                    7
\                      10 m             10.01 m                                     3                    7
Net3    92             40 psi           60 psi           5                          5                    5
\                      40 psi           40.01 psi                                   5                    12
Exnet   1891           0 m              20 m             141                        6                    5
\                      20 m             40 m             1148                       6                    6
\                      20 m             20.01 m                                     6                    52
======= ============== ================ ================ ========================== ==================== ===

**References**

ANG, W.K. & JOWITT, P.W. 2006. Solution for Water Distribution Systems
under Pressure-Deficient Conditions. *Journal of Water Resources
Planning and Management - ASCE*, 132(3) pp175-182.

CHEUNG, P.B., VAN ZYL, J.E. & REIS, L.F.R. 2005. Extension of EPANET for
Pressure Driven Demand Modeling in Water Distribution System. In: SAVIĆ,
D.A., WALTERS, G.A., KING, R. & KHU, S.T. (eds.) *Proceedings of the
Eighth International Conference on Computing and Control for the Water
Industry* (CCWI2005). University of Exeter, UK. Vol 1, pp311-316.
http://www.thematrix.it/irrigationit/epanet/artc_1147708476_40.pdf

GUPTA, R. & BHAVE, P.R. 1996. Comparison of Methods for Predicting
Deficient-Network Performance. *Journal of Water Resources Planning and
Management - ASCE*, 122(3), pp214-217.

TODINI, E. 2003. A More Realistic Approach to the Extended Period
Simulation of Water Distribution Networks. In: Maksimovic, C. , Butler,
D., and Memon, F.A. (eds) *Advances in Water Supply Management,
Proceedings of the CCWI '03 Conference,* Swets and Leitlinger, Lisse.

.. |image0| image:: media/image1.png
   :width: 3.25347in
   :height: 2.69375in
.. |image1| image:: media/image2.png
   :width: 3.34722in
   :height: 2.69375in
.. |Example1.png| image:: media/image3.png
   :width: 6.5in
   :height: 2.34375in
.. |image3| image:: media/image4.png
   :width: 4.97917in
   :height: 3.97917in
.. |image4| image:: media/image5.png
   :width: 4.97917in
   :height: 3.97917in
