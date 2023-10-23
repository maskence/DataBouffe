<template>
    <div>
      <Header />
      <Sidebar />
      <main class="ml-64 pt-16 pl-4 pr-4"> <!-- Adjust margins for sidebar width -->
        <slot />
      </main>
    </div>
  </template>
  
  <script>
  import Header from '~/components/layout/header.vue'
  import Sidebar from '~/components/layout/sidebar.vue'
  
  export default {
    components: {
      Header,
      Sidebar
    }
  }
  </script>
  