<template>
  <div>
    <layout-page-header>
      <div class="header-container">
        <div style="box-sizing: inherit">
          <h1 class="header-title">Today's Meal</h1>
          <p class="header-sub-title">
            Maxence, Keep track of your daily meal plan
          </p>
        </div>
        <Calendar class="calendar" v-model="selectedDate" showIcon></Calendar>
      </div>
    </layout-page-header>

    <div class="main-card">
      <div class="meal-card">
        <h1 class="daily-title">Year Daily Meal Plan</h1>
        <div v-for="day in week" :key="day.date" class="day-container">
          <div v-if="day.date === formatDate(selectedDate)" style="width: 100%">
            <div
              v-for="meal in day.meals"
              :key="meal.meal_label"
              @click="handleMealClick(meal)"
              :class="{
                'meal-container': true,
                'selected-meal': meal.meal_type === selectedMealType,
              }"
            >
              <div>
                <h2 class="meal-label">{{ meal.meal_label }}</h2>
                <h2 class="meal-info">
                  {{ meal.meal_type }} - Végétarien - Français
                </h2>
                <div class="information-container">
                  <div class="nutritional-info">
                    <p>
                      <strong>Protein:</strong>
                      {{ meal.meal_nut_stats.protein }}
                    </p>
                    <p>
                      <strong>Carbohydrate:</strong>
                      {{ meal.meal_nut_stats.carbohydrate }}
                    </p>
                    <p><strong>Fat:</strong> {{ meal.meal_nut_stats.fat }}</p>
                    <p>
                      <strong>Fiber:</strong> {{ meal.meal_nut_stats.fiber }}
                    </p>
                    <p><strong>Kcal:</strong> {{ meal.meal_nut_stats.kcal }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="meal-info-card">
        <div class="meal-info-container">
          <h1 class="meal-label border-title-info">Apport journalier</h1>
          <div class="table-container">
            <p>OUI OUI OUI</p>
          </div>
        </div>
        <div class="meal-container">
          <h1 class="meal-label border-title-info">Recette</h1>
          <div>
            <section class="recipe-section">
              <p class="recipe-subtitle">Ingredients</p>
              <ul class="recipe-list">
                <li
                  v-for="(ingredient, index) in ingredients"
                  :key="index"
                  class="recipe-item"
                >
                  {{ ingredient }}
                </li>
              </ul>
            </section>

            <section class="recipe-section">
              <p class="recipe-subtitle">Tools</p>
              <ul class="recipe-list">
                <li
                  v-for="(tool, index) in tools"
                  :key="index"
                  class="recipe-item"
                >
                  {{ tool }}
                </li>
              </ul>
            </section>

            <section class="recipe-section">
              <p class="recipe-subtitle">Time</p>
              <p class="recipe-time">Cooking Time: {{ cookingTime }}</p>
              <p class="recipe-time">Preparation Time: {{ preparationTime }}</p>
            </section>

            <section class="recipe-section">
              <p class="recipe-subtitle">Steps</p>
              <ol class="recipe-ordered-list">
                <li
                  v-for="(step, index) in steps"
                  :key="index"
                  class="recipe-item"
                >
                  {{ step }}
                </li>
              </ol>
            </section>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const ingredients: string[] = ["Ingredient 1", "Ingredient 2", "Ingredient 3"];
const tools: string[] = ["Tool 1", "Tool 2", "Tool 3"];
const cookingTime: string = "30 minutes";
const preparationTime: string = "15 minutes";
const steps: string[] = [
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
  "Nulla facilisi. Sed vel odio at justo aliquam bibendum.",
  "Proin aliquet purus vel tortor fringilla, vitae tristique libero venenatis.",
];

let selectedMealType = ref<string | null>(null);

function handleMealClick(meal: any): void {
  // Set the selected meal type when a meal card is clicked
  selectedMealType.value = meal.meal_type;
}

const selectedDate = ref(new Date());

function formatDate(date: Date): string {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");

  return `${year}-${month}-${day}`;
}

import mealData from "~/store/mealExample.json";

const week = ref(mealData.week);
</script>

<style>
.recipe-details {
  font-family: "Arial", sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
}

.recipe-header {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 1em;
}

.recipe-section {
  margin: 20px auto;
  padding: 20px;
}

.recipe-subtitle {
  font-size: 16px;
  font-weight: 800;
  color: #333;

}

.recipe-list {
  list-style-type: none;
  padding: 0;
}

.recipe-item {
  margin-bottom: 8px;
}

.recipe-time {
  color: #555;
}

.recipe-ordered-list {
  list-style-type: decimal;
  margin-left: 20px;
}

.recipe-footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 1em;
  position: fixed;
  bottom: 0;
  width: 100%;
}

.recipe-copyright {
  margin: 0;
}

.meal-info-container {
  padding: 24px;
  margin-bottom: 15px;
  border-bottom: 1px solid #ccc;
  background: #fff;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
  border-radius: 4px;
}

.border-title-info {
  border-bottom: 1px solid #38a388;
}

.table-container {
  margin-top: 16px;
  width: 100%;
}

.meal-info-card {
  width: 70%;
  padding: 24px;
  margin-top: 60px;
}

.header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;

  max-width: 1440px;
  width: 100%;
}
.main-card {
  display: flex;
  flex-direction: row;
  padding: 24px;
}

.calendar {
  order: 1;
}

.header-title {
  color: #302f2f;
  font-size: 28px;
  font-weight: 600;
}

.daily-title {
  color: #38a388;
  font-size: 26px;
  font-weight: 800;
}

.header-sub-title {
  color: #605e5e;
  font-size: 12px;
  font-weight: 400;
}

.meal-card {
  width: 30%;
  padding: 24px;
}

.day-container {
  display: flex;

  margin-bottom: 20px;
  margin-top: 20px;
  padding-bottom: 20px;
}

.day-date {
  font-size: 1.2em;
  margin-bottom: 10px;
}

.meal-container {
  padding: 12px;
  margin-bottom: 15px;
  border-bottom: 1px solid #ccc;
  background: #fff;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
  border-radius: 4px;
}

.selected-meal {
  /* Add your styles for the selected meal card here */
  padding: 12px;
  margin-bottom: 15px;
  border-bottom: 1px solid #ccc;
  background: #fff;
  box-shadow: 0px 0px 15px -3px rgb(56, 163, 136);
  border-radius: 4px;
}

.meal-label {
  font-size: 20px;
  font-weight: 600;
  color: #006761;
}

.meal-info {
  font-size: 12px;
  font-weight: 400;
  color: #605e5e;
}

.recipe-list {
  list-style-type: none;
  padding: 0;
}

.recipe-list li {
  margin-bottom: 5px;
  color: #555;
}

.information-container {
  padding: 12px;
}

.nutritional-info {
  display: flex;
  flex-direction: row;
  margin-bottom: 10px;
  font-size: 12px;
}
</style>
