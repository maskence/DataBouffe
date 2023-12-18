<template>
    <div class="page-header">
      <div class="flex page-header-content">
        <slot/>
      </div>
    </div>
  </template>
  
<style scoped>
.page-header {

   padding: 24px 30px 0;

}

.page-header-content {
  max-width: 1440px;
  width: 100%
}

</style>