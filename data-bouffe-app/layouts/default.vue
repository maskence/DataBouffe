<template>
  <div :class="{ 'sidebar-open': sidebarOpen }" class="layout">
    <layout-sidebar :is-open="sidebarOpen" @toggleSidebar="toggleSidebar" />

    <div class="main-content">
      <slot />
    </div>
  </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  
  const sidebarOpen = ref(true);
  
  const toggleSidebar = () => {
    sidebarOpen.value = !sidebarOpen.value;
  };
  </script>
  

<style scoped>
/* Add your global styles here */

.layout {
  display: flex;
}

.sidebar-open .main-content {
  margin-left: 250px; /* Adjust the value based on your sidebar width */
  transition: margin-left 0.3s ease; /* Add smooth transition effect */
}

.main-content {
  margin-left: 78px;
  flex: 1;
  overflow: hidden;
}
</style>