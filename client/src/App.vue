<template>
  <div id="app">
    <Header />
    <div id="content">
      <router-view />
    </div>
  </div>
</template>

<script>
import Header from "@/components/Header";

export default {
  components: {
    Header,
  },
};
</script>

<style lang="scss">
#content {
  margin: 1em;
}
</style>
