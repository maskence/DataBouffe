<template>
  <div>
    <layout-page-header>
      <div class="header-container">
        <div style="box-sizing: inherit">
          <h1 class="header-title">Dashboard</h1>
          <p class="header-sub-title">
            Maxence, Keep track of your progress
          </p>
        </div>
      </div>
    </layout-page-header>
    <div class="main-card">
      <div v-for="(day, index) in weekDays" :key="index" class="day-card">
        <div class="day-title">
          <h1>{{ day.name }}</h1>
        </div>
        <div>{{ day.mealCount }} repas - {{ day.calories }} kcal</div>
        <div class="day-meal-container">
          <div
            v-for="(meal, mealIndex) in day.meals"
            :key="mealIndex"
            class="meal-card"
          >
            {{ meal }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const weekDays = [
  {
    name: "Lundi",
    mealCount: 3,
    calories: 1800,
    meals: ["Repas 1", "Repas 2", "Repas 3"],
  },
  {
    name: "Mardi",
    mealCount: 3,
    calories: 1900,
    meals: ["Repas 1", "Repas 2", "Repas 3"],
  },
  {
    name: "Mercredi",
    mealCount: 3,
    calories: 2000,
    meals: ["Repas 1", "Repas 2", "Repas 3"],
  },
  {
    name: "Jeudi",
    mealCount: 3,
    calories: 1800,
    meals: ["Repas 1", "Repas 2", "Repas 3"],
  },
  {
    name: "Vendredi",
    mealCount: 3,
    calories: 1700,
    meals: ["Repas 1", "Repas 2", "Repas 3"],
  },
  {
    name: "Samedi",
    mealCount: 3,
    calories: 2000,
    meals: ["Repas 1", "Repas 2", "Repas 3"],
  },
  {
    name: "Dimanche",
    mealCount: 3,
    calories: 1900,
    meals: ["Repas 1", "Repas 2", "Repas 3"],
  },
];
</script>

<style scoped>
.meal-card {
  border: 2px #38a388 solid;
  width: 100%;
  margin-top: 5px;
}

.day-card {
  width: 22%; /* Set the width to 25% to fit four items in a row */
  box-sizing: border-box; /* Include padding and border in the width */
  border: 1px solid #ddd; /* Add a border for better visibility */
  padding: 10px; /* Add padding to create space between items */
  text-align: center; /* Center the content */
  margin: 5px; /* Add margin for space between items */
  background: #fff;
}

.day-title {
  padding: 10px;
  background-color: #38a388 !important;
  color: #fff;
  text-align: center;
}

.main-card {
  display: flex;
  flex-wrap: wrap; /* Allow items to wrap into a new row if needed */
  width: 100%;
  gap: 48px;
}
</style>
