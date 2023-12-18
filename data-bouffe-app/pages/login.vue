<template>
    <div class="login-container">
      <form @submit.prevent="handleLogin" class="flex flex-col w-56">
        <input v-model="username" type="text" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
        <div class="flex justify-evenly">
            <button type="submit">Login</button>
            <a href="/register">register</a>
        </div>
        <p>{{ error_message }}</p>
      </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { check_auth, login } from '~/lib';

definePageMeta({
    layout : "start"
}
)
const username = ref('');
const password = ref('');
const error_message = ref('');
const router = useRouter();

async function handleLogin()  { 
    const resp = await login(username.value, password.value)
    if (resp.ok) {
        router.push('/dashboard'); 
    }
    else {
        error_message.value = await resp.json()
    }
};

onMounted( async () => {
    const user_infos = await check_auth()
    if (user_infos != null) {
        router.push("/dashboard")
    }
})
</script>

  