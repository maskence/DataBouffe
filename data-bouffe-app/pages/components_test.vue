<template>
    <mealCard2 :meal="meal"/>
</template>

<script setup>
import MealCard2 from '~/components/mealCard2.vue';

let meal = { "id": 9082, "name": "Blé dur précuit cuisiné, en sachet micro-ondable", "nutrients": { "glucid": 29.5, "kcal": 188, "lipid": 4.84, "protein": 5.29 } }

</script>