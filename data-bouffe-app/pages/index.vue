<template>
    <div class="h-screen flex flex-col justify-center">

        <header class="bg-900 text-maintextcolor text-center py-20">
            <div class="container mx-auto">
                <h1 class="text-4xl font-extrabold">Welcome to DataBouffe</h1>
            </div>
        </header>

        <section class="py-16">
            <div class="container mx-auto text-center">
                <h2 class="text-3xl font-semibold text-gray-800 font-alatsi">Ready to Start Your Meal Planner?</h2>
                <p class="text-gray-600 mt-4">Join DataBouffe and make your diet planning a breeze.</p>
                <!-- Get Started Button with Continuous Active Color -->
                <button class="mt-8 px-6 py-3 rounded-full bg-activecolor text-white font-alatsi">Get Started</button>
                <!-- Learn More Button with White Arrow -->
                <a href="#" class="mt-4 inline-flex items-center px-4 py-2 rounded-full text-activecolor font-alatsi">
                    Learn More
                </a>
            </div>
        </section>
        
      
    </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'start'
})
</script>