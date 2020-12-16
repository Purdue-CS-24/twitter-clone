<template>
  <div>
    <h1>Register</h1>
    <b-alert :show="alertDisplayed" :variant="alertType">
      {{ alertMessage }}
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
      <b-button type="submit" variant="primary">Create Account</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      username: "",
      password: "",
      alertMessage: "",
      alertType: "danger",
      alertDisplayed: false,
    };
  },
  methods: {
    onSubmit: function () {
      this.errorDisplayed = false;
      this.$http
        .post(
          "/api/users/register",
          { username: this.username, password: this.password },
          { withCredentials: true }
        )
        .then((response) => {
          this.alertMessage = response.data.message;
          this.alertType = "success";
          this.alertDisplayed = true;
          setTimeout(() => {
            this.$router.push("/");
          }, 1000);
        })
        .catch((error) => {
          this.alertMessage = error.response.data.message;
          this.alertType = "danger";
          this.alertDisplayed = true;
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
