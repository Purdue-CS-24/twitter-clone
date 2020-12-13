<template>
  <b-modal
    id="postModal"
    title="Add Post"
    ok-only
    ok-title="Post!"
    @ok="onSubmit()"
  >
    <b-form>
      <b-form-group label="What's on your mind?">
        <b-form-textarea
          v-model="content"
          rows="3"
          max-rows="6"
          required
          autofocus
        ></b-form-textarea>
      </b-form-group>
    </b-form>
  </b-modal>
</template>

<script>
import store from "@/store";

export default {
  data: function () {
    return {
      content: "",
    };
  },
  methods: {
    onSubmit: function () {
      this.$http
        .put(
          "/api/posts/add",
          { content: this.content },
          { withCredentials: true }
        )
        .then(() => {
          this.$router.go();
        })
        .catch(() => {
          store.clearStore();
          this.$router.push("/login");
        });
    },
  },
};
</script>
