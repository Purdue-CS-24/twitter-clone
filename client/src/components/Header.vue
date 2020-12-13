<template>
  <div>
    <b-navbar type="dark">
      <b-navbar-brand to="/">peteSpace</b-navbar-brand>

      <b-navbar-nav class="ml-auto">
        <b-nav-item>
          <b-icon-plus-circle
            v-if="isLoggedIn"
            v-b-modal.postModal
          ></b-icon-plus-circle>
        </b-nav-item>
        <b-nav-item-dropdown right>
          <template #button-content>
            <b-icon-person-circle></b-icon-person-circle>
          </template>
          <b-dropdown-text v-if="isLoggedIn" id="greeting">
            Hello, {{ username }}!
          </b-dropdown-text>
          <b-dropdown-item v-if="isLoggedIn" @click="signOut()"
            >Sign Out</b-dropdown-item
          >
          <b-dropdown-group v-else>
            <b-dropdown-item to="/login">Log In</b-dropdown-item>
            <b-dropdown-item to="/register">Register</b-dropdown-item>
          </b-dropdown-group>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-navbar>

    <PostModal />
  </div>
</template>

<script>
import PostModal from "@/components/PostModal";
import store from "@/store";

export default {
  components: {
    PostModal,
  },
  computed: {
    isLoggedIn: function () {
      return store.isLoggedIn();
    },
    username: function () {
      return store.getUsername();
    },
  },
  methods: {
    signOut: function () {
      this.$http.get("/api/users/logout", { withCredentials: true });
      store.clearStore();
    },
  },
};
</script>

<style lang="scss" scoped>
.navbar {
  background-color: goldenrod;
}

.b-dropdown-text {
  width: 15em;
}

#greeting {
  font-weight: unset;
}
</style>
