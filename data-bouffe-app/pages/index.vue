<template>
    <div class="flex flex-col justify-center h-screen">

        <header class="py-20 text-center bg-900 text-maintextcolor">
            <div class="container mx-auto">
                <h1 class="text-4xl font-extrabold">Welcome to DataBouffe</h1>
            </div>
        </header>

        <section class="py-16">
            <div class="container mx-auto text-center">
                <h2 class="text-3xl font-semibold text-gray-800 font-alatsi">Ready to Start Your Meal Planner?</h2>
                <p class="mt-4 text-gray-600">Join DataBouffe and make your diet planning a breeze.</p>
                <!-- Get Started Button with Continuous Active Color -->
                <button class="px-6 py-3 mt-8 text-white rounded-full bg-activecolor font-alatsi"><a href="/login">Get Started</a></button>
                <!-- Learn More Button with White Arrow -->
                <a href="#" class="inline-flex items-center px-4 py-2 mt-4 rounded-full text-activecolor font-alatsi">
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