<template>
    <div>
      <h1>Test Re-Draw</h1>
      <button :onClick="changeData" style="width: 100%">Change Data</button>
      <button :onClick="changeLayout" style="width: 100%">Change Layout</button>
      <button :onClick="changeConfig" style="width: 100%">Change Config</button>
      <nuxt-plotly
        :data="pieChart.data"
        :layout="pieChart.layout"
        :config="pieChart.config"
        style="width: 100%"
      ></nuxt-plotly>
    </div>
  </template>
  
  <script setup>
  import { reactive } from 'vue';
  const data = [
    [
      {
        values: [19, 26, 55],
        labels: ['Residential', 'Non-Residential', 'Utility'],
        type: 'pie',
      },
    ],
    [
      {
        values: [16, 15, 12, 6, 5, 4, 42],
        labels: [
          'US',
          'China',
          'European Union',
          'Russian Federation',
          'Brazil',
          'India',
          'Rest of World',
        ],
        domain: { column: 0 },
        name: 'GHG Emissions',
        hoverinfo: 'label+percent+name',
        hole: 0.4,
        type: 'pie',
      },
      {
        values: [27, 11, 25, 8, 1, 3, 25],
        labels: [
          'US',
          'China',
          'European Union',
          'Russian Federation',
          'Brazil',
          'India',
          'Rest of World',
        ],
        text: 'CO2',
        textposition: 'inside',
        domain: { column: 1 },
        name: 'CO2 Emissions',
        hoverinfo: 'label+percent+name',
        hole: 0.4,
        type: 'pie',
      },
    ],
  ];
  
  const layout = [
    {
      title: '[layout0] Pie Chart on `PieChart.client.vue`',
    },
    {
      title: '[layout1] Pie Chart on `PieChart.client.vue`',
      showlegend: false,
    },
  ];
  
  const config = [
    { scrollZoom: true, displayModeBar: true },
    { scrollZoom: false, displayModeBar: false },
  ];
  
  const pieChart = reactive({
    changeDataNo: 1,
    data: data[0],
    changeConfigNo: 1,
    config: config[0],
    changeLayoutNo: 1,
    layout: layout[0],
  });
  
  function changeData() {
    pieChart.data = data[pieChart.changeDataNo];
    pieChart.changeDataNo = pieChart.changeDataNo == 1 ? 0 : 1;
  }
  
  function changeLayout() {
    pieChart.layout = layout[pieChart.changeLayoutNo];
    pieChart.changeLayoutNo = pieChart.changeLayoutNo == 1 ? 0 : 1;
  }
  
  function changeConfig() {
    pieChart.config = config[pieChart.changeConfigNo];
    pieChart.changeConfigNo = pieChart.changeConfigNo == 1 ? 0 : 1;
  }
  </script>
  