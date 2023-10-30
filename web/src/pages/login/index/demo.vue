<script setup></script>

<template>
  <div class="demo">
    <h2>DEMO</h2>
    <div>
      <p>Email: demo@demo.com</p>
      <p>Senha: 01De@mo85</p>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";
.demo {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin: 20px 0;
  padding: 20px;
  border-radius: $border-radius;
  background-color: $background;

  h2 {
    text-align: center;
  }

  p {
    color: $txt-aside;
    font-weight: 500;
  }
}
</style>
