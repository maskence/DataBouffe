<template>
    
<div v-if="user_goals">
    <div v-for="(value, key) in user_goals" >
        <p>{{ key }} : {{ value }}</p>
    </div>
</div>

</template>

<script setup>
//todo: add a way to change the users goals that connects to the POST user_infos route of the api.
import { onMounted } from 'vue';
import { get_user_goals } from '~/lib';

const user_goals = ref()

onMounted(async () => {
    user_goals.value = await get_user_goals()

})
</script>