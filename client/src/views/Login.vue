<template>
  <div>
    <h1>Log In</h1>
    <b-alert :show="errorDisplayed" variant="danger">
      {{ errorMessage }}
    </b-alert>
    <b-form @submit.prevent="onSubmit">
      <b-form-group label="Username:">
        <b-form-input v-model="username" required autofocus></b-form-input>
      </b-form-group>
      <b-form-group label="Password:">
        <b-form-input
          v-model="password"
          type="password"
          required
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Log In</b-button>
    </b-form>
  </div>
</template>

<script>
import store from "@/store";

export default {
  data: function () {
    return {
      username: "",
      password: "",
      errorMessage: "",
      errorDisplayed: false,
    };
  },
  methods: {
    onSubmit: function () {
      this.errorDisplayed = false;
      this.$http
        .post(
          "/api/users/login",
          { username: this.username, password: this.password },
          { withCredentials: true }
        )
        .then((response) => {
          console.log(response);
          store.setUsername(response.data.user.username);
          this.$router.push("/");
        })
        .catch((error) => {
          this.errorMessage = error.response.data.message;
          this.errorDisplayed = true;
        });
    },
  },
};
</script>

<style lang="scss" scoped>
form {
  max-width: 20em;
}
</style>
