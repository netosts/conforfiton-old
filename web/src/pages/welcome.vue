<template>
  <main>
    <h1>Bem-Vindo à Conforfit On</h1>
    <div class="ops">
      <p>Conheça nossa empresa.</p>
    </div>
  </main>
</template>

<style lang="scss" scoped>
@import "../assets/styles/variables";

h1 {
  margin-bottom: 20px;
  font-size: 3rem;
  color: $buttons;
}

.ops {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;

  p {
    color: $txt-aside;
  }

  a {
    color: $logo-color;
    text-decoration: none;
  }
}
</style>
