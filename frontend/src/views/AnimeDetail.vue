<template>
  <div class="container mb-5" style="text-align: left; padding: 0">
    <div class="card border-0 container mb-5">
      <img class="anime-cover-image" :src="animeData.cover_image" />
    </div>
    <div class="container mb-5">
      <h2>
        Description of : <u>{{ animeData.english_name }}</u>
      </h2>
    </div>
    <div
      v-if="animeData.description"
      v-html="animeData.description"
      class="container"
    ></div>
    <div v-else class="container">
      <p>We're sorry, the description isn't available yet.</p>
    </div>
  </div>
  <div class="container" v-if="commentData.results">
    <div
      v-for="comment in commentData.results"
      :key="comment.id"
      class="card mt-5 mb-5"
    >
      <div class="card-header">
        <p style="text-align: left; margin: 0">
          <b>{{ comment.author }} - {{ comment.created_date }}</b>
        </p>
      </div>
      <div class="card-body">
        <p class="card-text" style="text-align: left">
          {{ comment.content }}
        </p>
      </div>
    </div>
  </div>
  <form @submit.prevent="postComment">
    <div class="container mb-5">
      <div class="mb-3">
        <label class="form-label"><b>Add a comment</b></label>
        <textarea v-model="comment" class="form-control" rows="4"></textarea>
        <button class="w-30 btn btn-lg btn-primary mt-3" type="submit">
          post
        </button>
      </div>
    </div>
  </form>
  <div class="container">
    <hr />
  </div>
  <div class="container animes-wrapper">
    <div class="mt-5 mb-5" style="text-align: left">
      <h2>{{ getSubstitutesNumber() }} Animes that you could like</h2>
    </div>
    <div class="row mb-3">
      <transition-group name="fade" appear>
        <div
          class="container mb-3 col-6 col-lg-2"
          v-for="anime in linkedAnimesData"
          :key="anime.id"
        >
          <router-link
            class="router-link"
            :to="{ name: 'AnimeDetail', params: { id: anime.id } }"
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
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "AnimeDetail",
  props: ["id"],

  watch: {
    async $route() {
      if (this.$route.name !== "AnimeDetail") {
        return;
      }
      this.linkedAnimesData = [];
      this.getComment();
      const response = await axios.get(
        `api-v1/animes/${this.$route.params.id}/`
      );
      this.animeData = response.data;
      let linkedAnimesId = Object.values(this.animeData.linked_animes);
      for (const id of linkedAnimesId) {
        this.getLinkedAnimes(id);
      }
      window.scrollTo({ top: 0, behavior: "smooth" });
    },
  },

  data() {
    return {
      animeData: "",
      linkedAnimesData: [],
      comment: "",
      commentData: "",
    };
  },

  methods: {
    async getLinkedAnimes(id) {
      const response = await axios.get(`api-v1/animes/${id}/`);
      this.linkedAnimesData.push(response.data);
    },

    getSubstitutesNumber() {
      return this.linkedAnimesData.length;
    },

    async postComment() {
      await axios.post("api-v1/animes-comments/", {
        author: this.getUser.username,
        anime: this.animeData.id,
        content: this.comment,
      });
      this.comment = "";
      await this.getComment();
    },

    async getComment() {
      const response = await axios.get(
        `api-v1/animes-comments/?anime=${this.$route.params.id}`
      );
      this.commentData = response.data;
    },
  },

  computed: {
    ...mapGetters(["getAnimesData"]),
    ...mapGetters(["getUser"]),
  },

  async created() {
    const response = await axios.get(`api-v1/animes/${this.id}/`);
    this.animeData = response.data;
    let linkedAnimesId = Object.values(this.animeData.linked_animes);
    for (const id of linkedAnimesId) {
      this.getLinkedAnimes(id);
    }
    this.getComment();
  },
};
</script>