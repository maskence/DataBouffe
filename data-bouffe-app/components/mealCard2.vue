<template>
    <div class="meal-card">
      <h2>{{ meal.name }}</h2>
      <div class="nutritional-info" v-for="(value, key) in meal.nutrients" :key="key">
        <p><strong>{{  key  }} : </strong> {{ value }}</p>
      </div>
      <!-- add recipe later when its added to the api -->
    </div>
  </template>
  
<script setup>
const props = defineProps({
  meal : Object
});
</script>
  
  <style scoped>
  /* Add your styling here */
  .meal-card {
    border: 1px solid #ddd;
    padding: 16px;
    margin: 16px;
  }
  
  .nutritional-info {
    margin-top: 16px;
  }
  
  .recipe {
    margin-top: 16px;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    margin-bottom: 8px;
  }
  </style>
  