<template>
    <div class="space-y-2">
      <p>POST register/ {{ register_response }}</p>
      <p>POST login/ {{ login_response }}</p>
      <p>GET infos/ {{ goals_response }}</p>
      <p>GET meal_plan/ {{ meal_plan_response }}</p>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { login, get_meal_plan, get_user_goals, register } from "~/lib"

const register_response = ref('awaiting');
const login_response = ref("awaiting")
const goals_response = ref("awaiting")
const meal_plan_response = ref("awaiting")

const username : string = "test"
const password : string = "test"

onMounted(async () => {
  const resp1 = await register(username, password)
  register_response.value = await resp1.json()

  const resp = await login(username, password)
  login_response.value = await resp.json()
  
  goals_response.value = await get_user_goals()
  meal_plan_response.value = await get_meal_plan()
  });
</script>