<template>
  <div class="container fixed-top" style="max-width: 150%; padding: 0">
    <nav
      class="main-navbar navbar-expand-lg navbar-light bg-light border-bottom"
    >
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="true"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div
        class="collapse navbar-collapse container"
        id="navbarSupportedContent"
      >
        <ul class="nav me-auto">
          <li class="nav-item col-12 col-lg-auto">
            <router-link
              :to="{ name: 'Home' }"
              class="nav-link link-dark px-2 active"
              >Home</router-link
            >
          </li>
          <li class="nav-item col-12 col-lg-auto">
            <router-link
              v-if="getUser"
              :to="{
                name: 'AnimeList',
                query: { page: 1 },
              }"
              @click="clearUserInputAndReload"
              class="nav-link link-dark px-2"
              >Browse</router-link
            >
            <router-link
              v-else
              :to="{ name: 'Login' }"
              class="nav-link link-dark px-2"
              >Browse</router-link
            >
          </li>
        </ul>
        <ul v-if="!getUser" class="nav auth">
          <li class="nav-item col-12 col-lg-auto">
            <router-link :to="{ name: 'Login' }" class="nav-link link-dark px-2"
              >Login</router-link
            >
          </li>
          <li class="nav-item col-12 col-lg-auto">
            <router-link
              :to="{ name: 'Signup' }"
              class="nav-link link-dark px-2"
              >Sign up</router-link
            >
          </li>
        </ul>
        <ul v-if="getUser" class="nav auth">
          <li class="nav-item col-12 col-lg-auto">
            <a href="javascript:void(0)" class="nav-link link-dark px-2">{{
              getUser.username
            }}</a>
          </li>
          <li class="nav-item col-12 col-lg-auto">
            <a
              href="javascript:void(0)"
              @click="handleLogout"
              class="nav-link link-dark px-2"
              >Logout</a
            >
          </li>
        </ul>
        <div v-if="getUser">
          <SearchBar />
        </div>
      </div>
    </nav>
    <header class="py-3 mb-5 bg-white border-bottom">
      <div
        class="container d-flex flex-wrap justify-content-center"
        style="padding: 0"
      >
        <router-link
          :to="{ name: 'Home' }"
          class="
            d-flex
            align-items-center
            mb-3 mb-lg-0
            me-lg-auto
            text-dark text-decoration-none
          "
          ><h1>Min-helper</h1></router-link
        >
      </div>
    </header>
  </div>
</template>

<script>
import axios from "axios";
import SearchBar from "./SearchBar.vue";
import { mapGetters } from "vuex";

export default {
  name: "Navbar",
  components: {
    SearchBar,
  },

  data() {
    return {
      counter: 0,
    };
  },

  methods: {
    handleLogout() {
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      this.$store.dispatch("updateUser", null);
      this.$router.push("/");
    },

    async clearUserInputAndReload() {
      this.counter++;
      this.$store.dispatch("updateUserInput", this.counter);
      const response = await axios.get("api-v1/animes/");
      this.$store.dispatch("updateAnimesData", response.data);
    },
  },

  computed: {
    ...mapGetters(["getUser"]),
  },

  async created() {
    try {
      const response = await axios.get("api-v1/auth/user/");
      if (response.status == 200) {
        this.$store.dispatch("updateUser", response.data);
      }
    } catch (e) {
      return;
    }
  },
};
</script>

<style>
.main-navbar {
  text-align: left;
  padding: 6px;
}
.auth {
  margin-right: 2rem;
}
.nav-link {
  transition: 0.4s ease-out;
}
.nav-link:hover {
  transition: 0.4s ease-out;
  opacity: 0.8;
}
</style>