<template>
  <div>
    <h1>The Feed</h1>
    <b-card-group columns>
      <b-card v-for="post in posts" :key="post.id">
        <div class="post-content">{{ post.content }}</div>
        <div class="post-meta text-secondary">
          {{ formatTime(post.time_posted) }} &ndash; @{{ post.author }}
        </div>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
import moment from "moment";

export default {
  created: function () {
    this.$http.get("/api/posts").then((response) => {
      this.posts = response.data.posts;
    });
  },
  data: function () {
    return {
      posts: [],
    };
  },
  methods: {
    formatTime: function (timeString) {
      return moment.utc(timeString).fromNow();
    },
  },
};
</script>

<style lang="scss" scoped>
.card-columns {
  column-count: 1;
  max-width: 30em;
}

.post-meta {
  text-align: right;
}
</style>
