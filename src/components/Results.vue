<template>
    <div style="background-color: #242424; height: 75vh; overflow-y: auto;">
      <div class="album-container">
        <AlbumRecord v-for="result in results" :key="result.artist" :result="result" />
      </div>
    </div>
  </template>
  
  <script>
  import AlbumRecord from './AlbumRecord.vue'
  
  export default {
    name: 'SharkVue',
    components: {
      AlbumRecord
    },
    props: {
      results: []
    },
    data() {
      return {
        msg: ""
      }
    },
    async mounted() {
      console.log('Component mounted.')
    },
    methods: {
      
    }
  }
  </script>
  
  <style scoped>
  .album-container {
    display: flex;
    flex-wrap: wrap;
    justify-content:space-around;
  }
  
  /* Adjust the width of AlbumRecord components as needed */
  .album-container AlbumRecord {
    width: 48%; /* Adjust the width as per your layout */
    margin-bottom: 10px; /* Add margin for spacing between elements */
  }
  </style>
  