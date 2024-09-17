<template>
    <div class="flex justify-evenly bg-white rounded-md">
        <p>user : {{ username ? username : "..." }}</p> 
        <button @click="logout_user"> X </button>
    </div>
</template>

<script setup>
import { check_auth, logout } from '~/lib';
import { useRouter, useRoute } from 'vue-router';
import { onMounted, watch } from 'vue';

const router = useRouter()
const route = useRoute();

const username = ref('')

async function logout_user() {
    await logout()
    router.push("/login")
}
async function check_user_auth() {
    const user_infos = await check_auth()
    if (user_infos == null) {
        router.push("/login")
    } else {
        username.value = user_infos.username
    }
}
onMounted(check_user_auth)
watch(() => route.path, () => {
  check_user_auth()
});
</script>