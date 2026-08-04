---
title: Mapping/GIS
hide:
  - title
---

<div class="uc-hero" markdown>
__Under construction__
{ .uc-title }

This page is an active work in progress. The story map and Town Hall recording are still in development, publication lists are placeholders, and content and figures may change without notice. Please do not cite or circulate this page yet.
</div>

# Mapping the Geography of ALS

A growing collection of ALS TDI tools, data, and reading on where people with ALS live, what they are exposed to, and how place shapes disease risk and outcomes. These resources are assembled to support researchers, clinicians, and the ALS community.

---

## ALS TDI geospatial resources

<div class="grid cards" markdown>

-   __ALS Geospatial Story Map__

    ---

    An interactive narrative walking through ALS geographic patterns and environmental context. Currently in development.

    [:octicons-arrow-right-24: Preview below](#als-geospatial-story-map)

-   __Town Hall Recording__

    ---

    Recording of the ALS TDI community town hall on geospatial research and ALS, embedded here once the event has taken place.

    [:octicons-arrow-right-24: Watch below](#town-hall-recording)

-   __GeoALS__

    ---

    A nonprofit GIS platform that uses mapping to improve care, accelerate research, and advocate for the ALS community. ALS TDI partners with GeoALS on place-history research using ARC data.

    [:octicons-arrow-right-24: Visit GeoALS](https://www.geoals.org/)

-   __ALS Geospatial Hub__

    ---

    Authoritative data from federal agencies, research institutions, and nonprofit organizations, organized by geography.

    [:octicons-arrow-right-24: Open the Hub](https://als-geospatial-hub-nonprofit.hub.arcgis.com/)

</div>

---

## ALS Geospatial Story Map

A preview of the story map will live here as it comes together.

<div class="map-placeholder" markdown>
Preview image or live map will appear here once the story map is ready.
</div>

<!--
  When the story map is ready, replace the div above with ONE of these.

  Option A, static preview image:
  ![Preview of the ALS Geospatial Story Map](assets/geospatial/story-map-preview.jpg)

  Option B, live embed:
  <div class="video-embed">
    <iframe src="ARCGIS_STORYMAP_EMBED_URL" title="ALS Geospatial Story Map" allowfullscreen></iframe>
  </div>
-->

---

## Town hall recording

The recording of the ALS TDI community town hall on geospatial research and ALS will be embedded here, playable directly on this page, once the event has taken place.

<div class="map-placeholder" markdown>
Recording will appear here after the event.
</div>

<!--
  When the recording is ready, replace the div above with:

  <div class="video-embed">
    <iframe src="RECORDING_EMBED_URL" title="ALS TDI Geospatial Research Town Hall" allowfullscreen></iframe>
  </div>
-->

---

## ARC cohort geography

Place-based context complements the ALS TDI risk factor work. These maps are produced through the GeoALS and ALS TDI collaboration, and are discussed in full on the [ALS Risk Factors page](risk-factors-vs-population.md#geography-who-the-cohort-is-and-how-they-reach-care).

**Neighborhood tapestry of ARC participants.** Tapestry segments classify U.S. neighborhoods by shared demographic and socioeconomic profile, for example "Boomburbs" or "Metro Renters". Mapping the cohort this way characterizes who is enrolling.

![Dominant Esri Tapestry segments of ARC participants](assets/risk-factors/arc-tapestry-segments.png)

**Drive time to ALS clinical care.** Only about 13% of ARC participants live 90 minutes or more from an ALS clinic. Travel burden shapes who reaches specialty care, and so shapes ascertainment.

![30, 60, and 90 minute drive times to ALS clinics with ARC participants beyond 90 minutes](assets/risk-factors/arc-drive-time-to-clinics.png)

---

## Publications and further reading

### ALS TDI publications and education

<!-- Add ALS TDI papers, posters, and training materials here. -->

- *[Publication title]* - Author(s), Journal, Year
- *[Publication title]* - Author(s), Journal, Year

See also the full [Select Publications](select-publications.md) list.

### Background reading

<!-- Add outside articles and explainers on environmental health, geospatial methods, and ALS epidemiology here. -->

- Besse, H. and Rojas-Rueda, D. (2025). Environmental justice mapping tools in the United States: A review of national and state tools. *Science of the Total Environment, 962*, 178449. <https://doi.org/10.1016/j.scitotenv.2025.178449>
- *[Article title]* - Source, Year

---

## Publicly available environmental health data

A field guide to existing environmental health mapping tools, drawn from Besse and Rojas-Rueda's 2025 review in *Science of the Total Environment*, which catalogued 25 publicly available tools nationwide: 6 national and 19 state.

!!! danger "Several federal tools were removed in 2025"
    EJScreen, the Climate and Economic Justice Screening Tool (CEJST), and the Equitable Transportation Community Explorer were taken off federal websites in early 2025. Links below point to independent reconstructions maintained by the Public Environmental Data Partners coalition and to archived data. Confirm provenance and version before citing any of these in published work.

<div class="eht-controls">
  <input
    type="text"
    id="eht-search"
    class="ga4gh-search-input"
    placeholder="Search by tool, agency, state, or geographic unit"
  />
  <div class="eht-scale-filter">
    <button class="eht-scale-btn active" data-scale="all">All</button>
    <button class="eht-scale-btn" data-scale="national">National</button>
    <button class="eht-scale-btn" data-scale="state">State</button>
    <span id="eht-count" class="eht-count"></span>
  </div>
</div>

<div class="ga4gh-table-wrapper">
  <table id="eht-table" class="md-typeset__table">
    <thead>
      <tr>
        <th>Tool</th>
        <th>Coverage</th>
        <th>Indicators</th>
        <th>Geographic unit</th>
        <th>Updated</th>
      </tr>
    </thead>
    <tbody>
      <tr><td colspan="5" class="eht-loading">Loading tools...</td></tr>
    </tbody>
  </table>
</div>

Source data are in [`env-health-tools.csv`](assets/env-health-tools.csv). States not listed did not have a publicly available environmental health mapping tool meeting the review's criteria as of January 2024.

---

## Collaborate with us

ALS TDI welcomes collaboration on geospatial and environmental health research in ALS. If you have a data set, a mapping capability, a research question, or a community partnership to propose, we would like to hear from you.

<div class="collab-card" markdown>

__Get in touch with Hannah Walters, MPH, DrPH__

Scientist, ALS Therapy Development Institute

[:octicons-mail-24: hwalters@als.net](mailto:hwalters@als.net?subject=Geospatial%20research%20collaboration&body=Name%3A%0AOrganization%3A%0ARole%3A%0A%0AWhat%20you%20would%20like%20to%20collaborate%20on%3A%0A%0AData%2C%20tools%2C%20or%20geographies%20involved%3A%0A%0AAnything%20else%20we%20should%20know%3A%0A){ .md-button .md-button--primary }

The link opens an email with these prompts already filled in:

- Name, organization, and role
- What you would like to collaborate on
- Data, tools, or geographies involved
- Anything else we should know

</div>

---

## Sources

Tool status and links were verified in August 2026 against the following:

- Besse, H. and Rojas-Rueda, D. (2025), *Science of the Total Environment*: <https://doi.org/10.1016/j.scitotenv.2025.178449>
- Environmental Data and Governance Initiative, EPA removes EJScreen: <https://envirodatagov.org/epa-removes-ejscreen-from-its-website/>
- Harvard Environmental and Energy Law Program, CEJST removed: <https://eelp.law.harvard.edu/tracker/ceqs-climate-economic-justice-screening-tool-removed/>
- Public Environmental Data Partners, Data and Screening Tools: <https://screening-tools.com/>
- Individual agency pages for each state tool, linked in the table above
