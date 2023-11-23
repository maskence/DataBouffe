<!-- components/TabsBarWeek.vue -->
<template>
  <div class="tabs-bar">
    <div @click="goToPreviousWeek" class="arrow">&#9664;</div>
    <div v-for="day in days" :key="day.value" @click="selectDay(day)" :class="{ active: day.value === selectedDay.value }">
      <span>{{ day.name }}</span>
      <span>{{ day.number }}</span>
      <span>{{ day.month }}</span>
    </div>
    <div @click="goToNextWeek" class="arrow">&#9654;</div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

const days = ref([]);
const selectedDay = ref({});

const weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

const formatDate = (date) => {
  const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  const formattedDate = new Date(date).toLocaleDateString('en-US', options);

  const [dayName, fullDate] = formattedDate.split(',');
  const [month, day, year] = fullDate.trim().split(' ');

  return {
    name: dayName.trim(),
    number: day,
    month: month,
  };
};

onMounted(() => {
  const currentDate = new Date();
  days.value = weekdays.map((day, index) => {
    const date = new Date(currentDate);
    date.setDate(currentDate.getDate() - currentDate.getDay() + index);

    const formatted = formatDate(date);
    return {
      name: formatted.name,
      number: formatted.number,
      month: formatted.month,
      value: index,
    };
  });

  // Set the default selected day to today
  selectedDay.value = days.value[currentDate.getDay()];
});

const selectDay = (day) => {
  selectedDay.value = day;
};

const goToPreviousWeek = () => {
  const firstDay = days.value[0].value;
  const newSelectedDay = days.value[firstDay - 7];
  if (newSelectedDay) {
    selectedDay.value = newSelectedDay;
  }
};

const goToNextWeek = () => {
  const lastDay = days.value[6].value;
  const newSelectedDay = days.value[lastDay + 1];
  if (newSelectedDay) {
    selectedDay.value = newSelectedDay;
  }
};
</script>

<style scoped>
/* Add your styles here */

.tabs-bar {
  display: flex;
  background-color: #2c3e50;
  color: #ecf0f1;
}

.tabs-bar div {
  flex: 1;
  text-align: center;
  padding: 10px;
  cursor: pointer;
}

.tabs-bar .arrow {
  flex: 0.5;
  text-align: center;
  padding: 10px;
  cursor: pointer;
}

.tabs-bar div:hover, .tabs-bar .arrow:hover {
  background-color: #34495e;
}

.tabs-bar div.active {
  background-color: #3498db;
  color: white;
}
</style>
