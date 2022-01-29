<template>
  <div class="container mb-5" v-if="getUser">
    <div class="container row" style="max-width: 600px; margin: auto">
      <div class="container col-lg-6 col-12 mb-3">
        <label class="form-label"><b>Genres</b></label>
        <input
          class="form-control"
          list="datalistOptions"
          placeholder="Any"
          v-model="selectedCategory"
          @change="getAnimesFiltered"
        />
        <datalist id="datalistOptions">
          <option v-for="category in categoriesData" :key="category.id">
            {{ category.name }}
          </option>
        </datalist>
      </div>
      <div class="container col-lg-6 col-12">
        <label class="form-label"><b>Scoring</b></label>
        <select
          v-model="selectedScore"
          @change="getAnimesFiltered"
          class="form-select"
          aria-label="Default select example"
        >
          <option selected>Any</option>
          <option value="bestScore">Best</option>
          <option value="lowestScore">Lowest</option>
        </select>
      </div>
    </div>
  </div>
  <div
    v-if="getUser && !getAnimesData.count == 0"
    class="container animes-wrapper"
  >
    <div class="row mb-3">
      <transition-group name="fade" appear>
        <div
          class="container mb-3 col-6 col-lg-2"
          v-for="anime in getAnimesData.results"
          :key="anime.id"
        >
          <router-link
            class="router-link"
            :to="{ name: 'AnimesDetails', params: { id: anime.id } }"
          >
            <div class="anime-card card border-0">
              <img class="anime-cover-image" :src="anime.cover_image" />
              <p class="anime-name">
                <strong>{{ anime.english_name }}</strong>
              </p>
            </div></router-link
          >
        </div>
      </transition-group>
    </div>
    <div class="container">
      <button
        v-if="getAnimesData.previous"
        class="btn btn-primary me-2"
        @click="getPreviousPage"
      >
        Previous
      </button>
      <button
        v-if="getAnimesData.next"
        class="btn btn-primary"
        @click="getNextPage"
      >
        Next
      </button>
    </div>
  </div>
  <div v-else class="container">
    <Error :message="errorMessage" />
  </div>
</template>

<script>
import Error from "../components/Error.vue";
import { mapGetters, mapState } from "vuex";
import { getData } from "../api";

export default {
  name: "AnimeList",
  components: {
    Error,
  },
  data() {
    return {
      errorMessage: "No results found for your search",
      categoriesData: null,
      selectedCategory: null,
      selectedScore: "Any",
    };
  },
  methods: {
    async getAnimesFiltered() {
      if (this.selectedCategory) {
        if (this.selectedScore == "bestScore") {
          const response = await getData(
            `api-v1/animes/?categories=${this.selectedCategory}&ordering=-score`
          );
          this.$store.dispatch("updateAnimesData", response.data);
        } else if (this.selectedScore == "lowestScore") {
          const response = await getData(
            `api-v1/animes/?categories=${this.selectedCategory}&ordering=score`
          );
          this.$store.dispatch("updateAnimesData", response.data);
        } else if (this.selectedScore == "Any") {
          const response = await getData(
            `api-v1/animes/?categories=${this.selectedCategory}`
          );
          this.$store.dispatch("updateAnimesData", response.data);
        }
      } else if (this.getUserInput && isNaN(this.getUserInput)) {
        if (this.selectedScore == "bestScore") {
          const response = await getData(
            `api-v1/animes/?search=${this.getUserInput}&ordering=-score`
          );
          this.$store.dispatch("updateAnimesData", response.data);
        } else if (this.selectedScore == "lowestScore") {
          const response = await getData(
            `api-v1/animes/?search=${this.getUserInput}&ordering=score`
          );
          this.$store.dispatch("updateAnimesData", response.data);
        } else if (this.selectedScore == "Any") {
          const response = await getData(
            `api-v1/animes/?search=${this.getUserInput}`
          );
          this.$store.dispatch("updateAnimesData", response.data);
        }
      } else {
        if (this.selectedScore == "bestScore") {
          const response = await getData("api-v1/animes/?ordering=-score");
          this.$store.dispatch("updateAnimesData", response.data);
        } else if (this.selectedScore == "lowestScore") {
          const response = await getData("api-v1/animes/?ordering=score");
          this.$store.dispatch("updateAnimesData", response.data);
        } else if (this.selectedScore == "Any") {
          const response = await getData("api-v1/animes/");
          this.$store.dispatch("updateAnimesData", response.data);
        }
      }
    },
    async getCategories() {
      const response = await getData("api-v1/animes-categories/");
      this.categoriesData = response.data.results;
    },
    async getNextPage() {
      const response = await getData(this.getAnimesData.next);
      this.$store.dispatch("updateAnimesData", response.data);
      scrollTo(0, 0);
    },
    async getPreviousPage() {
      const response = await getData(this.getAnimesData.previous);
      this.$store.dispatch("updateAnimesData", response.data);
      scrollTo(0, 0);
    },
  },
  computed: {
    ...mapGetters(["getUser"]),
    ...mapGetters(["getAnimesData"]),
    ...mapGetters(["getUserInput"]),
    ...mapState(["userInput"]),
  },
  watch: {
    userInput(newValue, oldValue) {
      if (oldValue != newValue) {
        this.selectedScore = "Any";
        this.selectedCategory = null;
      }
    },
  },
  async created() {
    try {
      const response = await getData("api-v1/animes/");
      this.getCategories();
      this.$store.dispatch("updateAnimesData", response.data);
    } catch (e) {
      this.errorMessage = "You first need to login to access to all the animes";
    }
  },
};
</script>

<style>
.animes-wrapper {
  margin-bottom: 7rem;
}
.anime-card {
  transition: 0.4s ease-out;
}
.anime-card:hover {
  transition: 0.4s ease-out;
  opacity: 0.8;
}
.anime-name {
  text-align: left;
}
.anime-cover-image {
  border-radius: 5px;
  max-width: 196px;
  max-height: 270px;
}
.fade-enter-active,
.fade-leave-active {
  transition: all 1s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.router-link {
  text-decoration: none;
  color: black;
}
</style>