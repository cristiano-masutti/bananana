<template>
  <div class="container">
    <div class="top-container">
        <Results class="results" />
        <History class="history" />
    </div>
    <div class="search-container">
      <Search class="search" />
    </div>
  </div>
</template>

<script>
import Results from "@/components/Results.vue";
import Search from "@/components/Search.vue";
import History from "@/components/History.vue";

export default {
  name: "HomeView",
  components: {
    Results,
    Search,
    History
  }
};
</script>

<style scoped>

.container {
  
}
.top-container {
  margin-top: 100px;
  margin-left: 100px;
  display: flex;
  height: 80vh;
  width: 100%;
  align-items: stretch;
}

.results {
  width: 80%;
  height: 100%;
}

.history {
  height: 100%;
  width: 20%;
}

.search-container {
  height: 10vh;
  margin: 0;
}

/* Add any additional styling as needed for your components */
</style>
