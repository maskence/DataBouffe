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
      <div v-for="(today_meals, day_index) in meals" class="day-card">
        <div class="day-title">
          <h1>{{ week_days[day_index % week_days.length] }}</h1>
        </div>
        <div>{{ Math.floor(today_meals.reduce( (acc : number, val : any) => acc + val.nutrients.kcal,0) * 5)}} kcal</div>
        <div v-for="(meal_place, i) in meals_in_day" class="day-meal-container">
            <p> {{ meal_place }}</p>
            <div class="meal-card">
              {{ today_meals[i].name}}
            </div>
        </div>
        </div> 
      </div>
    </div> 
</template>

<script setup lang="ts">
import { get_meal_plan } from '~/lib';


const week_days = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
const meals_in_day = ["midi","dinner"]

const meals = ref<any[]>([])
onMounted(async () => {
  const all_meals = await get_meal_plan()

  //bunch the list of meals received from the api into days, this will probably be done serverside once the algorithm is more evolved
  for (let i = meals_in_day.length; i<=all_meals.length; i+=meals_in_day.length) {
    meals.value.push(all_meals.slice(i-meals_in_day.length,i))
  }
})

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
