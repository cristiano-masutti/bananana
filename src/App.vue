<template>
  <div class="parent">
    <div class="div1">
      <a href="/" class="link-to-home" style="text-decoration: none;">
        <div class="inParent">
          <img src="./assets/Banananana.webp" width="100" height="100" alt="Banananana Image">
          <h1 class="custom-h1">Banananana</h1>
        </div>
      </a>
    </div>
    <div class="div2"> </div>
    <div class="div3"> </div>
    <div class="div4"> </div>
    <div v-if="this.queryResult == 0 && !this.search"> <Welcome /> </div>
    <div v-if="this.queryResult == 0 && this.search" class="div6-empty"><NoResults/></div>
    <div v-if="this.queryResult != 0" class="div5"> <Results :results="this.queryResult"/></div>
    <div class="div6"> <History :query="this.query" @item-clicked="handleItemClick" @clear-history="clearArrayHistory" /> </div>
    <div class="div7"> </div>
    <div class="div8"> <Search :oldQuery="this.oldQuery" @search="updateSearch"/> </div>
    <div class="div9"> </div>
  </div>
</template>

<script>
import Results from "@/components/Results.vue";
import Search from "@/components/Search.vue";
import History from "@/components/History.vue";
import Welcome from "@/components/Welcome.vue";
import NoResults from "@/components/NoResults.vue";

export default {
  name: "App",
  components: {
    Results,
    Search,
    History,
    Welcome,
    NoResults
  },
  data() {
    return {
      queryResult : [],
      query: [],
      oldQuery: "",
      search: false
    }
  },
  mounted() {
    this.search = false;
    window.addEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      // Check if the user has reached the bottom of the page
      if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        // Disable or modify the default scroll behavior
        event.preventDefault();

        // You can also perform other actions here if needed
        // For example, loading more content or triggering a function
      }
    },
    updateSearch(query, queryResult) {
      this.search = true;
      this.query.unshift(query);
      this.queryResult = queryResult;
    },
    handleItemClick(clickedItem) {
      console.log('Item clicked in parent:', clickedItem);
      this.oldQuery = clickedItem
    },
    clearArrayHistory() {
      this.query = [];
    }
  },
  beforeUnmount() {
    // Remove the scroll event listener when the component is about to be unmounted
    window.removeEventListener("scroll", this.handleScroll);
  },
  
};
</script>



<style>
.parent {
  display: grid;
  grid-template-columns: 0.3fr 2fr 0.5fr;
  grid-template-rows: 1fr 1fr 1fr; /* Increased the size of the last row to 0.5fr */
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: #242424;
  height: 100vh;
}

.custom-h1 {
  font-family: 'Irish Grover', cursive;
  font-size: 20px;
  color: #D9D9D9;
}

.inParent {
  margin-left: 20px;
  margin-right: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
  
.div1 { 
  grid-area: 1 / 1 / 2 / 2; 
}
.div2 { 
  grid-area: 1 / 2 / 2 / 3; 
}
.div3 { 
  grid-area: 1 / 3 / 2 / 4; 
}
.div4 { 
  grid-area: 2 / 1 / 3 / 2; 
}
.div5 { 
  overflow: auto;
  grid-area: 2 / 2 / 3 / 3; 
}
.div6 { 
  grid-area: 2 / 3 / 3 / 4; 
}
.div7 { 
  grid-area: 3 / 1 / 4 / 2; 
}
.div8 { 
  grid-area: 3 / 2 / 4 / 3;
  border-top: 1px solid white; /* Add a white line on the upper border */
}
.div9 { 
  grid-area: 3 / 3 / 4 / 4;
  border-top: 1px solid white; /* Add a white line on the upper border */
}
.div6-empty{
  height: 76vh;
}

body {
  margin: 0;
  overflow-y: hidden;
  overflow-x: hidden;
}
</style>
