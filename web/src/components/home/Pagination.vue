<script setup>
import { ref, computed } from "vue";

const props = defineProps({
  students: Array,
});
const currentPage = ref(0);
const paginationSize = ref(5);
const start = computed(() => paginationSize.value * currentPage.value);
const end = computed(() => start.value + paginationSize.value);
const studentsPages = computed(() =>
  props.students.slice(start.value, end.value)
);
const pageCount = computed(() =>
  Math.ceil(props.students.length / paginationSize.value)
);
</script>

<template>
  <section class="students">
    <div v-for="student in studentsPages" :key="student" class="student">
      <div class="student__container">
        <RouterLink :to="`/student/${student.id}`">
          <div class="student__container__profile">
            <div class="student__container__profile__picture">
              <!-- <img src="../assets/images/default-profile-picture2.jpg" alt="default profile picture"> -->
            </div>
            <div class="student__container__profile__info">
              <div class="student__container__profile__info__name">
                <p>{{ student.name }}</p>
              </div>
            </div>
          </div>
        </RouterLink>
        <div class="student__container__button">
          <div class="student__container__button__box">
            <RouterLink :to="`/student/${student.id}/evaluations`">
              <button>Avaliação</button>
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
    <div class="pagination">
      <button
        @click="currentPage--"
        :disabled="currentPage === 0"
        class="pagination--inactive"
      >
        Anterior
      </button>
      <button
        v-for="(page, id) in pageCount"
        @click="currentPage = page - 1"
        :class="
          id === currentPage ? 'pagination--active' : 'pagination--inactive'
        "
      >
        {{ page }}
      </button>
      <button
        @click="currentPage++"
        :disabled="currentPage >= pageCount - 1"
        class="pagination--inactive"
      >
        Próxima
      </button>
    </div>
  </section>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/variables";
@import "@/assets/styles/mixins";

.students {
  display: flex;
  flex-direction: column;
  gap: 25px;
  width: 100%;

  .student {
    border-radius: $border-radius;
    box-shadow: $box-shadow;
    background-color: white;

    &__container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;

      a {
        flex: 1;
        padding: 16px;
        text-decoration: none;
        transition: 0.2s;

        &:hover {
          filter: brightness(0.8);
        }
      }

      &__profile {
        display: flex;
        flex-wrap: wrap;
        gap: 14px;

        &__picture {
          width: 60px;
          height: 60px;
          border-radius: $border-radius;
          background-image: url("@/assets/images/default-profile-picture2.jpg");
          background-size: cover;
        }

        &__info {
          display: flex;
          flex-direction: column;
          justify-content: space-around;

          &__name {
            font-size: 1.2rem;
            font-weight: 600;
            color: $txt-title;
          }

          &__content {
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            font-size: 0.9rem;
            color: $txt-subtitle;

            @include mq(l) {
              display: none;
            }
          }
        }
      }

      &__button {
        margin-right: 16px;
        button {
          padding: 14px 20px;
          border: none;
          border-radius: $border-radius;
          background-color: $validation;
          color: white;
          cursor: pointer;
          transition: 0.2s;

          &:hover {
            filter: brightness(0.9);
          }

          &:active {
            filter: brightness(0.7);
          }
        }
      }
    }
  }

  .pagination {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-end;
    gap: 10px;

    button {
      padding: 8px 14px;
      border: none;
      box-shadow: $box-shadow;
      border-radius: $border-radius;
      cursor: pointer;
      transition: 0.2s;
    }

    &--inactive {
      background-color: white;
      color: $txt-aside;

      &:active {
        filter: brightness(0.7);
      }

      &:hover {
        background-color: $background;
        filter: brightness(0.9);
      }
    }

    &--active {
      background-color: $buttons;
      color: white;
    }
  }
}
</style>
