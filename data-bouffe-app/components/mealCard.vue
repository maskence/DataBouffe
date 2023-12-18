<template>
    <div class="meal-card">
      <h2>{{ mealData }}</h2>
      <p><strong>Date:</strong> {{ date }}</p>
      <div class="nutritional-info">
        <p><strong>Protein:</strong> {{ mealStats.protein }}</p>
        <p><strong>Carbohydrate:</strong> {{ mealStats.carbohydrate }}</p>
        <p><strong>Fat:</strong> {{ mealStats.fat }}</p>
        <p><strong>Fiber:</strong> {{ mealStats.fiber }}</p>
        <p><strong>Vitamin C:</strong> {{ mealStats.vitamin_c }}</p>
        <p><strong>Kcal:</strong> {{ mealStats.kcal }}</p>
      </div>
      <div class="recipe">
        <h3>Recipe:</h3>
        <ul>
          <li v-for="(ingredient, index) in recipe" :key="index">{{ ingredient }}</li>
        </ul>
      </div>
    </div>
  </template>
  
<script setup>
import { ref, onMounted } from 'vue';
import mealData from '~/store/mealExample.json';

// Props are defined using the defineProps function
const props = defineProps({
  mealIndex: Number,
  dayIndex: Number,
});

const mealLabel = ref('');
const date = ref('');
const mealStats = ref({});
const recipe = ref([]);

onMounted(() => {
  const meal = mealData.week[props.dayIndex].meals[props.mealIndex];

  mealLabel.value = meal.meal_label;
  date.value = meal.date;
  mealStats.value = meal.meal_nut_stats;
  recipe.value = meal.recipe;
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
  