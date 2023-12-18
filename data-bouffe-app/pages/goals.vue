<template>
    
<div v-if="user_goals">
    <p> Your daily goals :</p>
    <div v-for="(value, key) in user_goals" :key="key">
        <div class="flex">
            <p>{{ key }} </p>
            <input type="range" :value="value" min="10" max="3000" @input="update_goal(key, $event.target.value)">
            <p> {{ value }}</p>
        </div>
    </div>
    <button @click="save_user_goals"> save </button>
</div>

</template>

<script setup >
//todo: add a way to change the users goals that connects to the POST goals route of the api.
import { onMounted } from 'vue';
import { get_user_goals, set_user_goals } from '~/lib';

const user_goals = ref()

async function save_user_goals() {
    const response = await set_user_goals(user_goals.value)
}

function update_goal(key , value ) {
    user_goals.value[key] =  value
}
onMounted(async () => {
    user_goals.value = await get_user_goals()

})
</script>