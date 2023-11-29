<!-- ./src/App.vue -->
<template>
  <div class="parent">
    <div class="div1"><img src="./assets/Banananana.webp" width="100" height="100"></div>
    <div class="div2"> </div>
    <div class="div3"> </div>
    <div class="div4"> </div>
    <div class="div5"> <Results/> </div>
    <div class="div6"> <History/> </div>
    <div class="div7"> </div>
    <div class="div8"> <Search/> </div>
    <div class="div9"> </div>
  </div>
</template>

<script>
import Results from "@/components/Results.vue";
import Search from "@/components/Search.vue";
import History from "@/components/History.vue";

export default {
  name: "App",
   components: {
     Results,
    Search,
    History
   }
};
</script>

<style>
.parent {
  display: grid;
  background-color: #242424;
  grid-template-columns: 0.3fr 2fr 0.5fr;
  grid-template-rows: 0.3fr 1fr 0.3fr;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  height: 100vh;
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
  }
  .div9 { 
    grid-area: 3 / 3 / 4 / 4; 
  }
</style>
