import Vue from "vue";

export const store = Vue.observable({
    user: localStorage.user,

    isLoggedIn() {
        return this.user != null;
    },
    getUsername() {
        if (this.user) {
            return this.user.username;
        } else {
            return undefined;
        }
    },
    setUsername(username) {
        this.user = {
            "username": username
        };
        this.setLocalStorage();
    },
    clearStore() {
        this.user = null;
        this.setLocalStorage();
    },
    setLocalStorage() {
        localStorage.user = JSON.stringify(this.user);
    }
});

export default store;
