<template>
  <main>
    <h1>Parabéns!</h1>
    <div class="ops">
      <p>
        Você concluiu o processo de cadastro. Fale com seu instrutor para
        prosseguir com os treinos.
      </p>
      <RouterLink to="/welcome"><strong>Conforfit On</strong></RouterLink>
    </div>
  </main>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

main {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  position: fixed;
  width: 100%;
  height: 100%;
  z-index: 888;
  overflow: auto;
  padding: 30px;
  text-align: center;

  @include mq(s) {
    padding: 10px;
  }

  h1 {
    margin-bottom: 30px;
    font-size: 3rem;
    color: $buttons;
  }

  .ops {
    p {
      color: $txt-aside;
      margin-bottom: 20px;
    }

    a {
      color: $logo-color;
      text-decoration: none;
    }
  }
}
</style>
