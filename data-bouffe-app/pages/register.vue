<template>
    <div class="login-container">
      <form @submit.prevent="handle_register" class="flex flex-col w-56">
        <input v-model="username" type="text" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
        <div class="flex justify-evenly">
            <button type="submit">Register</button>
            <a href="/login">login</a>
        </div>
        <p>{{ error_message }}</p>
      </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { get_user_infos, login, register } from '~/lib';

const username = ref('');
const password = ref('');
const error_message = ref('');
const router = useRouter();

async function handle_register()  { 
    const register_response = await register(username.value, password.value)
    if (register_response.ok) {
        
        const login_response = await login(username.value, password.value)
        if (login_response.ok) {
            router.push('/dashboard'); 
        }
        else {
            error_message.value = await login_response.json()
        }
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