# Plant Structure and Water Relations

\label{sec:unit_VIII_plant_structure_and_water}


<!-- chapter-metadata-badge -->
> Level 2/3 · 55 min read · 75 min lecture · Prerequisites: \cref{sec:unit_II_membrane_transport}

## Learning Objectives

1. Describe the major organ systems of [**angiosperm**](#gl:angiosperm)s: root system (taproot vs fibrous), shoot system, and leaf.
2. Compare the three plant tissue systems: dermal, ground, and vascular, including cell types within each.
3. Explain water relations in plants using the four-component water potential equation $\Psi = \Psi_s + \Psi_p + \Psi_m + \Psi_g$.
4. Describe [**transpiration**](#gl:transpiration) and the cohesion-tension \citep{dixon1894}-adhesion (TACT) mechanism of water ascent and critically evaluate its supporting evidence.
5. Explain the apoplast vs symplast pathways and the role of the Casparian strip and suberin lamella.
6. Explain phloem transport and the Münch pressure-flow hypothesis \citep{munch1930}, including apoplastic vs symplastic loading.
7. Describe stomatal regulation and the role of ABA in drought response at the molecular level.
8. Explain nutrient uptake strategies including mycorrhizal associations and quantitative turgor relations.
9. Quantify water-use efficiency at the leaf level and connect it to C3, C4, and CAM photosynthetic trade-offs.

<!-- curriculum-scaffold-start -->
### Study Blueprint

- **Big idea:** Plant form is an engineering solution to water movement, support, gas exchange, and growth.
- **Core concepts:** xylem, phloem, water potential, transpiration.
- **Framework alignment:** Vision & Change: Structure and function, Pathways and transformations of energy and matter, Systems; AP Biology: Energetics, Systems Interactions; NGSS-style topics: Structure and Function, Matter and Energy in Organisms and Ecosystems.
- **Model or quantitative lens:** Water-potential and transpiration-flux calculations.
- **Data skill:** Interpret plant-water data from pressure, solute, and humidity measurements.
- **Practice cadence:** Visual Representations, Questions and Methods, Argumentation.
- **Common misconception to repair:** Water does not move because plants pull with intention; it follows potential gradients and cohesion.
- **Primary lab:** \nameref{sec:lab_unit_VIII_plant_structure_and_water}.
- **Question bank:** \nameref{sec:q_unit_VIII_plant_structure_and_water}.
- **Transfer task:** Transfer plant-water reasoning to drought, irrigation, forest physiology, and crop breeding.
- **Bridge to computation:** `biology.botany.botany.water_potential`.
<!-- curriculum-scaffold-end -->

\begin{figure}[htbp]
\centering
\includegraphics[width=0.85\textwidth]{../figures/water_potential_transpiration.png}
\caption{Illustrative model calculations of plant water relations, not observations. Left: solute potential ($\psi_s=-CRT$, $i=1$, $T=298$ K) becomes more negative over 0.05–0.60 mol L$^{-1}$; fixed turgor of 0.5 MPa raises total potential. Right: $E=g(w_i-w_o)$ with fixed internal vapor mole fraction $w_i=0.013$ mol/mol and external values 0.0075–0.0125 mol/mol. Conductances $g=0.10$, 0.20 and 0.35 mol m$^{-2}$ s$^{-1}$ yield flux in mmol m$^{-2}$ s$^{-1}$; higher conductance increases flux at the same vapor gradient.}
\label{fig:unit_VIII_water_potential_transpiration}
\end{figure}
<!-- alt: Two illustrative model panels, not measured data. Left, solute potential at 298 K and i=1 declines over 0.05–0.60 mol per liter and total potential is shifted upward by fixed 0.5 MPa turgor. Right, distinct line styles compare conductances 0.10, 0.20 and 0.35 mol m^-2 s^-1 at fixed internal vapor mole fraction 0.013 mol/mol; flux in mmol m^-2 s^-1 declines as external vapor mole fraction rises from 0.0075 to 0.0125 mol/mol. -->

---

> **Opening Vignette — How a Giant Sequoia Pulls Water 100 Meters Up**
>
> A mature coast redwood (*Sequoia sempervirens*) can stand 115 meters tall. Getting water from soil to the topmost leaves requires lifting it against a gravitational pull of roughly 1.1 MPa — while simultaneously overcoming resistance to flow through millions of microscopic [**xylem**](#gl:xylem) conduits. How? The answer, worked out by Henry Dixon and John Joly in 1894 \citep{dixon1894} and validated with pressure-bomb measurements in the 1960s, is cohesion-tension: water molecules cohere to each other and adhere to xylem walls so strongly that evaporation from leaf [**stomata**](#gl:stomata) creates a continuous negative-pressure column (tension) that pulls water up from the roots. The column can sustain tensions as low as −10 MPa before xylem embolism shatters it. The bulk-flow ascent itself is passive — the xylem column requires no direct metabolic energy — though it is gated by active stomatal regulation; this mechanism moves trillions of liters of water into Earth's atmosphere annually, so elegantly that engineers studying microfluidics still struggle to replicate it artificially.

## The Plant Body Plan

Flowering plants (angiosperms, ~300,000 species) are organized into two major organ systems that work together to acquire resources from both soil and atmosphere.

### Root System Architecture and Soil Exploration

The root system anchors the plant, absorbs water and minerals, and stores nutrients. Two major architectural types exist:

- **Taproot system:** A single [**dominant**](#gl:dominant) primary root (derived from the embryonic radicle) with smaller lateral roots branching off. Common in eudicots (e.g., carrots, dandelions, oaks). Deep taproot systems can access water tables several meters below the surface.
- **Fibrous root system:** A dense mat of similarly sized adventitious roots arising from the stem base. The primary root is short-lived. Common in monocots (e.g., grasses, wheat, rice). Excellent for soil stabilization and surface nutrient capture.

**Root apical meristem (RAM):** Located near the root tip, protected by the root cap. The RAM contains slowly dividing cells in the quiescent center (QC) surrounded by rapidly dividing initial cells that produce most root tissues. The root tip is organized into distinct zones:

1. **Root cap** -- protects the meristem; secretes mucilage for lubrication; columella cells contain starch-filled amyloplasts (statoliths) for gravity sensing
2. **Meristematic zone** -- active cell division
3. **Elongation zone** -- cells expand primarily in length (up to 10-fold); driven by [**turgor pressure**](#gl:turgor-pressure) and cell wall loosening
4. **Maturation zone** -- cells differentiate into specialized types; root hairs develop here

**Root hairs** are single elongated epidermal cells that dramatically amplify surface area (~600 cm$^2$ per cm of root length). Mineral ions are absorbed actively against their electrochemical gradients by specific transporters (NO$_3^-$ by NRT1/NRT2; K$^+$ by HKT; Fe$^{2+}$ by IRT1).

### Plant Architecture: Phytomers and Plastochrons

The shoot is built as a series of repeating modular units called **phytomers**. Each phytomer comprises one node, the internode immediately below it, the leaf attached at the node, and the axillary bud subtending the leaf. Phytomer iteration generates the entire shoot — a tree is, formally, a clonal colony of phytomers expressed by a single genotype.

The temporal scaffolding is provided by the **plastochron index (PI)**, defined as the time interval between successive leaf-primordium initiations at the SAM (Erickson and Michelini, 1957). At constant temperature the plastochron is approximately constant for a given genotype (~24 h in *Arabidopsis*, ~36 h in maize), permitting developmental time to be expressed in plastochron units rather than chronological time. The **leaf plastochron index (LPI)** ranks leaves by developmental age — LPI 0 is the youngest visible leaf, LPI 1 the next, and so on — and is the standard developmental clock for maize and tobacco physiology experiments.

**Meristematic zones at the SAM** are organized radially and clonally:

- **L1 (tunica outer layer):** Strictly anticlinal divisions; gives rise to epidermis
- **L2 (tunica inner layer):** Mostly anticlinal; produces mesophyll, gametes
- **L3 (corpus):** Anticlinal and periclinal divisions; produces vascular and ground tissue

Genetic chimeras (e.g., variegated geraniums) reveal these clonal layers as stable, parallel cell lineages whose interactions specify organ identity.

### Shoot System Architecture and Light Capture

The shoot system comprises the stem and leaves and is responsible for [**photosynthesis**](#gl:photosynthesis), reproduction, and support.

**Shoot apical meristem (SAM):** Maintains a pool of pluripotent stem cells at the shoot tip throughout the plant's life. The SAM is organized into:

- **Central zone (CZ):** Slowly dividing stem cells maintained by the WUS-CLV3 negative feedback loop
- **Peripheral zone (PZ):** Faster-dividing cells that form lateral organ primordia (leaves, flowers)
- **Rib zone:** Cells below the CZ that contribute to stem internodes

Leaves are initiated at the PZ where PIN1-mediated auxin maxima form, producing the characteristic phyllotaxis pattern (often 137.5 degrees divergence angle).

### Leaf Anatomy for Gas Exchange and Photosynthesis

Leaf cross-section layers (adaxial to abaxial):

1. Upper epidermis + cuticle (waxy layer of cutin; reduces water loss)
2. Palisade mesophyll (densely packed columnar cells with abundant [**chloroplast**](#gl:chloroplast)s; principal photosynthetic layer)
3. Spongy mesophyll (loosely packed; CO$_2$ diffusion through intercellular air spaces; ~30-40% air space)
4. Lower epidermis + cuticle

**Stomata:** Pores bounded by two kidney-shaped **[guard cell](#gl:guard-cell)s**. Stomatal aperture is controlled by guard cell turgor:

- Light activates blue-light phototropins and red-light photosynthesis in guard cell chloroplasts. K$^+$ influx (via K$^+$ inward-rectifying channels) lowers osmotic potential. Water enters by [**osmosis**](#gl:osmosis). Guard cells swell and bow apart. Stomata open.
- Drought triggers ABA signaling. ABA activates SnRK2 kinases. SLAC1 anion channels open, releasing Cl$^-$. Membrane depolarizes. K$^+$ leaves via GORK channels. Water follows osmotically. Guard cells deflate. Stomata close.

Typical stomatal density: ~200 stomata/mm$^2$ in many mesophytes. Each stoma can open or close in minutes. Stomata allow CO$_2$ in and O$_2$ plus water vapor out -- the inevitable tradeoff between photosynthesis and transpiration.

> **Clinical Connection:** Understanding stomatal biology is essential for crop engineering. Overexpression of the SLAC1 [**gene**](#gl:gene) in barley produced plants with more responsive stomata and 40% greater water-use efficiency in field trials, directly relevant to agriculture in drought-prone regions.

**Concept Check 1:** Why are most stomata located on the lower (abaxial) epidermis of leaves rather than the upper surface?

**Concept Check 2:** A botanist counts an average plastochron of 30 hours in a tomato plant. After 15 days, approximately how many leaf primordia will have been initiated by the SAM, assuming temperature is constant?

---

## Plant Tissue Systems

Most plant organs are composed of three tissue systems: dermal, ground, and vascular.

```mermaid
---
config:
  layout: dagre
---
flowchart TB
    subgraph DERM["Dermal tissue system: outer covering"]
        direction LR
        D1["Epidermis and cuticle"]
        D2["Stomata + guard cells<br/>Trichomes; root hairs"]
        D1 ~~~ D2
    end
    subgraph GROUND["Ground tissue system: interior"]
        direction LR
        G1["Parenchyma<br/>Photosynthesis; storage<br/>Thin primary walls"]
        G2["Collenchyma<br/>Flexible support<br/>Unevenly thickened walls"]
        G3["Sclerenchyma<br/>Rigid support; lignified walls<br/>Often dead at maturity"]
        G1 ~~~ G2 ~~~ G3
    end
    subgraph VASC["Vascular tissue system: transport"]
        direction LR
        X["Xylem<br/>Tracheids: long, tapered; pits<br/>Vessel elements: shorter, wider;<br/>perforation plates"]
        P["Phloem<br/>Sieve-tube elements:<br/>no nucleus at maturity<br/>Companion cells: metabolic support"]
        X ~~~ P
    end
    DERM ~~~ GROUND ~~~ VASC
    classDef default fill:#f4f5f6,stroke:#59636e,color:#17212b
```
<!-- alt: Three labeled panels organize plant tissue systems without a wide branching tree. Dermal structures form the outer covering; ground tissue includes parenchyma, collenchyma and sclerenchyma with their wall and support properties; vascular cards distinguish xylem tracheids and vessel elements from phloem sieve-tube elements and companion cells. Panel order does not imply a developmental sequence. -->

*Three plant tissue systems in compact classification panels: dermal structures form the outer covering, ground cell types fill the interior and provide photosynthesis, storage or support, and vascular tissues provide transport. Xylem and phloem cards retain their major conducting and supporting cell types; sclerenchyma has lignified secondary walls. Panel order is organizational, not a developmental or causal sequence.*

### Dermal Tissue System

The dermal tissue system is the outer protective covering of the plant:

- **Epidermis:** A single layer of tightly packed cells covering most surfaces. Secretes the cuticle.
- **Cuticle:** A waxy layer composed of cutin (a polyester of hydroxylated fatty acids) and epicuticular waxes. Minimizes water loss from non-stomatal surfaces. The cuticle can reduce transpiration by 95% compared to an unprotected surface.
- **Trichomes:** Hair-like epidermal appendages. Diverse functions: reduce wind speed at leaf surface (boundary layer), reflect excess light, secrete defensive compounds (glandular trichomes of tomato produce toxic sesquiterpenes), deter [**herbivory**](#gl:herbivory).
- **Root hairs:** Tubular extensions of single epidermal cells in the root maturation zone. Increase absorptive surface area by 2-10-fold.

### Ground Tissue System

Ground tissue fills the space between dermal and vascular tissues. Three cell types:

**Parenchyma cells:** Living at maturity. Thin primary cell walls. Functions include photosynthesis (mesophyll), storage (starch in potato tubers, sugar in sugar beet roots), and wound healing (dedifferentiate to form callus tissue). Parenchyma cells retain the ability to divide, making them critical for regeneration.

**Collenchyma cells:** Living at maturity. Unevenly thickened primary cell walls (thicker at corners). Provide flexible mechanical support to growing organs. Found in petioles and young stems. Celery "strings" are collenchyma strands.

**Sclerenchyma cells:** Typically dead at maturity. Thick, lignified secondary cell walls. Provide rigid support. Two types: fibers (elongated cells in bundles; flax, hemp) and sclereids (short, irregular cells; the gritty texture in pears; the hard shell of walnuts).

### Vascular Tissue System -- Xylem in Detail

The vascular tissue system is the plant's long-distance transport network.

**Xylem** (water and mineral transport, upward) develops in two temporally distinct phases that yield mechanically distinct conduits:

**Protoxylem** matures while the surrounding tissue is still elongating. Its conduits must therefore stretch with the growing organ, so secondary-wall lignification is restricted to **annular** (ring-shaped) or **helical** (spiral) thickenings. These thickenings allow elongation but provide limited collapse-resistance under tension; protoxylem conduits are typically narrow (5–25 µm) and frequently obliterated as the tissue matures, leaving an air-filled lacuna.

**Metaxylem** differentiates after elongation has ceased. With no constraint on extensibility, metaxylem develops continuous lignified walls with **scalariform** (ladder-like), **reticulate** (net-like), or **pitted** thickenings. Metaxylem conduits are wider (50–500 µm in some lianas), longer-lived, and bear the bulk of mature transpiration flux.

A simple mnemonic: **proto = first** (extensible, ephemeral), **meta = mature** (durable, mechanically robust). The transition can be visualized in any longitudinal section of an elongating maize root: closer to the tip, narrow protoxylem dominates; further back in the maturation zone, metaxylem vessels of much greater caliber come on-line.

The two principal cell types of xylem differ markedly in mechanics:

- **Tracheids:** Long (1-5 mm), tapered cells with lignified secondary walls. Dead at maturity. Water moves between tracheids through bordered pit pairs (thin regions in the cell wall where secondary wall is absent). The pit membrane consists of the unmodified primary walls of the two adjacent cells plus the middle lamella; in conifers it bears a thickened central **torus** suspended by a porous **margo**, allowing the torus to seal the pit aperture if the adjacent conduit cavitates (an **aspirated pit**). Tracheids are found in most vascular plants and constitute the primary conducting element in most gymnosperms.
- **Vessel elements:** Shorter (0.2–1 mm), sometimes wider conducting cells, reaching 500 µm diameter in some lianas. Perforation plates connect elements into vessels; pits connect neighboring conduits. Dimensions, pits and network architecture determine conductance and embolism resistance, not an inherent vessel-versus-tracheid safety ranking.

**Bordered pit mechanics — the torus-margo valve:**

The conifer bordered pit is one of the most elegant valve structures in biology. The pit membrane is differentiated into two regions:

- **Torus:** A thickened, impermeable central disc (~5 µm diameter) made of cellulose microfibrils embedded in a lignified matrix
- **Margo:** A porous mesh of radial cellulose strands surrounding the torus, with pore sizes of 50–200 nm

Under normal flow, water moves through the porous margo. A pressure differential between an embolized and a water-filled tracheid can displace the torus against the pit aperture, **aspirating** the pit and limiting air spread. Seal geometry, torus overlap and membrane properties affect failure; a margo pore size alone does not specify an air-seeding threshold or a whole-tree safety margin.

Most angiosperm intervessel pit membranes lack a torus and resist air entry through their membrane structure. Their air-seeding thresholds vary among species and tissues; neither the absence of a torus nor vessel diameter alone establishes a universal safety ranking against conifers.

**Mechanical properties — the safety-efficiency tradeoff:**

The Hagen-Poiseuille equation predicts that volumetric flow scales as the *fourth power* of conduit radius:

\begin{equation}
Q = \frac{\pi r^4 \Delta P}{8 \eta L}
\label{eq:unit_VIII_hagen_poiseuille}
\end{equation}

where $Q$ is volumetric flow (m³/s), $r$ conduit radius (m), $\Delta P$ pressure drop (Pa), η dynamic viscosity (approximately 10⁻³ Pa·s for water at 20 °C), and $L$ length (m). Doubling radius gives 16-fold ideal conductance only with the other inputs fixed. Tissue conductivity also depends on conduit density, lengths, pits and connectivity; diameter alone does not establish embolism resistance. A woody-species synthesis found weak safety–efficiency correlations, not a universal category ranking \citep{gleason2016safetyefficiency}.

**Phloem** (sugar and organic compound transport, bidirectional):

- **Sieve tube elements:** Living at maturity but lack nucleus, [**ribosome**](#gl:ribosome)s, and tonoplast at maturity. Connected end-to-end at sieve plates (modified cell walls perforated by sieve pores, 1-15 µm diameter). P-[**protein**](#gl:protein) (phloem protein) plugs sieve pores when cells are damaged, preventing phloem sap loss.
- **Companion cells:** Retain full complement of [**organelle**](#gl:organelle)s. Connected to sieve tube elements by numerous plasmodesmata. Provide metabolic support including ATP for active sugar loading. Transfer cells (specialized companion cells with wall ingrowths) increase membrane surface area for active transport.

**Concept Check 3:** Why must xylem conducting cells be dead at maturity, while phloem sieve tube elements must remain alive?

**Concept Check 4:** Using the Hagen-Poiseuille relation, calculate the ratio of volumetric flow between a vessel of radius 100 µm and a tracheid of radius 25 µm, holding pressure gradient and length constant. Explain why drought-prone species may nevertheless favor the narrower conduit.

**Concept Check 5:** A botanist examines a longitudinal section of an emerging shoot from a deciduous tree. She notes spirally banded conduits near the apex but reticulate-pitted conduits 5 cm behind. Identify each conduit type and explain the developmental logic of the difference.

---

## Water Relations -- Water Potential

Plants control water movement using **water potential** (Ψ, units: MPa). The complete four-component formulation captures every thermodynamically relevant contribution to water's free energy:

\begin{equation}
\Psi = \Psi_s + \Psi_p + \Psi_m + \Psi_g
\label{eq:unit_VIII_water_potential}
\end{equation}

where:

- **$\Psi_s$** = osmotic (solute) potential = $-iCRT$ (typically $\leq 0$; solutes decrease water potential). $i$ is the van 't Hoff dissociation factor, $C$ is molar concentration, $R$ is the gas constant, $T$ is temperature in Kelvin.
- **$\Psi_p$** = pressure (turgor) potential. Positive in turgid cells (turgor pressure against cell wall). Negative in xylem under tension. Can range from +2 MPa in highly turgid cells to $-10$ MPa or lower in xylem of tall trees.
- **$\Psi_m$** = matric potential. Reflects water binding to colloidal surfaces (cell walls, soil clay particles, dry seeds). Typically $\leq 0$. Typically negligible in well-hydrated cells but dominates in dry seeds (where $\Psi_m$ can reach $-100$ MPa) and in dry soils.
- **$\Psi_g$** = gravitational potential = $\rho gh$, relative to a stated height datum. Above soil level, $\Psi_g(10\,\mathrm m)=+0.0981$ MPa and $\Psi_g(100\,\mathrm m)=+0.981$ MPa for $\rho=1000$ kg m$^{-3}$ and $g=9.81$ m s$^{-2}$. Upward flow requires a sufficiently negative pressure gradient to overcome this positive gravitational contribution and flow resistance.

In well-hydrated, free-flowing systems (most active leaf and root cells) $\Psi_m$ is folded into $\Psi_p$ and the simplified three-component form $\Psi = \Psi_s + \Psi_p + \Psi_g$ is used. In dry seeds, lichens, and very dry soils, $\Psi_m$ must be retained explicitly. See \cref{eq:unit_VIII_water_potential}. \cref{fig:unit_VIII_water_potential_transpiration} links solute-driven $\Psi_s$ shifts to Fick-law transpiration flux under varying stomatal conductance.

### Worked Example: Calculating Water Potential

**Problem:**
A plant cell has a solute concentration of $C = 0.3 \text{ mol L}^{-1}$ sucrose ($i=1$) at $T = 293 \text{ K}$ (20 °C) and a turgor pressure ($\Psi_p$) of $0.5 \text{ MPa}$. Assuming normal height where $\Psi_g = 0$ and the cell is well hydrated so $\Psi_m \approx 0$, what is the cell's total [**water potential (Ψ)**](#gl:water-potential)? If this cell is placed in an open beaker of pure water ($\Psi = 0$), will water flow into or out of the cell?

**Solution:**

1. **Calculate the osmotic potential ($\Psi_s$):**
   Using the van 't Hoff equation $\Psi_s = -iCRT$, where $R = 0.00831 \text{ L MPa mol}^{-1}\text{ K}^{-1}$:
   $$ \Psi_s = -(1) \cdot (0.3 \text{ mol L}^{-1}) \cdot (0.00831 \text{ L MPa mol}^{-1}\text{ K}^{-1}) \cdot (293 \text{ K})  \label{eq:unit_VIII_plant_structure_and_water_item_1}$$

   $$ \Psi_s \approx -0.73 \text{ MPa}  \label{eq:unit_VIII_plant_structure_and_water_item_2}$$


2. **Calculate the total water potential (Ψ):**
   $$ \Psi = \Psi_s + \Psi_p + \Psi_m + \Psi_g  \label{eq:unit_VIII_plant_structure_and_water_item_3}$$

   $$ \Psi = -0.73 \text{ MPa} + 0.5 \text{ MPa} + 0 + 0  \label{eq:unit_VIII_plant_structure_and_water_item_4}$$

   $$ \Psi = -0.23 \text{ MPa}  \label{eq:unit_VIII_plant_structure_and_water_item_5}$$


3. **Determine the direction of water flow:**
   Water typically moves from higher water potential to lower water potential. Since the beaker of pure water is at $\Psi = 0$ and the cell is at $\Psi = -0.23 \text{ MPa}$, water will flow **into the cell** until the cell's turgor pressure rises sufficiently to reach equilibrium ($\Psi = 0$).

Water typically moves from **higher to lower water potential** (down the Ψ gradient).

### Worked Example: A Leaf Cell at Dawn vs Midday

**Problem:** A mesophyll cell at dawn (cool, humid, stomata closed) has $\Psi_s = -1.1$ MPa, $\Psi_p = +0.9$ MPa, $\Psi_m \approx 0$, $\Psi_g \approx 0$. By midday (hot, dry, stomata open and transpiring), the cell loses water: $\Psi_s = -1.4$ MPa (solutes concentrated by 27.3%, corresponding to 21.4% volume loss at fixed solute amount), $\Psi_p = +0.2$ MPa. Compute Ψ in both states and identify which component drives the change.

**Solution:**

- Dawn: $\Psi = -1.1 + 0.9 = -0.2$ MPa
- Midday: $\Psi = -1.4 + 0.2 = -1.2$ MPa

Total Ψ has fallen by 1.0 MPa. Decomposing the change:

- $\Delta\Psi_s = -0.3$ MPa (small contribution from solute concentration)
- $\Delta\Psi_p = -0.7$ MPa (dominant contribution)

The midday plunge is driven primarily by **loss of turgor**. The cell remains alive and below the wilting threshold, but it is approaching the limit at which growth (which requires $\Psi_p > Y$ in the Lockhart equation) ceases. This is the molecular basis of midday "growth pause" almost universally observed in field crops.

```mermaid
flowchart LR
    subgraph Components ["Water Potential Components"]
        S["Solute Potential (psi_s)<br/>Always <= 0<br/>More solutes = more negative"]
        P["Pressure Potential (psi_p)<br/>Positive (turgor) or<br/>Negative (tension in xylem)"]
        G["Gravity Potential (psi_g)<br/>= rho*g*h<br/>Significant in tall trees"]
        M["Matric Potential (psi_m)<br/>Surface binding<br/>Dominates in dry seeds"]
    end
    S --> T["Total Water Potential<br/>psi = psi_s + psi_p + psi_m + psi_g"]
    P --> T
    G --> T
    M --> T
    T --> Move["Water moves from<br/>HIGH psi to LOW psi"]
    Move --> Soil["Illustrative moist-soil profile<br/>Soil: −0.03 MPa"]
    Soil --> Root["Root xylem: −0.3 MPa"]
    Root --> Stem["Stem xylem: −0.8 MPa"]
    Stem --> Leaf["Leaf mesophyll: −1.5 MPa"]
    Leaf --> Atm["Atmosphere: approximately −95 MPa<br/>at 25 °C and 50% RH"]
```
<!-- alt: Flowchart showing components of water potential and one illustrative soil–plant–atmosphere profile. Passive water flow follows decreasing total water potential. These are consistent example values, not independent universal ranges; sufficiently dry soil can stop or reverse root uptake. -->

*Components of water potential and one illustrative soil–plant–atmosphere profile. Passive water flow follows decreasing total water potential. These are consistent example values, not independent universal ranges; sufficiently dry soil can stop or reverse root uptake.*

### Quantitative Turgor Relations and Plasmolysis

**Turgor pressure** ($\Psi_p$) is generated when a cell with low internal $\Psi_s$ takes up water until the cell wall resists further expansion. The cell-wall yield curve is described by the **Lockhart equation** for irreversible expansion:

\begin{equation}
\frac{1}{V}\frac{dV}{dt} = \phi (\Psi_p - Y)
\label{eq:unit_VIII_lockhart}
\end{equation}

where φ is wall extensibility (a measure of how readily the wall yields), $\Psi_p$ is current turgor, and $Y$ is the yield threshold below which the wall behaves elastically (no growth). Cells grow primarily when $\Psi_p > Y$. In the elongation zone, expansin-mediated wall loosening reduces $Y$, allowing growth even at modest turgor.

**Plasmolysis** is the separation of the protoplast from the cell wall when the cell is placed in a hypertonic solution (external $\Psi_s$ more negative than internal). Three phases:

1. **Incipient plasmolysis:** Turgor reaches zero ($\Psi_p = 0$); at this point $\Psi = \Psi_s$. The protoplast is just losing contact with the wall.
2. **Concave plasmolysis:** Protoplast withdraws inward; plasma membrane appears scalloped at the corners.
3. **Convex plasmolysis:** Protoplast becomes a small spherical body in the center of the cell; reversible if rehydrated within minutes, but prolonged plasmolysis kills the cell.

**Worked Example — Quantitative Plasmolysis:** A cell at $\Psi_p = 0.5$ MPa, $\Psi_s = -0.73$ MPa is placed in a sucrose solution at $\Psi_s = -1.0$ MPa. Water leaves the cell. As water exits, $\Psi_s$ becomes more negative (solutes concentrate; take solute amount and temperature as constant). At incipient plasmolysis, $\Psi_p = 0$ and $\Psi_{cell} = \Psi_s$ must equal $\Psi_{external} = -1.0$ MPa. Since $\Psi_s$ scales inversely with cell volume ($\Psi_s \cdot V$ ≈ constant for ideal solutes), we calculate the relative volume at incipient plasmolysis as $V_p / V_0 = \Psi_{s,0} / \Psi_{s,p} = -0.73 / -1.0 = 0.73$, i.e., the cell loses ~27% of its initial volume before plasmolysing.

At full turgor: $\Psi_p = -\Psi_s$, so $\Psi = 0$ (cell is in equilibrium with pure water).

> **Clinical Connection:** Agricultural irrigation management relies on measuring soil water potential with tensiometers. When soil Ψ falls below $-1.5$ MPa (the permanent wilting point), most crop plants cannot extract water. Precision irrigation triggered at species-specific Ψ thresholds saves 20-40% of water compared to schedule-based irrigation.

**Concept Check 6:** A seed at storage moisture has $\Psi_m \approx -100$ MPa, $\Psi_s \approx -2$ MPa, and $\Psi_p = 0$. When placed on moist filter paper at $\Psi = -0.05$ MPa, water is rapidly imbibed. Explain which component dominates the imbibition gradient and why imbibition is a one-way process.

---

## Water Transport Pathways

### Apoplast vs Symplast Pathways

Water and dissolved minerals travel from the root surface to the xylem via two parallel routes:

**Apoplast pathway:** Water moves through connected cell walls and intercellular spaces without membrane crossing along that segment. Its contribution depends on pressure gradients, anatomy and barriers; no universal speed ranking follows.

**Symplast pathway:** Water moves through connected cytoplasm via plasmodesmata after membrane entry. Membrane transport can confer selectivity, but neither this route nor the endodermis guarantees perfect toxic-ion exclusion.

**Transmembrane pathway:** Water crosses plasma membranes via aquaporins (water channel proteins, PIP and TIP families; ~35 aquaporin genes in *Arabidopsis*). Aquaporin activity is regulated by phosphorylation, [**pH**](#gl:ph), and Ca$^{2+}$.

### Root Anatomy in Depth — The Endodermis as Filter

Radial anatomy of a young dicot root (from outside inward):

1. **Epidermis** with root hairs — initial absorption surface
2. **Cortex** — multiple layers of parenchyma; storage and apoplastic transport corridor; rich in plasmodesmata
3. **Endodermis** — single layer; the critical apoplastic checkpoint
4. **Pericycle** — cell layer giving rise to lateral roots
5. **Vascular cylinder (stele)** — central xylem and phloem strands

**The Casparian strip — chemistry and synthesis:**

The localized Casparian strip and later suberin lamellae are distinct barriers. In Arabidopsis, functional early strips form with lignin but without suberin \citep{naseer2012casparian}:

- **Lignin** is a phenylpropanoid polymer assembled from monolignol units. In a differentiated functional strip, localized lignification forms a continuous endodermal wall belt; immature patches or defective gaps are distinct from an intact barrier. In the cited Arabidopsis preparations, lignin-dependent tracer exclusion distinguished the localized strip from later suberin deposition \citep{naseer2012casparian}.
- **Suberin** (an aliphatic-aromatic polyester of long-chain ω-hydroxy fatty acids and ferulate esters) is deposited later as the **suberin lamella** on the inner face of the cell wall, after the Casparian strip is mature. Suberisation is regulated by SGN3-CIF1/CIF2 receptor-peptide signaling, which monitors the integrity of the Casparian strip via leakage of CIF peptides from stele to cortex.

**Different barrier functions:** Localized lignification restricts radial apoplastic diffusion; later suberin lamellae alter access to endodermal membranes and radial transport. Polymer presence alone does not establish complete exclusion of every solute or eliminate developmental bypasses.

**Bypass routes — apoplastic leakage at lateral root junctions:**

Lateral-root emergence changes barrier geometry, but a junction's presence does not establish the location or fraction of sodium bypass flow. In a study of Pokkali and IR20 rice, lateral-root density did not correlate with the measured bypass; barrier development, conditioning and genotype affected the comparison \citep{krishnamurthy2011ricebarriers}. Use paired tracer and ion-delivery measurements under specified conditions rather than a common rice/wheat fraction inferred from anatomy.

**Symplastic vs transmembrane pathways:**

- **Symplastic transport** moves through connected cytoplasm via plasmodesmata after initial membrane entry; it does not bypass plasma membranes entirely. Plasmodesmal aperture can be regulated by callose and other developmental/stress-dependent processes, changing intercellular transport.
- **Transmembrane pathway** crosses membranes repeatedly via water channels and solute transporters. Its conductance and selectivity depend on expression, gating, gradients and tissue state, not a universal slowest-route rule.

In practice, the three pathways operate simultaneously; the relative contribution shifts with developmental stage, salinity, and mycorrhizal colonization.

**Passage cells:** Some older-root endodermal cells remain relatively unsuberized and can provide membrane-mediated transport routes. A passage cell can retain a Casparian strip; absence of a suberin lamella is not an unrestricted apoplastic hole or proof that the remaining endodermis is completely sealed.

Rice can develop exodermal as well as endodermal apoplastic barriers. Their distribution and effects vary with development, genotype and environment; the Pokkali–IR20 experiments measured condition-dependent transport differences \citep{krishnamurthy2011ricebarriers}. These barriers do not make rice generally salt tolerant or establish a species-wide tolerance ranking.

```mermaid
---
config:
  layout: dagre
---
flowchart TB
    SOIL["Soil solution → root surface"]
    SOIL -->|apoplast| APO["Cortical cell walls<br/>Intact Casparian strip<br/>limits radial apoplastic passage"]
    SOIL -->|membrane entry| SYM["Cortical cytoplasm<br/>Symplastic transport<br/>via plasmodesmata"]
    SOIL -->|repeated membrane crossings| TRANS["Transmembrane route<br/>Across root-cell membranes"]
    APO -->|membrane-mediated entry| ENDO["Endodermal cytoplasm"]
    SYM --> ENDO
    TRANS --> ENDO
    ENDO -->|aquaporins and transporters| STELE["Pericycle and stele<br/>→ xylem conduit"]
    classDef default fill:#f4f5f6,stroke:#59636e,color:#17212b
```
<!-- alt: Flowchart showing an idealized intact endodermal barrier restricts radial apoplastic passage without making the continuing water route exclusively symplastic. Membrane-mediated and repeated transmembrane routes are shown; developmental bypasses and quantitative flow fractions require separate evidence. -->

*An idealized intact endodermal barrier restricts radial apoplastic passage without making the continuing water route exclusively symplastic. Membrane-mediated and repeated transmembrane routes are shown; developmental bypasses and quantitative flow fractions require separate evidence.*

---

## Transpiration and the Cohesion-Tension Mechanism

### Historical Context: The Birth of Cohesion-Tension Theory \citep{dixon1894}

The question of how water reaches the canopy of a tall tree exercised plant physiologists throughout the 19th century. Early proposals invoked **root pressure** (positive xylem pressure generated by active mineral secretion overnight; it can be measured by exudation from cut stumps at 0.05–0.5 MPa), giving ideal hydrostatic heads of about 5.1–51 m ($h=P/(\rho g)$), before flow resistance. This cannot explain sustained ascent in the tallest trees and is weak or absent in many species. **Capillarity** in xylem conduits could lift water about 1 m for the stipulated conduit geometry. **Atmospheric pressure** supports a column of about 10.3 m under sea-level conditions. None alone accounts for water rising to 100 m in *Sequoia*.

In 1894, Henry Dixon (Trinity College Dublin) and John Joly proposed a radical alternative: water in the xylem is under **tension** (negative pressure), pulled from above by evaporation rather than pushed from below \citep{dixon1894}. Liquid water under tension is metastable, but nucleation depends on gas nuclei, surfaces and pressure history, not merely on pressure being negative. Idealized estimates such as a tensile strength near $-140$ MPa describe water under specified physical assumptions, not a practical tree-height limit or a universal xylem failure threshold.

### Detailed TACT Mechanism

Water ascent in tall trees is explained by the **cohesion-tension-adhesion (TACT) mechanism**, refined by Renner (1911), and validated with pressure probes and MRI:

```mermaid
sequenceDiagram
    participant Atm as Atmosphere<br/>(psi ≈ −95 MPa, 25 °C, 50% RH)
    participant Leaf as Leaf Mesophyll<br/>(psi = -1.5 MPa)
    participant Xylem as Xylem Column<br/>(Continuous water column)
    participant Root as Root<br/>(psi = -0.3 MPa)
    participant Soil as Soil<br/>(psi = -0.03 MPa)

    Atm->>Leaf: 1. Evaporation at cell wall surface<br/>(driven by VPD)
    Note over Leaf: Water meniscus at cell wall<br/>generates negative pressure
    Leaf->>Xylem: 2. Tension (negative pressure)<br/>pulls water column upward
    Note over Xylem: Cohesion supports a metastable column<br/>Embolism vulnerability depends on structure and conditions
    Note over Xylem: Adhesion: water clings<br/>to hydrophilic xylem walls
    Xylem->>Root: 3. Tension transmitted<br/>through continuous column
    Root->>Soil: 4. Lower root water potential<br/>establishes uptake gradient
    Soil->>Root: Water uptake down psi gradient
    Root->>Xylem: Water transport upward
    Xylem->>Leaf: Water supply to evaporating surfaces
    Leaf->>Atm: Water vapor loss
    Note over Soil,Atm: Causal tension signals and material<br/>water transport have distinct arrows
```
<!-- alt: Sequence diagram showing transpiration-cohesion-tension mechanism of water ascent Evaporation at the leaf surface generates tension (negative pressure) that is transmitted through the continuous water column in the xylem, pulling water upward from the roots. Cohesion between water molecules and adhesion to xylem walls maintain the column. -->

*The transpiration-cohesion-tension mechanism of water ascent Evaporation at the leaf surface generates tension (negative pressure) that is transmitted through the continuous water column in the xylem, pulling water upward from the roots. Cohesion between water molecules and adhesion to xylem walls maintain the column.*

1. **Transpiration** from leaves drives evaporation at the mesophyll cell wall surface. Water evaporates from the thin film coating the cell wall into the substomatal air space, then diffuses out through open stomata.

2. As water evaporates, the air-water interface retreats into the nanoscale pores of the cell wall. Surface tension at this curved meniscus generates a large negative pressure (tension), following the Young-Laplace equation:

\begin{equation}
\Delta P = \frac{2\gamma \cos\theta}{r}
\label{eq:unit_VIII_young_laplace}
\end{equation}

Here $\Delta P=P_{\mathrm{air}}-P_{\mathrm{water}}$ is the pressure difference across a wetting concave meniscus, $\gamma=0.0728$ N/m, $\theta$ is contact angle and $r$ is pore radius. With $\cos\theta\approx1$ and stipulated radii 5–10 nm, the model gives water pressure approximately 29.1–14.6 MPa below air pressure. These are geometry-dependent pressure differences, not a measured universal xylem failure threshold.

3. This tension propagates through connected water columns in xylem conduits (tracheids and vessels) because of water's strong **cohesion** ([**hydrogen bond**](#gl:hydrogen-bond)s). Actual embolism vulnerability must be measured in the species, organ and conditions of interest; the idealized tensile strength of water cannot substitute for a xylem vulnerability curve.

4. **Adhesion** of water to the hydrophilic, lignified xylem walls prevents the water column from pulling away from the conduit walls.

5. The tension at the top of the column draws water from the roots, which in turn absorbs water from the soil down the water potential gradient.

### Cohesion-Tension Theory: Embolism Evidence and Synchrotron Imaging

The cohesion-tension model is not without controversy, and its mature form represents a triumph of integrating ecological, physical, and microscopic evidence — together with rebuttals to specific objections.

**Lines of supporting evidence:**

1. **Pressure-bomb measurements** (Scholander *et al.*, 1965) directly demonstrate that excised stems of transpiring trees release water primarily when external pressure is applied, consistent with negative xylem pressure prior to excision. Pressure required matches predictions of the tension hypothesis (typically $-1$ to $-3$ MPa for well-watered crops; $-6$ to $-10$ MPa under drought).
2. **Magnetic resonance imaging (MRI)** in vivo (Holbrook *et al.*, 2001) visualizes continuous water columns in mature angiosperm trunks, with abrupt transitions to embolised conduits matching predictions of tension-induced cavitation.
3. **Pressure probes** (Steudle, 1995) in living root cortex cells confirm steep tension gradients between epidermis and stele consistent with bulk-flow-driven uptake.
4. **Acoustic emission** of xylem during drought (Tyree and Sperry, 1989) records sharp clicks corresponding to individual cavitation events, the count of which scales with drought severity.

**The embolism debate:**

Critics (most prominently U. Zimmermann and colleagues, 1990s–2000s) argued that water columns under tensions of $-1$ MPa or more should be metastable and would cavitate continuously, making sustained negative pressures of $-10$ MPa physiologically implausible. The Zimmermann school proposed alternative "tissue tension" models in which water moved by mechanisms other than bulk flow.

This challenge has been progressively resolved by direct visualization:

- **Improved pressure probes** (Wei *et al.*, 1999) confirmed predicted tensions in living conduits without artifact.
- **Synthetic-tree experiments** (Wheeler and Stroock, *Nature* 2008) constructed transparent microfluidic devices replicating the geometry of a leaf's evaporative surface; these "synthetic trees" sustained water under tension to $-22$ MPa, mirroring biological systems and proving that cell wall pore geometry alone is sufficient to support the predicted tensions.
- **Synchrotron X-ray micro-CT** (Brodersen *et al.*, *Plant Physiol.* 2010; Choat *et al.*, *Nature* 2012) imaged living xylem in real time and showed that under moderate drought, embolisms are confined to a small fraction of conduits — settling the long-running argument over how prevalent embolism is in actively transpiring plants. Synchrotron imaging also visualized **embolism repair** under daily root pressure: embolised conduits refill overnight in *Vitis* and *Laurus*.

**Mechanism of embolism repair:** Two complementary mechanisms are now well-attested:

- **Root pressure refilling:** Active mineral secretion into xylem at night generates positive xylem pressure (0.05–0.5 MPa) sufficient to push water back into embolised conduits. Common in herbaceous species and in many trees overnight.
- **Phloem-driven refilling:** Phloem-derived sugars osmotically draw water into embolised conduits via parenchyma cells lining the xylem (Salleo *et al.*, 2004; Nardini *et al.*, 2011). This mechanism operates against negative bulk xylem pressure and is observed during the day.

**Net assessment:** The TACT mechanism is correct in its essentials. Water in xylem is genuinely under tension; the column is stabilized by cohesion and adhesion at scales where pore geometry sustains negative pressures far beyond what bulk water could endure. The system is metastable but biologically sufficient — and the cost of occasional cavitation is mitigated by redundant pathways and active repair.

### Xylem Transport Parameters

**Xylem sap velocity** measured by MRI and heat pulse methods: 3-45 m/h in trees; 15-50 m/h in herbaceous plants. Ring-porous trees (oak, elm) can reach velocities of 40+ m/h in their large early-wood vessels.

**Transpiration flux** (Fick's first law for water vapor):

\begin{equation}
E = g_s \cdot \Delta w
\label{eq:unit_VIII_transpiration_flux}
\end{equation}

where $g_s$ is molar stomatal conductance (mol m$^{-2}$ s$^{-1}$), $\Delta w=w_i-w_a$ is the dimensionless water-vapor mole-fraction difference (mol/mol), and $E$ has units mol m$^{-2}$ s$^{-1}$. At equal total pressure, $\Delta w=(e_i-e_a)/P$. Vapor concentrations in mol m$^{-3}$ must first be divided by total air molar density $P/(RT)$; they cannot be substituted directly. For illustrative $g_s=0.2$ and $w_i-w_a=0.005$, $E=0.001$ mol m$^{-2}$ s$^{-1}=1$ mmol m$^{-2}$ s$^{-1}$. Boundary-layer resistance is omitted here.

A well-watered broadleaf tree can transpire 200-400 liters of water per day. A large oak may transpire over 150,000 liters during a growing season.

### Cavitation and Embolism

When xylem tension exceeds the capacity of the water column, dissolved gas comes out of solution forming a bubble -- **cavitation**. The gas bubble expands to fill the conduit, creating an **embolism** (air lock) that blocks water flow.

Plants have evolved multiple strategies to manage cavitation:

- **Conduit dimensions and safety:** For an otherwise identical ideal tube, larger radius increases conductance, but embolism resistance depends strongly on pits and other anatomical traits. A safety–efficiency tradeoff is not a universal species ranking: comparative data show only a weak relationship between xylem-specific efficiency and embolism resistance \citep{gleason2016safetyefficiency}.
- **Pit membranes:** In tracheids, bordered pits have a torus-margo structure. When one tracheid cavitates, the torus seals against the pit aperture, preventing air from spreading to adjacent conduits.
- **Embolism repair:** Some plants can refill embolisms overnight when transpiration ceases and root pressure (positive xylem pressure generated by active mineral secretion into xylem) pushes water back into embolised conduits.
- **Redundant pathways:** Multiple parallel conduits ensure that loss of some to embolism does not stop water transport entirely.

> **Ecological Connection:** Drought can impair hydraulic transport, but a narrow-vessel desert shrub is not automatically safer than a wide-vessel rainforest tree. Compare measured vulnerability curves, operating water potentials, stomatal responses and exposure. Hydraulic dysfunction can contribute to mortality alongside other stresses; a conductance-loss threshold is not itself a universal lethal threshold \citep{choat2012hydraulicmargins}.

**Concept Check 8:** In a stipulated comparison, a conifer sample retains most conductivity at $-6$ MPa while a ring-porous angiosperm sample loses conductivity at $-2$ MPa. Propose pit-structure and conduit-network hypotheses, and identify the anatomical and vulnerability-curve measurements needed to test them. Why would this comparison not establish a universal conifer–angiosperm ranking?

### Worked Example: Water Potential in the Transpiration Stream

**Problem:** Track the illustrative local water-potential ($\Psi=\Psi_s+\Psi_p$) gradient between xylem and leaf mesophyll before and after stomatal opening. State the flow direction and what additional measurements would be needed to assess embolism risk.

Initial (pre-dawn, stomata closed):

- Leaf mesophyll cell: $\Psi_s = -1.2$ MPa, $\Psi_p = +0.3$ MPa $\Rightarrow \Psi_{\text{leaf}} = -0.9$ MPa
- Adjacent xylem sap: $\Psi_s \approx -0.1$ MPa, $\Psi_p = -0.8$ MPa (modest standing tension) $\Rightarrow \Psi_{\text{xylem}} = -0.9$ MPa

The cell is at equilibrium with the xylem ($\Delta\Psi = 0$). No net flow.

**Stomata open at sunrise; evaporation first lowers mesophyll water potential and transmits tension to the xylem:**

- Xylem now: $\Psi_s \approx -0.1$ MPa, $\Psi_p = -1.5$ MPa $\Rightarrow \Psi_{\text{xylem}} = -1.6$ MPa
- Leaf cell after initial evaporative loss: $\Psi_s=-2.0$ MPa and $\Psi_p=+0.2$ MPa, giving $\Psi_{\text{leaf}}=-1.8$ MPa. These are illustrative states at approximately the same height, so gravity cancels in this local comparison.

**Solution:**

1. **Driving force.** $\Psi_{\text{xylem}}-\Psi_{\text{leaf}}=-1.6-(-1.8)=+0.2$ MPa.
2. **Direction.** Water flows from higher $\Psi$ (xylem, $-1.6$ MPa) into lower $\Psi$ (mesophyll, $-1.8$ MPa), replacing water evaporated from cell-wall surfaces. The soil–root–xylem–mesophyll–air continuum supplies this loss; stomata are diffusion pores, not pumps.
3. **Embolism risk is not determined by these states alone.** The stipulated xylem pressure is $-1.5$ MPa, but no species-, organ- and protocol-specific vulnerability curve is supplied. A measured $P_{50}$ describes pressure at 50% conductivity loss in that assay, not the onset of every cavitation event or a universal lethal threshold.

**Interpretation.** Evaporation, the local water-potential gradient and xylem tension are coupled in this model. To assess a biological safety margin, measure operating water potentials and a matching vulnerability curve, and specify the loss endpoint, hydraulic network and exposure. Neither vessel width alone nor crossing $P_{50}$ determines mortality; species and conditions must be compared explicitly \citep{choat2012hydraulicmargins,gleason2016safetyefficiency}.


---

## Stomatal Regulation of Water Loss and CO2 Uptake

Stomata represent the critical control point where plants balance carbon gain (CO$_2$ uptake for photosynthesis) against water loss (transpiration).

### Stomatal Opening — Guard Cell Ion Fluxes

In Arabidopsis, blue-light opening involves phototropins and coordinated guard-cell solute accumulation; related Vicia faba experiments support several pump-regulation and osmolyte steps below. Individual transporter contributions and resulting ion concentrations, potentials and apertures depend on species and experimental conditions:

1. **Blue light activates phototropins** PHOT1 and PHOT2 in the studied Arabidopsis response \citep{kinoshita2001phototropins}.
2. **Pump phosphorylation precedes reader binding.** Downstream signaling promotes phosphorylation of the plasma-membrane H$^+$-ATPase at its penultimate C-terminal Thr. Subsequent 14-3-3 binding helps relieve autoinhibition and activate the pump; 14-3-3 is the binding regulator, not the phosphate writer \citep{hayashi2010pump,fuglsang1999aha2}.
3. **ATP-dependent H$^+$ extrusion** makes the interior more negative and establishes a proton electrochemical gradient.
4. **Inward K$^+$ transport** depends on driving force and channel gating. Arabidopsis guard cells express KAT1 and other channel subunits, including KAT2. The studied KAT1-deficient insertion line retained opening under its assay conditions and showed somatic reversion/residual transcript; this refutes unique KAT1 necessity without proving every complete null normal in every condition \citep{szyroki2001kat1}.
5. **Counterion accumulation** accompanies K$^+$ uptake. Depending on availability and conditions, it includes chloride or nitrate uptake and metabolically accumulated malate; accumulation does not identify one universal transport route.
6. **Transport compartments matter.** CHL1/NRT1.1 contributes to guard-cell nitrate uptake/opening in nitrate-supplied Arabidopsis. AtCLCc contributes to vacuolar homeostasis across the tonoplast, not external uptake across the plasma membrane. SLAH3 participates in anion release/closure signaling, not the proposed reverse-mode chloride-import mechanism \citep{guo2003nitrate,jossier2010clcc,geiger2011slah3}.
7. **Organic osmolytes also contribute.** Vicia faba epidermal-peel experiments found light-quality- and time-dependent malate/sucrose changes; they do not establish a universal afternoon sucrose fraction \citep{talbott1993osmolytes}.
8. **Solute accumulation lowers osmotic potential.** Water enters when total guard-cell water potential falls below that of its surrounding water source; pressure as well as solute potential matters.
9. **Turgor and wall mechanics** couple water uptake to changes in guard-cell shape and pore opening.
10. **Aperture is an outcome to measure**, not a fixed species-independent width predicted from this schematic sequence.

### Stomatal Closure -- ABA Signaling Cascade in Detail

Under drought stress, abscisic acid (ABA) triggers rapid stomatal closure through a molecular relay that has become a textbook example of plant signal transduction. The pathway can be summarized in five steps:

> **ABA → PYR1 → PP2C → SnRK2 → SLAC1**

Each step in this cascade has been crystallographically resolved (PYR1-ABA-PP2C ternary complex, Melcher *et al.*, *Nature* 2009; SnRK2-PP2C complex, Soon *et al.*, *Science* 2012) and is now textbook signaling.

1. **ABA synthesis:** Soil drying activates NCED3 (9-*cis*-epoxycarotenoid dioxygenase) in roots, cleaving 9'-*cis*-violaxanthin/neoxanthin to xanthoxin (ABA precursor). Local ABA biosynthesis also occurs in leaf vasculature and guard cells themselves.
2. **ABA distribution:** ABA travels via xylem to guard cells and is concentrated by the AIT1/NPF4 family of ABA importers and the ABCG25 exporter.
3. **Receptor binding:** ABA binds **PYR/PYL/RCAR** receptors (14 paralogs in *Arabidopsis*) at a START-domain pocket. This binding "closes" the receptor's gate loop over the binding pocket.
4. **PP2C inhibition:** The closed ABA-PYR complex docks onto and **inhibits Type-2C protein phosphatases** (ABI1, ABI2, HAB1). PP2Cs normally dephosphorylate (and thereby inactivate) downstream kinases.
5. **SnRK2 signaling:** Relief of inhibitory PP2C control permits SnRK2-dependent signaling, including OST1/SnRK2.6. Downstream ABA responses include:
   - **SLAC1** anion channel: phosphorylation-dependent activation permits chloride/nitrate efflux in the measured selectivity preparations and can depolarize the membrane. Ser120 regulation does not mean that phosphorylation of one site alone is sufficient, and SLAC1 is not the principal malate-release route \citep{geiger2009slac1}.
   - **GORK** outward-rectifying K$^+$ channel: opens at depolarized potentials; K$^+$ leaves the cell down its electrochemical gradient
   - **Inward K$^+$ uptake** can be inhibited during ABA signaling, restricting re-entry rather than specifying identical gating for inward rectifiers and GORK.
   - **NADPH oxidase RBOHF**: produces reactive oxygen species (ROS) that activate Ca$^{2+}$-permeable channels, raising cytosolic Ca$^{2+}$ and amplifying SLAC1/GORK responses
6. **Osmotic deflation:** Net solute loss raises guard-cell osmotic potential; water exits when the total water-potential gradient favors outward flow, and turgor falls.
7. **Aperture closure:** The response's extent and timing depend on stimulus, genotype, water status and experimental conditions; no fixed closure time follows from the pathway alone.

The ABA cascade integrates with a parallel **CO$_2$-sensing pathway** (HT1 kinase, MPK4/12) and an **immune pathway** (FLS2 receptor activated by bacterial flagellin) at the level of SLAC1, which serves as a hub for diverse closure stimuli.

```mermaid
flowchart TD
    Drought[Soil drying] --> NCED[NCED3 activated]
    NCED --> ABA[ABA synthesized]
    ABA --> Xylem[Xylem transport to guard cells]
    Xylem --> PYR["PYR/PYL/RCAR receptor (closed gate)"]
    PYR --> PP2C[PP2C phosphatase INHIBITED]
    PP2C --> SnRK2[SnRK2/OST1 kinase ACTIVE]
    SnRK2 --> SLAC[SLAC1: Cl- and nitrate efflux]
    Depol --> GORK[GORK opens: K+ efflux]
    SnRK2 --> RBOH[RBOHF NADPH oxidase: ROS, Ca2+ rise]
    SLAC --> Depol[Membrane depolarized]
    GORK --> Loss[Net solute loss]
    SLAC --> Loss
    Loss --> Water[Water exits via aquaporins]
    Water --> Close[Stomata narrow: condition-dependent timing]
```
<!-- alt: Flowchart showing ABA signaling cascade in guard cells ABA binding releases SnRK2 kinases from PP2C inhibition; SnRK2 then drives the ion-flux changes that osmotically deflate the guard cell. -->

*The ABA signaling cascade in guard cells ABA binding releases SnRK2 kinases from PP2C inhibition; SnRK2 then drives the ion-flux changes that osmotically deflate the guard cell.*

### Other Factors Affecting Stomata

- **CO$_2$ concentration:** Elevated internal CO$_2$ promotes closure (reduces need for gas exchange). This is significant under rising atmospheric CO$_2$, where plants partially close stomata, reducing transpiration but potentially increasing leaf temperature.
- **Humidity:** Low humidity (high vapor pressure deficit, VPD) promotes closure as a protective response against excessive water loss
- **Photosynthetically active radiation (PAR):** Drives opening via both blue-light specific and photosynthesis-dependent pathways
- **Circadian clock:** Stomata show anticipatory opening before dawn, controlled by the plant circadian clock

### Water-Use Efficiency

Stomatal opening trades CO$_2$ acquisition against water loss. The intrinsic water-use efficiency captures this trade-off at the leaf level:

\begin{equation}
iWUE = \frac{A_n}{g_s}
\label{eq:unit_VIII_iwue}
\end{equation}

where $A_n$ is net CO$_2$ assimilation rate (µmol CO$_2$ m$^{-2}$ s$^{-1}$) and $g_s$ is stomatal conductance to water vapor (mol H$_2$O m$^{-2}$ s$^{-1}$). Higher iWUE means more carbon fixed per unit stomatal conductance. Instantaneous water-use efficiency is $A_n/E$, where $E$ is transpiration rate; unlike iWUE, it also depends directly on evaporative demand, including leaf-to-air vapor pressure deficit (VPD).

**C3, C4, and CAM trade-offs:**

- **C3 plants** (rice, wheat, soybean) lack the C4 or CAM CO$_2$-concentrating cycle. Their assimilation and iWUE depend on intercellular CO$_2$, photorespiration, stomatal behavior and measurement conditions, not a pathway-wide numerical range.
- **C4 plants** (maize, sorghum, sugarcane, many tropical grasses) concentrate CO$_2$ in bundle-sheath cells via the C4 pump. Under suitable conditions this can support a given assimilation rate at lower stomatal conductance than in a C3 comparison, but the magnitude depends on species, temperature, light, water status and the comparison design \citep{taylor2018c4water}.
- **CAM plants** (many succulents, cacti, agaves, pineapple) can take up atmospheric CO$_2$ at night, store it as malate and release it internally during the day, permitting reduced daytime stomatal opening. When nighttime VPD is lower, reduced evaporative demand can improve carbon gain per water lost; that effect concerns $A_n/E$ or integrated water use, not an intrinsic increase in $A_n/g_s$ from nighttime timing alone. CAM comparisons require a defined diel accounting interval.

C3, C4 and CAM are alternative photosynthetic strategies, not a universal iWUE or ecological ranking. Controlled grass comparisons support condition-dependent C3–C4 differences \citep{taylor2018c4water}, not a general explanation of maize–wheat competitive outcomes or cactus dominance. Comparisons must specify species, environment, gas-exchange timing and whether the endpoint is intrinsic, instantaneous or integrated water-use efficiency.

**Concept Check 9:** A researcher fumigates a leaf with elevated CO$_2$ while simultaneously illuminating it with blue light. Predict the net effect on stomatal aperture and explain the competing signals at the level of OST1/SLAC1.

**Concept Check 10:** An *ost1* loss-of-function *Arabidopsis* mutant is subjected to drought. Predict its phenotype relative to wild type. What would happen if the same mutant carried a constitutively active SLAC1 transgene?

**Concept Check 11 (Analyze) — Guard-cell ion logic at opening and closing.** In a simplified Arabidopsis model, pump phosphorylation followed by 14-3-3 binding promotes H$^+$-ATPase activation; inward K$^+$ transport and counterion/osmolyte accumulation support water entry and opening. During ABA-induced closure, SLAC1 chloride/nitrate release depolarizes the membrane, favoring outward K$^+$ transport through available GORK channels. (a) For a constructed calculation, stipulate $E_{\mathrm K}=-90$ mV and compare $V_m=-180$ mV with $V_m=-30$ mV. Determine the sign of $V_m-E_{\mathrm K}$ and the favored K$^+$ flux if a conducting pathway is open; distinguish driving force from channel-specific gating. (b) Which measurements are needed to quantify closure impairment in a *slac1* mutant? Explain why genotype plus a 24-hour drought cannot supply a numerical lost fraction. (c) Design matched-solution aperture, voltage and patch-clamp measurements that distinguish loss of depolarizing drive from loss of K$^+$ efflux capacity under imposed depolarization.

**Concept Check 12 (Evaluate) — Endodermal barrier and ion selection.** An intact Casparian strip constrains radial apoplastic entry, but developmental discontinuities and transporter specificity affect actual ion delivery. At 50 mM NaCl irrigation, compare wild type, a strip-defective mutant and a complemented line using matched growth conditions, barrier tracers and xylem Na$^+$:K$^+$ measurements. Which outcomes would distinguish barrier leakage from transporter changes? Why can neither an exact fold change, perfect Na$^+$ exclusion nor a universally lethal/adaptive phenotype be predicted from the mutation alone?


---

## Phloem Transport -- The Münch Pressure-Flow Model

Unlike xylem (upward, driven by transpiration tension), **phloem** transports photosynthate (sucrose at 0.3-0.9 M plus amino acids, [**hormone**](#gl:hormone)s, mRNAs, and small proteins) **bidirectionally** from sources to sinks.

### Phloem Loading — Apoplastic vs Symplastic Pathways

How sugars enter sieve tubes from photosynthetic mesophyll determines key physiological properties: loading rate, concentration limits, and the species-specific tradeoffs between transport efficiency and protection from herbivores. The choice of loading strategy is one of the most striking ecophysiological dichotomies in plants.

**Apoplastic loading** (Type 2; most herbaceous crops, including most major cereals, *Arabidopsis*, sugar beet, soybean, tomato):

1. Sucrose is exported from mesophyll cells to the apoplast (cell-wall space) via **SWEET11/SWEET12** sucrose efflux carriers (uniporters, facilitated diffusion)
2. The H$^+$-ATPase on the companion-cell plasma membrane creates a steep proton gradient (apoplast pH ~5.5; cytoplasm pH ~7.5) and a hyperpolarised membrane potential
3. **SUT1** (Sucrose-H$^+$ symporter; also known as SUC2 in *Arabidopsis*) uses the proton gradient to import sucrose against its concentration gradient (10–50× concentration step). The full family of **sucrose transporters (SUTs)** comprises three clades with distinct cellular localisations and kinetic properties: SUT1/SUC2 is the workhorse loader on companion cells (low $K_m$ ~1 mM); SUT4 localizes to tonoplasts and mediates vacuolar sucrose mobilization; SUT2 has been proposed as a sucrose sensor with high $K_m$. Knockout of *SUT1* in maize (*sut1* mutants) causes sugar accumulation in source leaves and starvation in sinks, confirming its role as the rate-limiting loader.
4. Imported sucrose moves through plasmodesmata between companion cell and sieve element to enter the conducting stream
5. Loading rate: 5–15 µmol sucrose per cm$^2$ of leaf per hour

Apoplastic loading is energetically costly (one ATP per sucrose) but allows very high sieve-tube concentrations (up to 1 M sucrose) by "uphill" transport against the concentration gradient.

**Symplastic loading** (Type 1; many trees, especially temperate broadleaves like willow, poplar; also many tropical species):

1. Sucrose moves from mesophyll to companion cells **predominantly through plasmodesmata**, largely without crossing a membrane (real leaves show some apoplastic leakage even in symplastic loaders). Plasmodesmal density at the mesophyll–companion cell interface is 10–100 × higher in symplastic loaders than in apoplastic loaders. This is the diagnostic anatomical feature of symplastic loading — first established by Gamalei (1989) in his comparative survey of >300 species.
2. In specialized "intermediary cells" (companion-cell variant), sucrose is converted to larger oligosaccharides (raffinose, stachyose) by **galactinol synthase + raffinose synthase**. These larger oligosaccharides cannot diffuse back through the narrow plasmodesmal aperture (~3 nm size limit at the desmotubule).
3. The accumulated raffinose-family oligosaccharides (RFOs) form a one-way **polymer trap** (Turgeon, 1991), lowering $\Psi_s$ and drawing water into the sieve tube.

Symplastic loading is energetically cheap (no membrane transport) but limited in concentration. Some temperate trees (apple, *Malus*) use a third hybrid strategy — passive symplastic loading without polymer trapping, where the source-sink concentration gradient alone drives unloading.

**Plasmodesmatal conductance and regulation:**

Plasmodesmata are dynamic; their aperture is set by the deposition of callose (β-1,3-glucan) at the neck. Callose synthases (CalS1/3/7/8) and β-1,3-glucanases (BG_pap, BG_ppap) act antagonistically. Under stress (wounding, pathogen attack), callose deposition closes plasmodesmata within minutes, isolating affected cells. SUT1-dependent (apoplastic) loading is unaffected by plasmodesmal closure; symplastic loaders are critically dependent on open plasmodesmata and are more vulnerable to wounding-induced flow disruption.

**Comparison across plant groups:**

: Phloem Loading — Apoplastic vs Symplastic Pathways: Loading type and Plant groups. {#tbl:unit_VIII_plant_structure_and_water_phloem_loading_apoplastic_vs_symplastic_pathways}
| Loading type | Plant groups | Plasmodesmata at mesophyll-CC interface | Rate-limiting step | Phloem sap [sucrose] |
| ------------ | ------------ | --------------------------------------- | ------------------ | -------------------- |
| Apoplastic (SUT1) | Most herbaceous crops, cereals, *Arabidopsis*, *Solanum* | Few (<1 per µm$^2$) | SUT1 H$^+$-symport | Up to 1.0 M |
| Symplastic active (polymer trap) | Many temperate broadleaves: *Salix*, *Populus*, *Cucurbita*, *Coleus* | Many (>10 per µm$^2$) | Raffinose synthase rate | 0.3–0.8 M |
| Symplastic passive | Some trees (apple, *Quercus*?) | Many | None (diffusion-limited) | 0.2–0.4 M |

### The Münch Pressure-Flow Hypothesis \citep{munch1930}

Ernst Münch's 1930 model remains the consensus explanation for bidirectional phloem flow, supplemented by ~95 years of experimental refinement.

**Mechanism:**

1. **Sugar loading at source** (mature leaves) raises sucrose concentration in sieve tubes to 0.5–1 M, lowering $\Psi_s$ to $-2$ to $-3$ MPa
2. Water enters by osmosis from adjacent xylem (where Ψ is more positive). Turgor pressure ($\Psi_p$) rises to +1 to +2 MPa at the source
3. **Sugar unloading at sink** (roots, developing fruit, growing tips, storage organs) removes sucrose. Sucrose may be cleaved by invertase (to glucose + fructose) or sucrose synthase. As sucrose is removed, $\Psi_s$ rises, water exits to surrounding tissues, and turgor pressure falls to +0.3 to +0.6 MPa
4. The **pressure gradient** between source (high turgor) and sink (low turgor) drives bulk flow through the sieve-tube network along the path of least resistance
5. The unloaded water re-enters the xylem and is recycled to the source (closing the loop)

**Unloading mechanisms** are sink-specific:

- **Symplastic unloading** (most growing sinks, e.g., root tips, developing leaves): sucrose moves through plasmodesmata into surrounding cells; intracellular sucrose synthase or invertase cleaves it for use.
- **Apoplastic unloading** (storage sinks isolated by suberin, e.g., developing seeds and grains): sucrose is exported by SWEETs into the apoplast, then cleaved by cell-wall invertase to glucose + fructose, which are imported via hexose transporters. The maternal-filial boundary in seeds is typically apoplastic, ensuring genetic isolation between mother plant and developing offspring.

Flow rates: 0.5-1.5 m/h; rates up to 3 m/h have been measured.

**Supporting evidence for Münch flow:**

1. **Aphid-stylet sap collection** (Mittler, 1953): aphids cleanly tap individual sieve tubes; collected sap shows sucrose concentrations of 10–25% w/v, consistent with osmotically active loading
2. **Pressure probes** on individual sieve elements directly measure positive turgor of +1–2 MPa near the source and lower turgor near sinks
3. **Cessation of flow on cooling** the petiole (which inhibits H$^+$-ATPase but does not block plasmodesmata) confirms active loading is required
4. **Source–sink reversal:** Removing the lower leaves of a soybean plant reverses flow direction in the stem (downward to upward) within hours, consistent with passive bulk flow following the pressure gradient
5. **Mathematical modeling** with realistic sieve-tube geometry (Thompson and Holbrook, 2003) shows Münch flow can readily account for observed transport rates in trees up to ~100 m, provided sieve tubes are wide enough

**Evidence against (and modifications to) Münch flow:**

1. The **giant-vine objection** (T.W. Mason, 1922): flow rates in long vines were measured to exceed Münch's predictions for narrow conduits. This was resolved when measurements showed sieve-tube radii in such species are actually larger than initially supposed.
2. **Pressure-driven model alone cannot account for observations of sieve plate occlusion** (P-protein, callose) in healthy phloem, suggesting flow regulation through dynamic plate gating
3. **High-velocity, short-distance flow** in some tropical lianas (>3 m/h) approaches the upper bound of Münch flow and may require a supplementary "relay" mechanism

The current consensus: Münch pressure-flow is the **dominant** mechanism, supplemented by molecular regulators (sieve-plate occlusion, P-protein gating) that fine-tune flow without overturning the basic pressure-driven principle.

> **Clinical Connection:** Girdling (removal of a ring of bark including phloem) causes sugar accumulation above the girdle and starvation below, eventually killing the tree. This principle explains why bark-stripping by elephants, deer, or porcupines can be lethal. Conversely, targeted phloem disruption is used as a management tool to kill invasive tree species.

**Concept Check 11:** Predict the consequence for phloem flow if a chemical inhibitor of the H$^+$-ATPase is locally applied to the source leaf petiole of an apoplastic-loading species. Would the same treatment have the same effect in a symplastic-loading tree?

**Concept Check 12:** A maize *sut1* mutant accumulates sucrose to 200 mM in mesophyll but 10 mM in sieve tubes (wild-type values: 50 mM and 800 mM, respectively). Trace this phenotype through the apoplastic loading pathway and predict the appearance of source leaves and roots.

---

## Nutrient Uptake and Mineral Nutrition

### Essential Mineral Nutrients and Deficiency Logic

Plants require 17 essential elements, divided into macronutrients and micronutrients:

**Macronutrients** (required in large quantities):

: Essential Mineral Nutrients and Deficiency Logic: Element and Symbol. {#tbl:unit_VIII_plant_structure_and_water_essential_mineral_nutrients_and_deficiency_logic}
| Element | Symbol | Primary Functions | Deficiency Symptoms |
| ------- | ------ | ----------------- | ------------------- |
| Nitrogen | N | Amino acids, [**nucleotide**](#gl:nucleotide)s, [**chlorophyll**](#gl:chlorophyll) | Chlorosis (yellowing) of older leaves first |
| Phosphorus | P | ATP, nucleic acids, membranes | Purple/dark green leaves; stunted growth |
| Potassium | K | Osmotic regulation, [**enzyme**](#gl:enzyme) activation, stomata | Marginal leaf necrosis; weak stems |
| Calcium | Ca | Cell wall (middle lamella), signaling | Growing point death; blossom-end rot |
| Magnesium | Mg | Chlorophyll center, enzyme cofactor | Interveinal chlorosis of older leaves |
| Sulfur | S | Cysteine, methionine, coenzyme A | General chlorosis; stunted growth |

**Micronutrients** (required in trace quantities):

: Essential Mineral Nutrients and Deficiency Logic: Element and Symbol. {#tbl:unit_VIII_plant_structure_and_water_essential_mineral_nutrients_and_deficiency_logic_2}
| Element | Symbol | Primary Functions |
| ------- | ------ | ----------------- |
| Iron | Fe | Electron transport, chlorophyll synthesis |
| Manganese | Mn | Photosystem II (water-splitting complex) |
| Boron | B | Cell wall cross-linking, pollen tube growth |
| Zinc | Zn | Enzyme cofactor (carbonic anhydrase, SOD) |
| Copper | Cu | Plastocyanin, lignin biosynthesis |
| Molybdenum | Mo | Nitrate reductase, nitrogenase cofactor |
| Chlorine | Cl | Photosystem II, osmotic regulation |
| Nickel | Ni | Urease cofactor |

### Nitrogen Fixation Symbiosis

Atmospheric N$_2$ is inaccessible to plants directly. Some plants form symbiotic associations with nitrogen-fixing bacteria:

**Rhizobium-legume symbiosis:**

1. Legume roots secrete flavonoids into the rhizosphere
2. Flavonoids activate *nod* genes in *Rhizobium*, producing Nod factors (lipochitooligosaccharides)
3. Nod factors bind NFR1/NFR5 receptors on root hair cells, triggering root hair curling and infection thread formation
4. Bacteria enter root cortex via infection thread, released into host cells, and differentiate into bacteroids within specialized structures called nodules
5. Bacteroids express **nitrogenase** (enzyme complex: Fe-protein + MoFe-protein) which catalyses:

\begin{equation}
N_2 + 8H^+ + 8e^- + 16\text{ATP} \rightarrow 2NH_3 + H_2 + 16\text{ADP} + 16P_i
\label{eq:unit_VIII_nitrogenase}
\end{equation}

6. **Leghemoglobin** (produced by host, gives nodules pink color) maintains low O$_2$ concentration (nitrogenase is irreversibly inhibited by O$_2$) while supplying O$_2$ for bacteroid respiration

The plant provides photosynthate (sucrose, then metabolized to malate/succinate) to the bacteroid; the bacteroid provides fixed nitrogen as NH$_4^+$ or amino acids (alanine, aspartate).

Other nitrogen-fixing associations: *Frankia* (actinobacterium) with alder, bayberry; *Anabaena* with water fern *Azolla* (used as green manure in rice paddies for millennia).

### Mycorrhizal Associations and Nutrient Exchange

**Mycorrhizae** are root–fungus associations that can exchange plant carbon for soil nutrients. Association prevalence requires a source-defined taxonomic denominator; association is not obligatory plant dependence or benefit in every soil. Two major anatomical types are:

**Arbuscular mycorrhizae (AM, Glomeromycota):**
- Obligate plant symbionts; cannot grow without host
- Arbuscules form within cortical-cell walls but remain separated from host cytoplasm by a plant-derived membrane, creating an exchange interface.
- Extraradical hyphae extend several centimetres into soil, accessing a far greater soil volume than roots alone
- Primary benefit: phosphorus delivery (hyphae secrete phosphatases and organic acids to solubilise bound P)
- Plant provides up to 20-30% of photosynthate to fungus
- Found in ~80% of land plant species; ancestral association dating to >400 million years ago

**Ectomycorrhizae (EM, Basidiomycota + Ascomycota):**
- Hyphae form a dense sheath (mantle) around root tips
- **Hartig net:** Hyphae penetrate between cortical cells but do not enter cells
- Provide nitrogen (via proteolytic enzymes that break down soil organic matter) and phosphorus
- Dominant in temperate and boreal forest trees (*Pinus*, *Betula*, *Fagus*, *Quercus*)
- Many EM fungi produce mushrooms (e.g., chanterelles, truffles, *Amanita*)

**Common mycorrhizal networks (CMNs):** Mycorrhizal fungi can connect multiple plants, forming underground networks. Carbon, water, and nutrient signals have been documented moving between plants via these networks, though the ecological significance of active plant-plant signaling through CMNs remains debated.

**Concept Check 13:** A farmer notices that legume crops planted alongside non-legume crops improve the growth of both. Explain the mechanisms by which nitrogen fixed by rhizobia in legume nodules can become available to neighboring non-legume plants.

---

## Adaptations for Water and Nutrient Acquisition

### Xerophyte Adaptations to Water Deficit

Plants in arid environments have evolved numerous strategies to minimize water loss and maximize water uptake:

- **Thick cuticle and epicuticular waxes** (reduce cuticular transpiration)
- **Sunken stomata** in pits or grooves (create humid microenvironment; *Nerium oleander*)
- **Reduced leaf surface area** (needles, spines) or deciduousness during dry season
- **CAM photosynthesis** (stomata open at night, close during day; CO$_2$ stored as malate)
- **Succulence** (water storage in stems or leaves; *Opuntia*, *Aloe*)
- **Deep or extensive root systems** (mesquite roots can reach 50+ m depth)

### Hydrophyte Adaptations to Flooded Environments

Aquatic and wetland plants face the opposite challenge -- too much water and often [**anaerobic**](#gl:anaerobic) substrates:

- **Aerenchyma** (large air-filled cortical spaces for gas transport to submerged roots)
- **Thin or absent cuticle** (CO$_2$ and O$_2$ diffuse directly from water)
- **Dissected or thin leaves** (maximize surface area for gas exchange in water)
- **Adventitious roots** from stem nodes

### Carnivorous Plants and Nutrient Acquisition

In nutrient-poor environments (bogs, sandy soils), some plants supplement mineral nutrition by capturing and digesting insects and other small animals:

- **Pitcher plants** (*Nepenthes*, *Sarracenia*): modified leaves form pitfall traps with slippery surfaces and digestive enzymes
- **Sundews** (*Drosera*): sticky mucilage on tentacle-like trichomes; leaf slowly curls around prey
- **Venus flytrap** (*Dionaea muscipula*): snap trap triggered by touch-sensitive trigger hairs; requires two stimulations within 20 seconds (counting mechanism involves Ca$^{2+}$ signaling)

Most carnivorous plants derive primarily nitrogen and phosphorus from prey.

**Concept Check 14:** Sketch a pressure-flow circuit (source–sink) for a CAM plant during the night when stomata are open. How does CAM-driven nighttime malate accumulation interact with phloem loading dynamics in the same tissue?

---

## Computational Bridge

Whole-cell water potential sums osmotic and pressure components in MPa:

```python
from biology.botany import water_potential

psi = water_potential(0.3, turgor_pressure_MPa=0.5)
print(round(psi.water_potential_MPa, 4))
```

> **Clinical / systems note:** Crop drought breeding screens often proxy cellular osmotic adjustment --- the same $\Psi_s$ shifts you estimate from solute accumulation.

---

## Current Evidence and Frontier Biology: Plant Structure and Water Relations

For **Plant Structure and Water Relations**, frontier biology belongs inside the evidence logic of
the chapter. Plant biology links molecular regulation to climate stress, water limitation, crop resilience, phenology, and ecosystem feedbacks. The core reading question is this: plant-water claims require water potential, hydraulic pathway, stomatal control, tissue anatomy, and stress context.

- **What to verify:** identify the observation, model, assay, or dataset that
  would make the claim stronger or weaker.
- **What to qualify:** state the scale, organism, cell type, environmental
  condition, or population where the claim is expected to hold.
- **What to compare:** test at least one alternative explanation, baseline, or
  null model before treating the pattern as causal.
- **What to cite:** distinguish primary evidence, review synthesis, public
  dataset, and institutional guidance; for recent or numeric claims, prefer
  the source closest to the measurement and state what has changed since it was
  published.

A strong plant-transport claim names the tissue, water-potential component, environmental driver, measurable flow, and tradeoff with growth or defense.

**Source practice:** For plant-water claims, connect anatomy and physiology to water-potential measurements, field context, and growth-reproduction tradeoffs.

Hydraulic safety claims should be benchmarked against comparative vulnerability data and measured operating water potentials \citep{choat2012hydraulicmargins}. P50 denotes the pressure at 50% loss of hydraulic conductivity; it is not necessarily the pressure causing whole-plant death. A safety margin must name both its operating-pressure measure and vulnerability endpoint, rather than treating drought tolerance as binary.

### Current Evidence Map: Hydraulic Safety Tradeoff

```mermaid
flowchart LR
    A["Dry air or soil"] --> B["Lower water potential"]
    B --> C["Stomatal closure"]
    C --> D["Less water loss"]
    C --> E["Less CO2 entry"]
    B --> F["Xylem tension"]
    F --> G["Cavitation risk"]
    D --> H["Survival"]
    E --> I["Lower growth"]
```
<!-- alt: Flowchart showing drought responses should be read as tradeoffs among carbon gain, water loss, hydraulic safety, and growth rather than as simple stress resistance. -->

*Drought responses should be read as tradeoffs among carbon gain, water loss, hydraulic safety, and growth rather than as simple stress resistance.*

## Summary

- **Plant body plan:** Root system (taproot or fibrous) + shoot system (stem + leaves). Phytomers (node + internode + leaf + axillary bud) are the modular building units; plastochron index sets developmental time.
- **Three tissue systems:** Dermal (protection, cuticle, stomata, trichomes), ground (parenchyma for photosynthesis/storage, collenchyma for flexible support, sclerenchyma for rigid support), vascular (xylem: tracheids/vessels for water; phloem: sieve tubes/companion cells for sugars).
- **Xylem development:** Protoxylem (annular/helical, extensible) precedes metaxylem (scalariform/pitted, mechanically robust). Vessels are wider and more efficient than tracheids but more cavitation-prone (Hagen-Poiseuille r⁴ scaling). Conifer pits with torus-margo valves provide most-or-nothing cavitation isolation; angiosperm homogeneous pit membranes are more vulnerable.
- **Water potential:** Full four-component form $\Psi = \Psi_s + \Psi_p + \Psi_m + \Psi_g$ (\cref{eq:unit_VIII_water_potential}) governs direction of water flow; matric potential dominates in dry seeds and soils. The SPAC has a steep gradient driving water from soil ($-0.01$ to $-1.5$ MPa) to atmosphere ($-100$ MPa).
- **Transport pathways:** Apoplastic, symplastic and transmembrane routes operate together. Localized lignified Casparian strips restrict radial apoplastic passage; later suberin lamellae alter transport. Passage cells and lateral-root development modify routes, so membrane selectivity is not perfect exclusion or a universal speed hierarchy.
- **TACT mechanism \citep{dixon1894}:** Transpiration creates tension in xylem; water's cohesive H-bonds maintain continuous column; adhesion to xylem walls supports the column; water rises passively. Critical evaluation: pressure probes, MRI, synthetic-tree experiments, and synchrotron X-ray micro-CT confirm tensions of $-1$ to $-22$ MPa; embolism repair via overnight root pressure and phloem-driven refilling mitigates cavitation losses.
- **Stomatal regulation:** Opening involves phototropin-dependent H$^+$-ATPase activation, inward K$^+$ transport and counterion/osmolyte accumulation; closure involves ABA-PYR-PP2C-SnRK2 signaling, inorganic-anion release, depolarization and GORK-mediated K$^+$ loss. Balances CO$_2$ gain vs water loss; iWUE = $A_n/g_s$ (\cref{eq:unit_VIII_iwue}) differs from VPD-dependent $A_n/E$. C4 CO$_2$ concentration and CAM temporal separation can improve water-use efficiency under specified conditions, but neither implies a universal pathway ranking or competitive outcome.
- **Phloem:** Münch pressure-flow \citep{munch1930} with apoplastic loading (SUT1 cotransporter; herbaceous crops; high sieve-tube concentration) or symplastic loading via polymer trap (raffinose; many trees; many plasmodesmata; lower concentration) at source. Bidirectional flow follows turgor gradient; symplastic vs apoplastic unloading varies by sink type.
- **Nutrient uptake:** Rhizobial nitrogen fixation and mycorrhizal exchange can aid nutrient acquisition. AM and ECM differ anatomically; measured benefit, prevalence and obligatory dependence are separate endpoints requiring defined soil, partner and taxonomic scope.
- **Connections:** See \cref{sec:unit_VIII_plant_reproduction} and \cref{sec:unit_VIII_plant_responses} for reproduction and signaling, \cref{sec:unit_I_water_and_life} for water [**thermodynamics**](#gl:thermodynamics), and \cref{sec:unit_X_biomes_and_conservation} for primary production.

---

## Key Terms

: Current Evidence Map: Hydraulic Safety Tradeoff: Term and Definition. {#tbl:unit_VIII_plant_structure_and_water_current_evidence_map_hydraulic_safety_tradeoff}
| Term | Definition |
| ---- | ---------- |
| **Water potential (Ψ)** | Free energy of water per unit volume; determines direction of water movement; units MPa |
| **Osmotic potential ($\Psi_s$)** | Component of water potential due to solute concentration; typically negative |
| **Turgor pressure ($\Psi_p$)** | Positive pressure exerted by cell contents against the cell wall |
| **Matric potential ($\Psi_m$)** | Component due to water binding on colloidal surfaces; dominant in dry seeds and soils |
| **Casparian strip** | Localized lignified endodermal wall barrier restricting radial apoplastic passage; distinct from later suberin lamellae |
| **Suberin lamella** | Later endodermal wall layer that alters membrane access and radial transport; not the localized strip itself |
| **Passage cell** | Relatively unsuberized endodermal cell that can retain a strip and permit membrane-mediated transport |
| **Cohesion-tension mechanism** | Transpiration-driven water ascent relying on hydrogen bond cohesion |
| **Cavitation** | Formation of gas bubble in xylem under excessive tension |
| **Stomata** | Pores bounded by guard cells; regulate gas exchange and transpiration |
| **Apoplast** | Continuum of cell walls and intercellular spaces |
| **Symplast** | Continuum of cytoplasm connected by plasmodesmata |
| **Tracheids** | Elongated, tapered xylem cells with bordered pits; found in most vascular plants |
| **Vessel elements** | Wide xylem cells with perforation plates; primarily in angiosperms |
| **Bordered pit (torus-margo)** | Conifer pit with thickened central torus suspended in porous margo; valves on cavitation |
| **Protoxylem** | Early xylem with annular/helical thickenings; extensible during organ growth |
| **Metaxylem** | Late xylem with scalariform/pitted thickenings; mechanically robust |
| **Sieve tube elements** | Enucleate phloem cells connected by sieve plates; conduct sugars |
| **Companion cells** | Nucleate cells that metabolically support sieve tube elements |
| **SUT1 (SUC2)** | Sucrose-H$^+$ symporter on companion cells; rate-limiting loader in apoplastic species |
| **SWEET11/12** | Sucrose efflux carriers; export sucrose from mesophyll to apoplast |
| **Polymer trap** | Symplastic loading mechanism using raffinose-family oligosaccharides |
| **Plasmodesmatal conductance** | Bulk transfer rate through plasmodesmata; regulated by callose deposition |
| **Münch pressure-flow** | Model of phloem transport driven by turgor pressure gradient from source to sink |
| **Phytomer** | Modular shoot unit: node + internode + leaf + axillary bud |
| **Plastochron index** | Time interval between successive leaf-primordium initiations |
| **Mycorrhizae** | Root–fungus associations that can exchange plant carbon for nutrients; measured benefit depends on partners and conditions |
| **Arbuscular mycorrhizae** | AM fungi that form arbuscules inside root cortical cells; deliver P |
| **Ectomycorrhizae** | EM fungi that form external mantle and Hartig net; deliver N and P |
| **Nitrogenase** | Enzyme complex in nitrogen-fixing bacteria; converts N$_2$ to NH$_3$ |
| **Aquaporins** | Water channel proteins (PIP, TIP families) in plant cell membranes |
| **OST1/SnRK2.6** | Master kinase of guard-cell ABA response; phosphorylates SLAC1 |
| **iWUE (intrinsic WUE)** | $A_n/g_s$; net CO$_2$ assimilated per unit stomatal conductance |

---

## Review Questions

1. A plant cell has a solute concentration of 0.4 M, turgor pressure of 0.3 MPa, and is at ground level. Using $\Psi_s = -iCRT$ with $i = 1$, $R = 0.00831$ L MPa mol$^{-1}$ K$^{-1}$, and $T = 298$ K, calculate the total water potential. If this cell is adjacent to another cell with $\Psi = -0.5$ MPa, which direction will water flow?

2. Explain why xylem vessels are more efficient than tracheids for water transport but also more vulnerable to cavitation. What structural features of tracheids (torus-margo pits) help prevent the spread of embolisms? Contrast with angiosperm pit membranes.

3. Describe the complete pathway of a water molecule from the soil solution to the atmosphere, naming each structure it passes through. At which points must the molecule cross a cell membrane?

4. Compare apoplastic and symplastic phloem loading. Which is more common in herbaceous crop plants? What is the energetic cost of each, and why might symplastic loading be advantageous in some environments? Cite SUT1 and the polymer-trap mechanism in your answer.

5. A farmer observes that phosphorus-deficient plants show improved growth when inoculated with arbuscular mycorrhizal fungi but not when given additional phosphorus fertiliser alone. Explain this observation in terms of the spatial distribution of phosphorus in soil and the relative surface area of roots vs mycorrhizal hyphae.

6. Explain how the Casparian strip (lignin) and suberin lamella of the endodermis act as a quality control checkpoint. What would happen to plant ion [**homeostasis**](#gl:homeostasis) if the Casparian strip were absent? What is the role of passage cells in older roots? Account for apoplastic bypasses at lateral root emergence sites.

7. During a heat wave, a crop plant simultaneously experiences high temperatures (stomatal opening signal from photosynthesis demand) and soil drying (ABA-mediated stomatal closure signal). Trace the molecular competition between these signals at the level of OST1/SLAC1 in guard cells and predict which typically dominates.

8. Compare and contrast water movement in xylem and phloem in terms of: driving force, direction, conducting cell viability, and substances transported.

9. Describe the nitrogen fixation symbiosis between *Rhizobium* and legumes. Why must nitrogenase be protected from oxygen, and how does the nodule accomplish this?

10. A coast redwood (*Sequoia sempervirens*) is 100 m tall. Calculate the gravitational component of water potential at the top of the tree. Given that atmospheric Ψ can reach $-100$ MPa at 50% humidity, explain why the tree can still pull water to the canopy.

11. Critically evaluate the cohesion-tension theory \citep{dixon1894}. Identify two lines of evidence supporting it (including synchrotron imaging) and one historical objection that has been resolved. What is the air-seeding hypothesis, and how does it apply to torus-margo pits?

12. Using `transpiration_flux`, predict whether doubling stomatal conductance doubles water loss if the leaf-to-air vapor gradient is held fixed. Then compute the iWUE consequence assuming $A_n$ saturates at 80% of the doubled $g_s$.

13. Contrast **hydraulic redistribution** via roots with capillary rise in soil --- when does each dominate overnight water status?

14. Use the Hagen-Poiseuille equation \cref{eq:unit_VIII_hagen_poiseuille} to estimate the relative volumetric flow capacity of a 200-µm vessel versus a 30-µm tracheid (same length and pressure gradient). How does this calculation explain the prevalence of vessels in fast-transpiring angiosperms?

15. In a stipulated noon comparison, a C3 wheat leaf has iWUE of 80 µmol CO$_2$ mol$^{-1}$ H$_2$O and a C4 maize leaf has iWUE of 200, with equal $A_n$. Calculate their relative $g_s$. Why does this ratio alone establish neither relative $A_n/E$ without evaporative-demand information nor competitive superiority in a semi-arid environment? What species, environmental and diel measurements would be needed?

---


## Further Reading and Source Notes: Plant Structure and Water Relations

- \citet{dixon1894} — On the ascent of sap. *Philosophical Transactions of the Royal Society B*, 186.
- \citet{munch1930} — Die Stoffbewegungen in der Pflanze. *Gustav Fischer Verlag*.

---

## Companion Source Module: Plant Structure and Water Relations

**Plant Structure and Water Relations** should leave a reproducible trail from a biological claim to
the code, figure, diagram, or paper-based activity that can test it. Use the
surfaces below to inspect the chapter's assumptions, rerun the relevant model,
or compare the manuscript explanation with companion labs and figures.

: Companion source surfaces for Plant Structure and Water Relations. {#tbl:unit_VIII_plant_structure_and_water_companion_source_surfaces}
| Surface | Use it for |
| --- | --- |
| `src/biology/botany/botany.py` (`water_potential`, `transpiration_flux`) | Reproduce plant-water calculations and hydraulic tradeoffs. |
| `src/biology/cell/cell_biology.py` (`osmotic_pressure`) | Connect cellular osmotic pressure to tissue-level water movement. |
| `src/visualization/plots.py` (`plot_light_response_curve`) | Practice graph interpretation for environmental-response curves. |

**Reproducibility check:** list solute potential, pressure potential, tissue, humidity, temperature, and stomatal state before predicting water movement. **Cross-reference:** use \cref{sec:unit_I_water_and_life} and \cref{sec:unit_VIII_plant_responses}.
