<template>
  <div>
    <layout-page-header>
      <div class="header-container">
        <div style="box-sizing: inherit">
          <h1 class="header-title">Meal Calendar</h1>
          <p class="header-sub-title">
            Maxence, Keep track of your daily meal plan
          </p>
        </div>
        <Calendar
          class="calendar"
          v-model="selectedDate"
          view="week"
          showIcon
        ></Calendar>
      </div>
    </layout-page-header>
    <div>
      <h1  class="daily-title">Your progress</h1>
      <div class="main-card">
        <div class="graph-card">
          <client-only>
            <nuxt-plotly
              :data="data"
              :layout="layout"
              :config="config"
              style="width: 100%"
              @on-ready="myChartOnReady"
            ></nuxt-plotly>
          </client-only>
        </div>
        <div class="graph-card">
          <client-only>
            <nuxt-plotly
              :data="dataBar"
              :layout="layoutBar"
              :config="configBar"
              style="width: 100%"
              @on-ready="myChartOnReady"
            ></nuxt-plotly>
          </client-only>
        </div>
      </div>
      <!-- <pie-chart></pie-chart> -->
    </div>
  </div>
</template>

<script setup lang="ts">
import type {
  NuxtPlotlyData,
  NuxtPlotlyLayout,
  NuxtPlotlyConfig,
  NuxtPlotlyHTMLElement,
} from "nuxt-plotly";

/* First Graph */

const years = [2010, 2011, 2012, 2013, 2014];
const weight = [70, 72, 68, 75, 73];
const kcalConsumed = [2500, 2600, 2400, 2700, 2600];

// Utilisez "scatter" comme type pour un graphique en ligne
const data: NuxtPlotlyData = [
  {
    x: years,
    y: weight,
    type: "scatter",
    mode: "lines",
    name: "Poids (kg)",
    marker: { color: "blue" },
  },
  {
    x: years,
    y: kcalConsumed,
    type: "scatter",
    mode: "lines",
    name: "kcal consommées",
    yaxis: "y2",
    marker: { color: "green" },
  },
];

const layout: NuxtPlotlyLayout = {
  title: "Évolution du Poids et de la Consommation de kcal",
  xaxis: { title: "Année" },
  yaxis: { title: "Poids (kg)" },
  yaxis2: {
    title: "kcal consommées",
    overlaying: "y",
    side: "right",
  },
};

const config: NuxtPlotlyConfig = {
  responsive: true,
};

/* BarChart */

const carbohydrates = [150, 160, 140, 130, 120];
const lipids = [80, 90, 85, 75, 70];
const proteins = [60, 70, 65, 75, 80];

// Utilisez "bar" comme type pour un graphique en barres
const dataBar: NuxtPlotlyData = [
  {
    x: years,
    y: carbohydrates,
    type: "bar",
    name: "Glucides",
    marker: { color: "blue" },
  },
  {
    x: years,
    y: lipids,
    type: "bar",
    name: "Lipides",
    marker: { color: "green" },
  },
  {
    x: years,
    y: proteins,
    type: "bar",
    name: "Protéines",
    marker: { color: "orange" },
  },
];

const layoutBar: NuxtPlotlyLayout = {
  title: "Évolution de la Consommation des Nutriments (moyenne par repas)",
  xaxis: { title: "Année" },
  yaxis: { title: "Quantité (g)" },
  barmode: "group", // Utilisez "stack" si vous souhaitez empiler les barres
};

const configBar: NuxtPlotlyConfig = {
  responsive: true,
};

function myChartOnReady(plotlyHTMLElement: NuxtPlotlyHTMLElement) {
  const { $plotly } = useNuxtApp();
  console.log({ $plotly });
  console.log({ plotlyHTMLElement });

  plotlyHTMLElement.on?.("plotly_afterplot", function () {
    console.log("done plotting");
  });

  plotlyHTMLElement.on?.("plotly_click", function () {
    alert("You clicked this Plotly chart!");

    // use plotly function via `$plotly` to download chart image
    $plotly.downloadImage(plotlyHTMLElement as HTMLElement, {
      format: "png",
      width: 800,
      height: 600,
      filename: "newplot",
    });
  });
}
</script>

<style scoped>
.graph-card {
  background: #fff;
  border-radius: 15px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
  padding: 24px;
}
.main-card {
  display: flex;
  flex-wrap: wrap; /* Allow items to wrap into a new row if needed */
  width: 100%;
  gap: 48px;
}

.daily-title {
  color: #38a388;
  font-size: 26px;
  font-weight: 800;
  padding: 24px;
}
</style>
